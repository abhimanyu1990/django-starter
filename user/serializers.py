from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields=('id','username','first_name','last_name','email','password','groups')
        model =User
        extra_kwargs = {'password':{'write_only':True}}
