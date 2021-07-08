from django.urls import path
from .views import index
from .views import obras

urlpatterns = [
    path('',index,name="index"),
    path('',obras,name="obras"),
]
