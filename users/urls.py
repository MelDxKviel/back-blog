from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import UserLogin, ProfileView, UserRegister, ProfileEditView, ProfileChangePassword, ProfileDeleteView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='posts'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<pk>/edit', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/<pk>/delete', ProfileDeleteView.as_view(), name='profile_delete'),
    path('profile/changepass', ProfileChangePassword.as_view(), name='profile_changepass'),
    path('register/', UserRegister.as_view(), name='register')
]
