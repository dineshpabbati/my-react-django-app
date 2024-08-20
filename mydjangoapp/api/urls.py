from django.urls import path
from .views import api_home, api_data

urlpatterns = [
    path('', api_home, name='api_home'),  
    path('data/', api_data, name='api_data'),  
]

