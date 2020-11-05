from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectTest(TestCase):
    """ Test module for Project model """

    def setUp(self):
        Project.objects.create(
            title='Test', link='https://github.com', description='Test project', user=self.user)
       