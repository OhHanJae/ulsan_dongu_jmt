from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("jmt/get_result", views.result, name='get_result'),
]