""" Users Logic """

# Django Library
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model

# Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Tasks
from pinterest.taskapp.tasks import send_confirmation_email

# Models
from pinterest.users.models import Profile

# Get Model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'name',
            'email',
        )


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user/profile creation.
    """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)

    # Name
    name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify passwords match."""
        # Check Password
        passwd = data['password']
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        # Make User
        user = User.objects.create_user(**data, is_verified=False, is_client=True)
        Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user
