from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from comprasApp.views import Vista_comprar


urlpatterns = [
    path('<int:id>', login_required(Vista_comprar.as_view()), name='comprar')
]