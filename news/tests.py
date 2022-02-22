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
  # Testing Save method
  def test_save_method(self):
    self.mandela.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors) > 0)
