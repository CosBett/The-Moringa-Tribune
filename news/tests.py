import email
from django.test import TestCase
from .models import Editor,Article,tags


class EditorTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.mandela = Editor(first_name = 'mandela', last_name ='Bett', email = 'cosmasbett9@gmail.com')
  # test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.mandela,Editor))   