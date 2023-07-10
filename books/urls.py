from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("templates/books/", views.index, name="index"),
  path("templates/empresas/", views.empresas, name="empresas")
]