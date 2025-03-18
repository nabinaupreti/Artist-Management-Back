# user/urls.py
# from django.urls import path
# from .views import RegisterView, LoginView, ProtectedView,RefreshTokenView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('protected/', ProtectedView.as_view(), name='protected'),
#     path('refresh/', RefreshTokenView.as_view(), name='refresh'),
# ]

from django.urls import path
from .views import SignupView, LoginView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]

# "first_name": "test",
#     "last_name": "test",
#     "emil": "nabina@gmail.com",
#     "password": "1234",
#     "gender":"male",
#     "role_type": "artist"