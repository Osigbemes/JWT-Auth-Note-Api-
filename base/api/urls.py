from django.urls import path
from . import views
from .views import MyTokenObtainPairView, RegisterUserView, DeleteUserView, GetUserView, GetAllUserView
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('get-all/', GetAllUserView.as_view(), name='get-all'),
    path('get-user/<str:pk>', GetUserView.as_view(), name='get-user'),
    path('delete/<str:pk>', DeleteUserView.as_view(), name='delete'),
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('create-notes/', views.postNotes)
]
