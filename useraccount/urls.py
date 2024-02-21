from django.urls import path
from . views import (
    UserRegistrationView,
    UserActivateView,
    UserLoginView
)


urlpatterns = [
    path('user/register/',UserRegistrationView.as_view(),name='registratio'),
    path('users/activate/<uidb64>/<token>/', UserActivateView.as_view(), name='user_activate'),
    path('user/login/',UserLoginView.as_view(),name='user_loging'),
]
