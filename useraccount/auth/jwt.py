from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, *args):
        token = super().get_token(user)
        if user.email:
            token["email"] = user.email
        return token


def get_tokens_for_user(user, *args):
    refresh = MyTokenSerializer.get_token(user, *args)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }