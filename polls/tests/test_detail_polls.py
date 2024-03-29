"""These module is use for testing the polls."""

import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

def create_question(question_text, days):
    """Create a question with the given `question_text` and published the \
        given number `days` offset to now (negative for questions published \
        in the past, positive for questions that have yet to be published)."""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionDetailViewTests(TestCase):
    """Creating question that test only View class."""

    def test_future_question(self):
        """The detail view of a question with a pub_date \
            in the future returns a 302 not found."""
        future_question = create_question(question_text='Future question.',
                                          days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_past_question(self):
        """The detail of a question with a pub_date in \
            the past displays the question's text."""
        past_question = create_question(question_text="Past question.",
                                        days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
