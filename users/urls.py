from django.urls import path
from users.views import LoginLoginView, LogoutLogoutView, RegistrationCreateView

app_name = 'users'

urlpatterns = [
    path('login/', LoginLoginView.as_view(), name='login'),
    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
]
