# Create your tests here.

# from django.core.exceptions import ValidationError
# from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from appsearch.forms import AppSearchForm
from appsearch.utils import get_android_app_info, get_apple_app_info
from appsearch.views import get_app_info

# from django.views.generic import View


class AppSearchTests(TestCase):
    data = {
        "correct_android_appID": "com.appxplore.voidtroopers",
        "correct_scraped_android_app_name": "Void Troopers : Sci-fi Tapper",
        "incorrect_android_appID": "com.appxplore.void",
        "correct_apple_appID": "id1367822033",
        "correct_apple_appName": "void-troopers-sci-fi-tapper",
        "correct_scraped_apple_app_name": "Void Troopers : Sci-fi Tapper",
        "incorrect_apple_appID": "ip1367822034",
    }

    # @classmethod
    # def setUpTestData(cls):
    #     user_data = dict(cls.data)

    def test_index_view(self):
        url = reverse("appsearch:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("appsearch:index")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_get_app_info(self):
        context = get_app_info("android", self.data.get("correct_android_appID"), None)
        self.assertEqual(context["status"], "success")
        self.assertEqual(context["message"], "App Found !")
        self.assertEqual(
            context["name"], self.data.get("correct_scraped_android_app_name")
        )

        context = get_app_info(
            "android", self.data.get("incorrect_android_appID"), None
        )
        self.assertEqual(context["status"], "fail")
        self.assertEqual(context["message"], "Invalid App ID")
        self.assertIsNone(context.get("name"))

        context = get_app_info(
            "apple",
            self.data.get("correct_apple_appID"),
            self.data.get("correct_apple_appName"),
        )
        self.assertEqual(context["status"], "success")
        self.assertEqual(context["message"], "App Found !")
        self.assertEqual(
            context["name"], self.data.get("correct_scraped_apple_app_name")
        )

        context2 = get_app_info(
            "apple",
            self.data.get("incorrect_apple_appID"),
            self.data.get("correct_apple_appName"),
        )
        self.assertEqual(context2["status"], "fail")
        self.assertEqual(context2["message"], "Invalid App ID or Name")
        self.assertIsNone(context2.get("name"))

    def test_get_android_app_info(self):
        context = get_android_app_info(self.data.get("correct_android_appID"))
        self.assertEqual(context["status"], "success")
        self.assertEqual(context["message"], "App Found !")
        self.assertEqual(
            context["name"], self.data.get("correct_scraped_android_app_name")
        )

        context = get_android_app_info(self.data.get("incorrect_android_appID"))
        self.assertEqual(context["status"], "fail")
        self.assertEqual(context["message"], "Invalid App ID")
        self.assertIsNone(context.get("name"))

    def test_get_apple_app_info(self):
        context = get_apple_app_info(
            self.data.get("correct_apple_appID"), self.data.get("correct_apple_appName")
        )
        self.assertEqual(context["status"], "success")
        self.assertEqual(context["message"], "App Found !")
        self.assertEqual(
            context["name"], self.data.get("correct_scraped_apple_app_name")
        )

        context2 = get_apple_app_info(
            self.data.get("incorrect_apple_appID"),
            self.data.get("correct_apple_appName"),
        )
        self.assertEqual(context2["status"], "fail")
        self.assertEqual(context2["message"], "Invalid App ID or Name")
        self.assertIsNone(context2.get("name"))

    def test_forms(self):
        form_data = {"something": "something"}
        form = AppSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {
            "storeName": "apple",
            "appID": self.data.get("correct_apple_appID"),
            "appName": self.data.get("correct_apple_appName"),
        }
        form = AppSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {
            "storeName": "android",
            "appID": self.data.get("correct_android_appID"),
        }
        form = AppSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
