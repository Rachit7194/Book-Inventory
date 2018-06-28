from django.urls import path, include
from .views import CustomAuthentication


urlpatterns = [

    path('auth/', CustomAuthentication.as_view(), name ="auth"),
]
