from django.db import models


# Create your models here.
class KeywordModel(models.Model):
    keyword = models.CharField(max_length=50)

    def __str__(self):
        return self.keyword


class UrlModel(models.Model):
    url = models.CharField(max_length=500)
    keyword = models.ManyToManyField(KeywordModel)

    def __str__(self):
        return self.url
