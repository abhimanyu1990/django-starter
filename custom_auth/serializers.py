from rest_framework import serializers, exceptions
from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type":   "password"})
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password','password2','groups')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        groups = validated_data["groups"]
        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(username=username, email=email, groups = groups, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user
