from django.test import TestCase
from account.models import *

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
#         User.objects.create(username="TestUser", password="testPass")
#         Experiment.objects.create(name="Experiment1", )
        user1 = User(username="testUsername", password="testPassword")
        user1.save()
        
        user2 = User(username="testUsername2", password="testPassword") 
        user2.save()
        
    def testcheckUsers(self):
        self.assertEqual(user1, User.objects.get(username="testUsername"))
        self.assertEqual(user2, User.objects.get(username="testUsername2"))