# Create your tests here.
# from django.core.exceptions import ValidationError
# from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from keyfinder.forms import KeyFinderForm
from keyfinder.models import UrlModel
from keyfinder.utils import get_keywords
from keyfinder.views import recommend_keys

# from django.views.generic import View


class AppSearchTests(TestCase):
    data = {
        "correct_inputURL": "https://stackoverflow.com/",
        "correct_inputURL2": "https://www.interviewbit.com/",
        "incorrect_inputURL": "https://a.a/",  # determined by validations of urlfield
        "incorrect_inputURL2": "https://www.google.coda/",  # determined by sending get request to site
    }

    # @classmethod
    # def setUpTestData(cls):
    #     user_data = dict(cls.data)

    def test_index_view(self):
        url = reverse("keyfinder:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("keyfinder:index")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_get_keywords(self):
        keywords = get_keywords(self.data.get("correct_inputURL"))
        self.assertTrue(len(keywords) > 0)

        keywords2 = get_keywords(self.data.get("incorrect_inputURL"))
        self.assertIsNone(keywords2)

        keywords = get_keywords(self.data.get("correct_inputURL2"))
        self.assertTrue(len(keywords) > 0)

        keywords2 = get_keywords(self.data.get("incorrect_inputURL2"))
        self.assertIsNone(keywords2)

    def test_forms_n_recommendation(self):
        form_data = {"something": "something"}
        form = KeyFinderForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {"inputURL": self.data.get("incorrect_inputURL")}
        form = KeyFinderForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {"inputURL": self.data.get("incorrect_inputURL2")}
        form = KeyFinderForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_obj = form.save()
        self.assertIsNone(form_obj)
        self.assertTrue(form.errors)

        form_data = {"inputURL": self.data.get("correct_inputURL")}
        form = KeyFinderForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_obj = form.save()
        self.assertIsNotNone(form_obj)
        self.assertFalse(form.errors)

        form_data = {"inputURL": self.data.get("correct_inputURL2")}
        form = KeyFinderForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_obj = form.save()
        self.assertIsNotNone(form_obj)
        self.assertFalse(form.errors)

        # checking recommendation
        input_url_obj = UrlModel.objects.get(url=self.data.get("correct_inputURL2"))
        context = recommend_keys(input_url_obj)
        self.assertEquals(context["status"], "success")
        self.assertTrue(len(context["inputKeywords"]) > 0)
        self.assertTrue(len(context["outputKeywords"]) > 0)

        input_url_obj = UrlModel.objects.get(url=self.data.get("correct_inputURL"))
        context = recommend_keys(input_url_obj)
        self.assertEquals(context["status"], "success")
        self.assertTrue(len(context["inputKeywords"]) > 0)
        self.assertTrue(len(context["outputKeywords"]) > 0)
