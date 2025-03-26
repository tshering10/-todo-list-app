from django.urls import path
from users.views import RegisterView, UserLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
]
