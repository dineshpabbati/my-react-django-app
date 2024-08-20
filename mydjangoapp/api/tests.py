from django.test import TestCase
from django.urls import reverse

class ApiTests(TestCase):
    def test_api_home(self):
        response = self.client.get(reverse('api_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the API")

    def test_api_data(self):
        response = self.client.get(reverse('api_data'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"name": "John Doe", "age": 30, "location": "Boston"}
        )
