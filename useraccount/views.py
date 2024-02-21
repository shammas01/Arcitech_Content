from django.shortcuts import render
from . serializers import UserRegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from . models import User
from . auth.smtp import send_activation_email
from rest_framework.response import Response
from rest_framework import status,generics
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate,login
from . auth.jwt import get_tokens_for_user
# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request):
        
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            phone = serializer.validated_data.get('phone')
            pincode = serializer.validated_data.get('pincode')

            hashed_password = make_password(password)
            new_user = User.objects.create(
                email = email,
                password = hashed_password,
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                pincode = pincode
            )

            if new_user != None:
                send_activation_email(
                    user = new_user, email=new_user.email
                )
            
            response = {
                "msg":"register successfully",
                "data":serializer.data
            }
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class UserActivateView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user != None and default_token_generator.check_token(user, token) and user.is_active == False:
            user.is_active = True
            user.save()
            return HttpResponse("<h3>Account activated successfully</h3>", status=200)
        else:
            return HttpResponse("<h3>Invalid activation link</h3>", status=400)
        


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer()
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"massage":f"this is not registred email {email}"})
        
        if user.is_active == True:
            user1 = authenticate(email=email,password=password)
            if user1 != None:
                jwt_token = get_tokens_for_user(user1)
                login(request, user1)
                serializer = UserRegisterSerializer(user1)
                response = {
                    "logined_user":user1.id,
                    "Your email": email,
                    "token": jwt_token,
                    "serializer":serializer.data,
                    "messege": "your account successfull logind",
                }
                return Response(response,status=status.HTTP_200_OK)
            return Response({"massage":"incorrect your password"})
        send_activation_email(
            user=user, email=user.email
        )
        response = {"massage":"check you mail and acitivate your account",
                    "response":"your account is not activated"}
        return Response(response, status=status.HTTP_202_ACCEPTED)
    


    
