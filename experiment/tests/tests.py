from django.test import TestCase
from account.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from experiment.views import createTable, insertTable, tableExist
# Create your tests here.

class ExperimentTestCase(TestCase):
    def setUp(self):
#         User.objects.create(username="TestUser", password="testPass")
#         Experiment.objects.create(name="Experiment1", )
        user1 = User(username="testUsername", password="testPassword")
        user1.save()
        
        experiment1 = Experiment(name = "Exp1", description="test")
        experiment2 = Experiment(name = "Exp2", description="test")

        experiment1.save()
        experiment2.save()

        
        user1.experiments.add(experiment1, experiment2)
        user1.save()
        
#     def checkRelations(self):
#         u1 = Experiment.objects.get(name = "testUsername")
#         u2 = Experiment.objects.get(name = "testUsername2")
#         
#         #self.assertEqual(a, b) does a == b? 
        
    def testTable(self):
        """
        Tests the table creation method, check if table exists method,
        and the table insert method
        """
        table_name = "tableForTest"
        sqlQuery = """
            CREATE table {} (
            val1 VARCHAR(3),
            val2 VARCHAR(3),
            val3 VARCHAR(3)
            );"""
        data1 = {"val1": "1", "val2":"2", "val3":"3"}
        data2 = {"val1": "12", "val2":"23", "val3":"33"}
        data3 = {"val1": "13", "val2":"21", "val3":"d3"}
        data = [data1 ,data2, data3]
        CreateTable(table_name, sqlQuery)
        #check if table exists
        self.assertTrue(tableExist(table_name))
        #Insert data into table
        InsertTable(table_name, data1)
        cur = cursor.connection()
        
        self.assertTru(data1, cur.fetchone())
        
    
        
        
        