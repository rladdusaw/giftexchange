from django.test import TestCase
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateTestUserMixin(object):

    def create_test_user(self):
        self.client.post(
            '/authenticate/register/',
            data={
                'username': 'test@email.com',
                'password1': 'test',
                'password2': 'test'
            },
            follow=True
        )

    def log_test_ueser_in(self):
        return self.client.post(
            '/authenticate/login/',
            data={'username': 'test@email.com', 'password': 'test'},
            follow=True
        )


class HomeViewTest(CreateTestUserMixin, TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_shows_name_of_authenticated_user(self):
        self.create_test_user()
        self.log_test_ueser_in()
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('Welcome, test@email.com', response.content)


class ErrorViewTest(TestCase):

    def test_error_url_resolves_to_error_page_view(self):
        response = self.client.get('/authenticate/error/')
        self.assertTemplateUsed(response, 'error.html')


class LogoutViewTest(CreateTestUserMixin, TestCase):

    def test_logout_view_logges_user_out(self):
        self.create_test_user()
        self.log_test_ueser_in()
        response = self.client.get('/')
        self.assertContains(response, 'Welcome, test@email.com')
        response = self.client.get('/authenticate/logout/', follow=True)
        self.assertContains(response, 'Welcome, Anonymous User')

    def test_logout_view_returns_home_page(self):
        self.create_test_user()
        response = self.log_test_ueser_in()
        self.assertContains(response, 'secret')
        response = self.client.get('/authenticate/logout/', follow=True)
        self.assertTemplateUsed(response, 'home.html')


class RegistrationViewTest(CreateTestUserMixin, TestCase):

    def test_register_url_resolves_to_registration_view(self):
        response = self.client.get('/authenticate/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_registration_page_uses_user_creation_form(self):
        response = self.client.get('/authenticate/register/')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_valid_POST_requests_are_saved(self):
        self.create_test_user()
        self.assertEqual(User.objects.count(), 1)
        new_user = User.objects.first()
        self.assertIn('test@email.com', new_user.get_username())

    def test_invalid_POST_requests_are_not_saved(self):
        self.client.post(
            '/authenticate/register/',
            data={
                'username': 'test@email.com',
                'password1': 'test',
                'password2': 'nottest'
            }
        )
        self.assertEqual(User.objects.count(), 0)

    def test_registration_redirects_after_POST(self):
        response = self.create_test_user()
        self.assertTemplateUsed(response, 'login.html')


class LoginViewTest(CreateTestUserMixin, TestCase):

    def test_login_url_resolves_to_login_view(self):
        response = self.client.get('/authenticate/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_valid_user_can_login_sucessfully(self):
        self.create_test_user()
        response = self.log_test_ueser_in()
        self.assertEqual(
            response.context['user'].get_username(),
            'test@email.com'
        )

    def test_login_redirects_after_sucessful_login(self):
        self.create_test_user()
        response = self.log_test_ueser_in()
        user = User.objects.filter(username='test@email.com')
        self.assertTemplateUsed(response, 'secret.html')
