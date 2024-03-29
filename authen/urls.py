from django.urls import path
from authen.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:id>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:id>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('get-user/',UserView.as_view(),name='get_user'),
    path('get-user-personal/',UserPersonal.as_view(),name='get_user_personal'),
    path('check-email',CheckEmailView.as_view(),name='check_email'),
    path('get-add/',Getaddresses.as_view(),name='check_email'),

]