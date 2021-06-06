from django.urls import path

from homeapp.views import HomeTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="index"),
]
