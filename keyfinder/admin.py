from django.contrib import admin

from keyfinder.models import KeywordModel, UrlModel

# Register your models here.
admin.site.register(UrlModel)
admin.site.register(KeywordModel)
