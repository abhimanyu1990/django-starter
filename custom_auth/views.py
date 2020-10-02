from rest_auth.serializers import LoginSerializer
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from drf_yasg.utils import swagger_auto_schema
from user.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_auth.app_settings import (
   LoginSerializer)
from rest_auth.utils import jwt_encode
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from .serializers import UserRegisterSerializer

@swagger_auto_schema(method='POST', request_body=LoginSerializer)
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def loginAuth(request):
    serializer = LoginSerializer(
    data=request.data,
    context={
        'request': request
    })
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    token = jwt_encode(user)
    data = {
                'user':serializer.data.get("username"),
                'token':token
    }
    response = Response(data, status=status.HTTP_200_OK)
        
    from rest_framework_jwt.settings import api_settings as jwt_settings
    if jwt_settings.JWT_AUTH_COOKIE:
        from datetime import datetime
        expiration = (datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA)
        response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
    return response

@swagger_auto_schema(method='POST', request_body=UserRegisterSerializer)
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserRegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    if user:
        res = serializer.data
        return response.Response(res, status.HTTP_201_CREATED)
    
    res={
        "error":"something went wrong"
    }
    return response.Response(res,status.HTTP_400_BAD_REQUEST)


    

