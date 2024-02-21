from rest_framework import serializers
from . models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','email','password','password_2','first_name','last_name','phone','pincode']

    def validate(self, attrs):
        password = attrs.get('password')
        password_2 = attrs.get('password_2')

        if len(password) <= 7:
            raise serializers.ValidationError("password must contain atleast 8 characters")
        if password != password_2:
            raise serializers.ValidationError("password did't match")
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise serializers.ValidationError("Password must contain at least one lowercase letter")
        return attrs