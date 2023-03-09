from django.urls import path
from . import views

urlpatterns = [
    path("", views.europa, name="europa"),
    path("frança", views.frança, name="frança"),
    path("italia", views.italia, name="italia"),
    path("suecia", views.suecia, name="suecia")

]
