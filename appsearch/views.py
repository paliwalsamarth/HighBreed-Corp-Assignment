import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

# from books.models import Book, Publisher
from appsearch.forms import AppSearchForm
from appsearch.utils import get_android_app_info, get_apple_app_info

# Create your views here.


class AppSearchTemplateView(TemplateView):

    template_name = "appsearch/page1.html"
    # model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["currpage"] = "appsearch"
        context["form"] = AppSearchForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == "POST":
            form = AppSearchForm(request.POST)
            if form.is_valid():
                storeName = form.cleaned_data["storeName"]
                appID = form.cleaned_data["appID"]
                appName = form.cleaned_data["appName"]
                context = self.get_app_info(storeName, appID, appName)
                return HttpResponse(
                    json.dumps(context), content_type="application/json"
                )
            else:
                message = [str(i) + str(form._errors[i]) for i in form._errors]
                # print(form.__dict__)
                # print(message)
                context = {"status": "fail", "message": message[0]}
                return HttpResponse(
                    json.dumps(context), content_type="application/json"
                )
        else:
            return redirect("appsearch:index")

    def get_app_info(self, storeName, appID, appName):
        if storeName == "apple":
            context = get_apple_app_info(appID, appName)
        else:
            context = get_android_app_info(appID)

        context["storeName"] = storeName
        return context
