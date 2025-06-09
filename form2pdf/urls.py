from django.urls import path
from . import views

urlpatterns = [
    path('form_data/', views.get_form_data, name='form_data'),
    path('download/', views.download, name='download'),
]
