
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .analysis import possible_outcome, detect_labels_local_file
from .views import home
import boto3

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        print("setup")
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        print("test1")
        self.assertEquals(self.response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        print("test2")
        view = resolve('/')
        self.assertEquals(view.func, home)
 
    def test_api_response(self):
        print('test3')
        photo = '/Users/hongdotcom/Desktop/Sites/django-imgsearch/imgsearch/static/images/bg1.jpg'
        resp = detect_labels_local_file(photo)
        self.assertTrue(resp=='pickup')
    
    def test_possible_outcome_unknown(self):
        res = {'Name':'Human'}
        resp = possible_outcome(res)
        self.assertTrue(resp=='NOT Matched')

