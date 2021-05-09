from django.test import TestCase
from .models import User

#model input test
class UserModelTest(TestCase):

    def test_create_user(self):

        data = {
            'login_id' : 'hello',
            'email' : 'hi@naevr.com',
            'password' : 'qwerty'
        }

        User.objects.create(login_id = data['login_id'], email= data['email'], password=data['password'])

        user = User.objects.get_object_or_404(login_id= data['login_id'])

        self.assertEquals(user.login_id, data['login_id'])
        self.assertEquals(user.login_id, 'hi')
