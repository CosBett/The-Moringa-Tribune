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

class ArticleTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.mandela = Editor(first_name = 'mandela', last_name ='Bett', email = 'cosmasbett9@gmail.com')
    self.mandela.save_editor()

  # creating a new tag and saving it
    self.new_tag =tags(name ='testing')
    self.new_tag.save()

    self.new_article = Article(title ='Test Article', post ='This is a random test article', editor ='self.mandela')
    self.new_article.save()
    self.new_article.tags.add(self.new_tag)

  def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Article.objects.all().delete() 
  