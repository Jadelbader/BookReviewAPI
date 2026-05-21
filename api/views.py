from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    BookSerializer,
    ReviewSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):

        user = request.user

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not user.check_password(old_password):

            return Response(
                {"error": "Old password is incorrect"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Password changed successfully"}
        )


class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):

        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]

        return [permissions.AllowAny()]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):

        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]

        return [permissions.AllowAny()]