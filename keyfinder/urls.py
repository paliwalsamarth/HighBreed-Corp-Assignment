from django.urls import path

from keyfinder.views import KeyFinderTemplateView

urlpatterns = [
    path("", KeyFinderTemplateView.as_view(), name="index"),
]
