from mixins import CreateUserMixin
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm



class LoginAndLoginRedirectTest(CreateUserMixin, TestCase):

    def setUp(self):
        self.user = self.create_user('existing_user')

    def test_redirection_to_login_on_anonymous_user_access_profile_page(self):
        response = self.client.get('/usermanagement/')
        self.assertRedirects(
            response,
            'login?next=/usermanagement/',
             status_code=302,
             target_status_code=301
        )
    
    def test_login(self):
        self.client.login(username = self.user.username, password = self.password)
        response = self.client.get('/usermanagement/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usermanagement/home.html')

    def test_failed_login_redirect(self):
        self.client.login(username = self.user.username, password = 'wrongpass')
        response = self.client.get('/usermanagement/')
        self.assertRedirects(
            response,
            'login?next=/usermanagement/',
             status_code=302,
             target_status_code=301
        )

    def test_failed_login(self):
    	response = self.client.post('/login/', {'username': self.user.username, 'password': 'wrongpass'})
    	self.assertTemplateUsed(response, 'registration/login.html')

class RegisterTest(TestCase):

    def test_register_form_is_valid(self):
        form = UserCreationForm(data={'username': 'test', 'password1': 'test123', 'password2': 'test123'})
        self.assertTrue(form.is_valid())

    def test_register_form_is_invalid(self):
        form = UserCreationForm(data={'username': 'test', 'password1': 'test123', 'password2': 'test12'})
        self.assertFalse(form.is_valid())

    def test_register_successful(self):
        response = self.client.post('/usermanagement/register/', {'username': 'test', 'password1': 'test123', 'password2': 'test123'})
        self.assertRedirects(
            response,
            '/login/',
             status_code=302,
             target_status_code=200
        )

    def test_register_unsuccessful(self):
        response = self.client.post('/usermanagement/register/', {'username': 'test', 'password1': 'test123', 'password2': 'test12'})
        self.assertTemplateUsed(response, 'registration/register.html')