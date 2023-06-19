from django.test import TestCase

from ..utils import spam_check


class SpamCheckTest(TestCase):
    def test_spam_check(self):
        self.assertTrue(spam_check("normal comment"))
        self.assertFalse(spam_check("comment with link https://www.google.com/"))
        self.assertFalse(spam_check("comment with another link gmail.com"))
        self.assertFalse(spam_check("Poker in casino"))
