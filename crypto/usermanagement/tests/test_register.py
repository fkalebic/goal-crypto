from testcases import BaseTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from private import *


class FailedRegisterPageTestCase(BaseTestCase):
    def setUp(self):
         super(FailedRegisterPageTestCase, self).setUp()

    def test_register_wrong_pass(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/usermanagement/register')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_elements_by_xpath("//*[@type='submit']")

        #Fill the form with data
        username.send_keys('new_user')
        password1.send_keys('fsdd')
        password2.send_keys('jhf')

        #sumbit the form
        for i in submit:
             i.click()

        message = selenium.find_element_by_css_selector('.errorlist li')

        self.assertEqual(
            message.text,
            "The two password fields didn't match."
        )

    def test_register_existing_user(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/usermanagement/register')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_elements_by_xpath("//*[@type='submit']")

        #Fill the form with data
        username.send_keys(USERNAME)
        password1.send_keys('pass')
        password2.send_keys('pass')

        #sumbit the form
        for i in submit:
             i.click()

        message = selenium.find_element_by_css_selector('.errorlist li')

        self.assertEqual(
            message.text,
            "A user with that username already exists."
        )

