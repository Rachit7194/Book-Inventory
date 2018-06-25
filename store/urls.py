from django.urls import path, include

from store.views import StoreAppFirst

urlpatterns = [

    path('demopage/', StoreAppFirst.as_view(), name="demopage"),
]