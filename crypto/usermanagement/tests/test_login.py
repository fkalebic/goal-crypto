from pages import LoginPage
from testcases import BaseTestCase
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium import webdriver
from private import *



class FailedLoginPageTestCase(BaseTestCase):
    def setUp(self):
         super(FailedLoginPageTestCase, self).setUp()

    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_elements_by_xpath("//*[@type='submit']")

        #Fill the form with data
        username.send_keys('regular')
        password.send_keys('fsdd')

        #sumbit the form
        for i in submit:
             i.click()

        message = selenium.find_element_by_css_selector('.errorlist li')

        self.assertEqual(
            message.text,
            'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        )

class LoginPageTestCase(BaseTestCase):
    
    def setUp(self):
         super(LoginPageTestCase, self).setUp()

    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_elements_by_xpath("//*[@type='submit']")

        #Fill the form with data from private.py
        username.send_keys(USERNAME)
        password.send_keys(PASS)
        
        #sumbit the form
        for i in submit:
             i.click()

        message = selenium.find_element_by_css_selector('.section h2')

        self.assertEqual(
            message.text,
            'Hello, regular'
        )