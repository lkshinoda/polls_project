from django.test import TestCase
from django.urls import reverse


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
