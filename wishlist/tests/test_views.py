from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import WishlistForm
from ..models import Wishlist, WishlistItem

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

class WishlistCreateTest(CreateTestUserMixin, TestCase):
    
    def test_wishlist_create_url_resolves_to_correct_view(self):
        self.create_test_user()
        response = self.client.get('/wishlist/create/', follow=True)
        self.assertTemplateUsed(response, 'create_wishlist.html')
        
    def test_wishlist_create_page_redirects_to_login_for_anon_user(self):
        response = self.client.get('/wishlist/create/', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')
        
    def test_wishlist_create_page_uses_wishlist_form(self):
        self.create_test_user()
        response = self.client.get('/wishlist/create/')
        self.assertIsInstance(response.context['form'], WishlistForm)
        
    def test_valid_POST_creates_new_wishlist(self):
        self.create_test_user()
        response = self.client.post(
            '/wishlist/create/',
            data={'name': 'Test Wishlist 1'},
            follow=True
        )
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertEqual(Wishlist.objects.first().name, 'Test Wishlist 1')
        
    def test_blank_name_field_returns_error(self):
        self.create_test_user()
        response = self.client.post(
            '/wishlist/create/',
            data={'name': ''},
            follow=True
        )
        self.assertFormError(
            response, 'form', 'name', 'This field is required.'
        )
        
        
class WishlistDetailViewTest(CreateTestUserMixin, TestCase):

    def setUp(self):
        self.create_test_user()
        user = User.objects.first()
        Wishlist.objects.create(owner=user, name='Test Wishlist 1')
        
    def test_wishlist_detail_url_resolves_to_correct_view(self):
        response = self.client.get('/wishlist/detail/1/')
        self.assertTemplateUsed(response, 'wishlist_detail.html')
        
    def test_wishlist_detail_redirects_to_login_for_anon_user(self):
        self.client.get('/accounts/logout/')
        response = self.client.get('/wishlist/detail/', follow=True)
        
    def test_valid_POST_creates_new_wishlist_item(self):
        self.client.post(
            '/wishlist/detail/1/',
            data={'description': 'Test 1', 'link': 'https://www.google.com'},
            follow=True
        )
        self.assertEqual(WishlistItem.objects.count(), 1)
        self.assertEqual(WishlistItem.objects.first().description, 'Test 1')