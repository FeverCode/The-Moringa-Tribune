import email
from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestCase(TestCase):
    
    # Set up method
    def setUp(self):
        self.giddy= Editor(first_name = 'Giddy', last_name = 'Lancs', email = 'giddy@mail.com')
        
#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.giddy,Editor))
        
    # Testing Save Method
    def test_save_method(self):
        self.giddy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
