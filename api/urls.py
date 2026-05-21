from django.urls import path
from .views import (
    RegisterView,
    ChangePasswordView,
    BookListCreateView,
    BookDetailView,
    BookReviewsView,
    ReviewDetailView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('books/', BookListCreateView.as_view(), name='book_list_create'),

    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    path('books/<int:book_id>/reviews/', BookReviewsView.as_view(), name='book_reviews'),

    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
]