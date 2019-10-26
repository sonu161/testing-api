import self as self
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Tag


def sample_user(email='test@mail.com',password='testpass'):
    """Create sample user"""
    return get_user_model().objects.create_user(email,password)

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
         """Test creating a new user"""
         email = 'sonu.swain61@gmail.com'
         password = 'testpass'
         user = get_user_model().objects.create_user(
             email=email,
             password=password
         )

         self.assertEqual(user.email,email)
         self.assertTrue(user.check_password(password))



    def test_new_user_email_normalize(self):
        """Test user email normalize"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Validating email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_super_user(self):
        """Create new super user"""
        user = get_user_model().objects.create_superuser(
            'testsuper@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag strin representation"""

        tag = Tag.objects.create(
            user=sample_user(),
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)