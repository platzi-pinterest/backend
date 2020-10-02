from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from pinterest.users.api.serializers import ProfileModelSerializer
from pinterest.users.api.serializers import (
    UserSerializer,
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Complements
from pinterest.utils.response import CustomActions

User = get_user_model()
custom_actions = CustomActions()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    # users/signup
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handle HTTP POST request."""
        # Make Serializer and Set Data
        serializer = UserSignUpSerializer(data=request.data)
        # Validate Model
        if not serializer.is_valid():
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Error to Signup', serializer.errors)
        else:
            # Save Object
            user = serializer.save()
            # Return User
            content = {"email": UserModelSerializer(user).data.get('email')}
            data = custom_actions.set_response(status.HTTP_201_CREATED, 'Singup Success!', content)
        # Get Status
        return custom_actions.custom_response(data)

    @action(detail=False, methods=['get'])
    def verify(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        # Get Data
        token = request.query_params.get('token')
        # Validate Model
        if not token:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        else:
            # Save Object
            serializer = AccountVerificationSerializer(data={'token': token})
            if not serializer.is_valid():
                data = custom_actions.set_response(
                    status.HTTP_400_BAD_REQUEST, 'Error to Verify', serializer.errors)
            else:
                # Return User
                serializer.save()
                data = custom_actions.set_response(status.HTTP_201_CREATED, 'User Verify!')
        # Get Status
        return custom_actions.custom_response(data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        # Make Serializer and Set Data
        serializer = UserLoginSerializer(data=request.data)
        # Validate Model
        if not serializer.is_valid():
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Error to Login', serializer.errors)
        else:
            # Save Object
            user, token = serializer.save()
            # Return User
            content = {
                'user': UserModelSerializer(user).data,
                'authToken': token
            }
            data = custom_actions.set_response(status.HTTP_200_OK, 'Login Success!', content)
        # Get Status
        return custom_actions.custom_response(data)

    @action(detail=False, methods=['get'])
    def profile(self, request, *args, **kwargs):
        """Get profile data."""
        # Get Data
        user = request.user
        # Validate Model
        if not user:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        else:
            # Get Object
            content = UserModelSerializer(user).data
            # Return User
            data = custom_actions.set_response(status.HTTP_200_OK, 'Get info User!', content)
        # Get Status
        return custom_actions.custom_response(data)

    @action(detail=True, methods=['put', 'patch'])
    def update_profile(self, request, *args, **kwargs):
        """Update profile data."""
        # Get Data
        user = self.get_object()
        # Validate Model
        if not user:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        else:
            # Save Object
            profile = user.profile
            partial = request.method == 'PATCH'
            serializer = ProfileModelSerializer(
                profile,
                data=request.data,
                partial=partial
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            content = UserModelSerializer(user).data
            # Return User
            data = custom_actions.set_response(status.HTTP_201_CREATED, 'User Verify!', content)
        # Get Status
        return custom_actions.custom_response(data)
