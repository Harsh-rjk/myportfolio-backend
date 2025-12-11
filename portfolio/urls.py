from django.urls import path
from . import view


urlpatterns = [
   path("", view.harsh),
   path("addentry/", view.addentry),
   path("getentry/", view.getentry),
]

