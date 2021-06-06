import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from keyfinder.forms import KeyFinderForm
from keyfinder.models import UrlModel

# Create your views here.


class KeyFinderTemplateView(TemplateView):

    template_name = "keyfinder/page2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["currpage"] = "keyfinder"
        context["nOfURL"] = UrlModel.objects.count()
        context["form"] = KeyFinderForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == "POST":
            form = KeyFinderForm(request.POST)
            try:
                if form.is_valid():
                    url_obj = form.save()
                    context = recommend_keys(url_obj)
                    return HttpResponse(
                        json.dumps(context), content_type="application/json"
                    )
                else:
                    raise ValidationError("invalid url")
            except ValidationError:
                context = {
                    "status": "fail",
                    "message": form._errors["inputURL"][0],
                }  # To display 1 error at a time
                return HttpResponse(
                    json.dumps(context), content_type="application/json"
                )
        else:
            return redirect("keyfinder:index")


def recommend_keys(urlObj):
    keyObj_list = []

    keyObj_list = urlObj.keyword.all()

    urlObjs = UrlModel.objects.filter(keyword__in=keyObj_list).distinct()

    keyObj_list = set(keyObj_list)
    resultKeywords = set()

    for urlObj in urlObjs:
        currUrlKeywords = set(urlObj.keyword.all())
        if len(currUrlKeywords.intersection(keyObj_list)) >= 3:
            resultKeywords.update(currUrlKeywords)

    resultKeywords = resultKeywords.difference(keyObj_list)

    context = {
        "status": "success",
        "message": "URL Processed !",
        "inputKeywords": [i.keyword for i in keyObj_list],
        "outputKeywords": [i.keyword for i in resultKeywords],
        "nOfURL": UrlModel.objects.count(),
    }

    return context
