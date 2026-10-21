from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator





validate_username_chars = RegexValidator(
    r"^[a-z0-9_]{3,20}$",
    "username فقط می‌تواند حروف کوچک لاتین، عدد و _ داشته باشد (۳ تا ۲۰ کاراکتر)",
)

class UserManager(BaseUserManager):

    use_in_migrations = True


    def _create_user(self, username, password, **extra):
        username = username.strip().lower()
        if not username:
            raise ValueError("username is empty!")
        user = self.model(username=username, **extra)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, username, password=None, **extra):
        extra.setdefault('is_staff', False)
        extra.setdefault('is_superuser',False)
        return self._create_user(username, password, **extra)



    def create_superuser(self, username , password=None , **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)

        if extra.get("is_staff") is not True:
            raise ValueError("is_staff must be true")
        if extra.get("is_superuser") is not True:
            raise ValueError("is_superuser must be true")

        return self._create_user(username, password, **extra)





class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True, validators=[validate_username_chars ])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS=[]

    objects = UserManager()

