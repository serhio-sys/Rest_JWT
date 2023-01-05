from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from PostApp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter().urls

urlpatterns = router


urlpatterns += [
    path('admin/', admin.site.urls),
    path('posts/',PostsViewSets.as_view({'post':'create','get':'list'})),
    path('posts/<pk>/',PostsViewSets.as_view({'get':'retrieve','put':'update','patch':'partial_update'})),
    path('posts/<pk>/cat/',PostsViewSets.as_view({'get':'CatsSort'})),
    path("api-session/",include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
