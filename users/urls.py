from django.urls import path, include
from rest_framework import routers
from .views import UserView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

router = routers.DefaultRouter()
router.register('', UserView, 'users')


urlpatterns = [
    path('',include(router.urls) ),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token'),
    path('auth/token_refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
]