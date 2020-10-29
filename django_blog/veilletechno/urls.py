
from django.urls import path
from veilletechno import views

urlpatterns = [
    path('', views.veilletechno, name='veilletechno'),
]



