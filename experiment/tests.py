from django.test import TestCase
from .models import *
from account.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

class ExperimentTestCase(TestCase):
    def setUp(self):
#         User.objects.create(username="TestUser", password="testPass")
#         Experiment.objects.create(name="Experiment1", )
        user1 = User(username="testUsername", password="testPassword")
        user1.save()
        
        user2 = User(username="testUsername2", password="testPassword") 
        user2.save()
        
        experiment1 = Experiment(name = "Exp1", description="test")
        experiment2 = Experiment(name = "Exp2", description="test")
        experiment3 = Experiment(name = "Exp3", description="test")
        experiment4 = Experiment(name = "Exp4", description="test")
        experiment1.save()
        experiment2.save()
        experiment3.save()
        experiment4.save()
        
        user1.experiments.add(experiment1, experiment2)
        user2.experiments.add(experiment3, experiment4)
        user1.save()
        user2.save()
        
    def checkRelations(self):
        u1 = Experiment.objects.get(name = "testUsername")
        u2 = Experiment.objects.get(name = "testUsername2")
        
        self.assertEqual(u1.experiments.all()[0], 'user1 works with "Exp1"')
        self.assertEqual(u1.experiments.all()[1], 'user1 works with "Exp2"')
       
        self.assertEqual(u2.experiments.all()[0], 'user1 works with "Exp3"')
        self.assertEqual(u2.experiments.all()[1], 'user1 works with "Exp4"')      
        
  