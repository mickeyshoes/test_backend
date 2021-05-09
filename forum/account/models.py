from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.http import Http404

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, login_id, email, password):
        
        if not login_id:
            raise ValueError('User must have an own ID')

        if not email:
            raise ValueError('User must have an own email')

        if not password:
            raise ValueError('User must have an own password')

        user = self.model(
            login_id = login_id,
            email = self.normalize_email(email) # email 형식을 지키면서 소문자로 변경
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login_id, email, password):

        user = self.model(
            login_id = login_id,
            email = email,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

    def get_object_or_404(self, login_id):
        try:
            user = User.objects.get(login_id=login_id)
            return user

        except User.DoesNotExist:
            raise Http404("No User matches the given query")

class User(AbstractBaseUser, PermissionsMixin):

    login_id = models.CharField(
        max_length = 50,
        unique = True,
        verbose_name = 'login_id'
    )

    email = models.EmailField(
        max_length = 100,
        unique = True
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELD = ['email']

    class Meta:
        verbose_name = 'user'

        def __str__(self):
            return self.login_id