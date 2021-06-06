from django.urls import path

from appsearch.views import AppSearchTemplateView

urlpatterns = [
    path("", AppSearchTemplateView.as_view(), name="index"),
]
