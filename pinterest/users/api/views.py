from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, UserSignUpSerializer, UserModelSerializer

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
