from django.urls import path, include

from .views import *

urlpatterns = [
    path('', profile_view, name='home'),
    path('dashboard/', dashboard, name='admin'),
    path('dashboard/', include('myresume.urls_dashboard')),
]


