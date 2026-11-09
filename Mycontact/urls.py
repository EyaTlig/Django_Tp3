from django.urls import path
from .views import controleform

urlpatterns = [
    path('first/',controleform,name="firstcontact"),


]