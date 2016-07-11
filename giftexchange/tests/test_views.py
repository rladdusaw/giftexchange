from django.contrib.auth import get_user_model
from django.test import TestCase

from registration.forms import RegistrationForm

from wishlist.models import Wishlist

User = get_user_model()


class CreateTestUserMixin(object):
    
    def create_test_user(self, username='test'):
        self.client.post(
            '/accounts/register/',
            data={
                'username': username,
                'email': 'test@test.com',
                'password1': 'adhvis47',
                'password2': 'adhvis47'
            },
            follow=True
        )

class HomeViewTest(CreateTestUserMixin, TestCase):
    
    def test_root_url_resolves_to_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_home_page_shows_logged_in_users_username(self):
        self.create_test_user()
        response = self.client.get('/')
        self.assertIn(b'Welcome, test', response.content)
        
class RegistrationViewTest(CreateTestUserMixin, TestCase):

    def test_registration_url_resolves_to_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertTemplateUsed(response, 'registration/registration_form.html')
        
    def test_registration_page_uses_registration_form(self):
        response = self.client.get('/accounts/register/')
        self.assertIsInstance(response.context['form'], RegistrationForm)
    
    def test_valid_POST_creates_user(self):
        self.create_test_user()
        self.assertEqual(User.objects.count(), 1)
        new_user = User.objects.first()
        self.assertEqual(new_user.username, 'test')
        
    def test_invalid_POST_reloads_with_errors(self):
        response = self.client.post(
            '/accounts/register/',
            data={
                'username': 'test',
                'email': 'test@test.com',
                'password1': 'adhvis47',
                'password2': 'adhvis'
            },
            follow=True
        )
        self.assertTemplateUsed(response, 'registration/registration_form.html')
        self.assertFormError(
            response, 'form', 'password2',
            'The two password fields didn\'t match.'
        )
        
    def test_sucessful_POST_redirects_to_profile_page(self):
        response = self.create_test_user()
        self.assertTemplateUsed(response, 'profile.html')
    
class ProfileViewTest(CreateTestUserMixin, TestCase):
    
    def setUp(self):
        self.create_test_user()
        
    def test_profile_url_resolves_to_profile_view(self):
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'wishlist_list.html')
    
    def test_profile_shows_users_wishlists(self):
        user = User.objects.first()
        Wishlist.objects.create(owner=user, name='list1')
        Wishlist.objects.create(owner=user, name='list2')
        response = self.client.get('/profile/')
        self.assertIn(b'list1', response.content)
    
    def test_profile_does_not_show_other_users_wishlists(self):
        self.create_test_user('test2')
        user1 = User.objects.get(id='1')
        user2 = User.objects.get(id='2')
        Wishlist.objects.create(owner=user1, name='list1')
        Wishlist.objects.create(owner=user2, name='list2')
        response = self.client.get('/profile/')
        self.assertIn(b'list2', response.content)
        self.assertNotIn(b'list1', response.content)
        