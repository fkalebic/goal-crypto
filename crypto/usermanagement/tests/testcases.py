from urlparse import urljoin

from django.test import LiveServerTestCase
from selenium import webdriver


class BaseTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.selenium = webdriver.Firefox()

    def tearDown(self):
        self.selenium.quit()
