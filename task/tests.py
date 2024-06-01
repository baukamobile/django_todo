
from django.test import TestCase

# Create your tests here.
class TestCase(TestCase):
    def testindex(self):
        response = self.client.get('/task/')
        self.assertEqual(response.status_code, 200)
    def testindex2(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
    def testinde3(self):
        response = self.client.get('//')
        self.assertEqual(response.status_code, 200)
    # def testindex4(self):
    #     response = self.client.get('/<int:id>/update/')
    #     self.assertEqual(response.status_code, 200)
