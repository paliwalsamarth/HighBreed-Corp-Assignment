from django import forms
from django.core.exceptions import ValidationError

from keyfinder.models import KeywordModel, UrlModel
from keyfinder.utils import get_keywords


class KeyFinderForm(forms.Form):
    inputURL = forms.URLField()

    def save(self):
        url = self.cleaned_data.get("inputURL", None)
        try:
            urlObj = UrlModel.objects.get(url=url)
            return urlObj
        except UrlModel.DoesNotExist:
            allKeywords = get_keywords(url)

            if allKeywords is None:
                raise ValidationError("Invalid Url")
                # self.add_error("inputURL", "Invalid Url")
                # means url is invalid
            else:
                urlObj = UrlModel.objects.create(url=url)

                for key in allKeywords:  # #TODO maybe can use bulk func to speedup
                    keyObj, created = KeywordModel.objects.get_or_create(keyword=key)
                    urlObj.keyword.add(keyObj)
                urlObj.save()
                return urlObj
