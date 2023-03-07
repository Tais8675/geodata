from django.urls import path
from . import views

urlpatterns = [
    path("", views.america, name="america"),
    path("canada", views.canada, name="canada"),
    path("mexico", views.mexico, name="mexico")

]
