# Create your tests here.

# from django.core.exceptions import ValidationError
# from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

# from django.views.generic import View


class HomeAppTests(TestCase):
    def test_index_view(self):
        url = reverse("homeapp:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("homeapp:index")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 405)
