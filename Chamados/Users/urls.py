from django.urls import path

from . import views

urlpatterns = [
    # path('register/', views.SignUp.as_view(), name='register'),
    path('register/', views.signup, name='register'),
]