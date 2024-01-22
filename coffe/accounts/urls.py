from django.urls import path
from .views import RegistrationAPIView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
