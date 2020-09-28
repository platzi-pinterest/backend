"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from pinterest.users.permissions.user import IsAccountOwner

# Serializers
from pinterest.users.serializers.profiles import ProfileModelSerializer
from pinterest.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Complements
from pinterest.utils.responses import CustomActions

# Models
from pinterest.users.models import User


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """
    custom_actions = CustomActions()

    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action:
            if self.action in ['signup', 'login', 'verify']:
                permissions = [AllowAny]
            elif self.action in ['partial_update', 'profile']:
                permissions = [IsAuthenticated, IsAccountOwner]
            else:
                permissions = [IsAuthenticated]
            return [permission() for permission in permissions]

    # users/login

    @action(detail=False, methods=['post'])
    def login(self, request):
        # Make Serializer and Set Data
        serializer = UserLoginSerializer(data=request.data)
        # Validate Model
        if not serializer.is_valid():
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Error to Login', serializer.errors)
        else:
            # Save Object
            user, token = serializer.save()
            # Return User
            content = {
                'user': UserModelSerializer(user).data,
                'authToken': token
            }
            data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'Login Success!', content)
        # Get Status
        return self.custom_actions.custom_response(data)

    # users/signup
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handle HTTP POST request."""
        # Make Serializer and Set Data
        serializer = UserSignUpSerializer(data=request.data)
        # Validate Model
        if not serializer.is_valid():
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Error to Signup', serializer.errors)
        else:
            # Save Object
            user = serializer.save()
            # Return User
            content = {"email": UserModelSerializer(user).data.get('email')}
            data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'Singup Success!', content)
        # Get Status
        return self.custom_actions.custom_response(data)

    @action(detail=False, methods=['get'])
    def verify(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        # Get Data
        token = request.query_params.get('token')
        # Validate Model
        if not token:
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        else:
            # Save Object
            serializer = AccountVerificationSerializer(data={'token': token})
            if not serializer.is_valid():
                data = self.custom_actions.set_response(
                    status.HTTP_400_BAD_REQUEST, 'Error to Verify', serializer.errors)
            else:
                # Return User
                serializer.save()
                data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'User Verify!')
        # Get Status
        return self.custom_actions.custom_response(data)

    @action(detail=False, methods=['get'])
    def profile(self, request, *args, **kwargs):
        """Get profile data."""
        # Get Data
        user = request.user
        # Validate Model
        if not user:
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        else:
            # Get Object
            content = UserModelSerializer(user).data
            # Return User
            data = self.custom_actions.set_response(status.HTTP_200_OK, 'Get info User!', content)
        # Get Status
        return self.custom_actions.custom_response(data)

    @action(detail=True, methods=['put', 'patch'])
    def update_profile(self, request, *args, **kwargs):
        """Update profile data."""
        # Get Data
        user = self.get_object()
        # Validate Model
        if not user:
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
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
            data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'User Verify!', content)
        # Get Status
        return self.custom_actions.custom_response(data)
