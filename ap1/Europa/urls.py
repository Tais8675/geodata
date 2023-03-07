from django.urls import path
from . import views

urlpatterns = [
    path("", views.europa, name="europa"),
    path("", views.frança, name="frança"),
    path("", views.italia, name="italia"),
    path("", views.suecia, name="suecia")

]
