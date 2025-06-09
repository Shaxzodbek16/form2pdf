from django.urls import path

urlpatterns = [
    path("form_data/", lambda x: x, name="form_data"),
    path("download/", lambda x: x, name="download"),
]
