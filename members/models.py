from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Used to create the Custom User and it's manager


class StudentUserManager(BaseUserManager):
    """
    Manage the blog user, email is the login identifier and first name and last name are mandatory
    """

    def create_user(self, email, first_name, last_name, password=None):
        """
        Create and save an User with the given EMAIL, FIRST_NAME, LAST_NAME and Password.
        """
        if not email:
            raise ValueError("Blog user must have an email address")
        if not first_name:
            raise ValueError("Blog user must have a First name")
        if not last_name:
            raise ValueError("Blog user must have a Last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Create and save an Super User with the given EMAIL, FIRST_NAME, LAST_NAME and Password.
        """

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# def get_image_extension(filename):
#     if "." in filename:
#         return filename.split(".")[-1]
#     else:
#         return None

# def get_profile_image_filepath(self, filename):
#     """
#     Returns the profile name path to store
#     """
#     extension = get_image_extension(filename)
    
#     if extension is not None:
#         return f"images/profile_images/{self.pk}/profile_image.{extension}"
#     else:
#         return f"images/profile_images/{self.pk}/profile_image.png"



# def get_default_profile_image():
#     """
#     Returns the default profile image
#     """

#     return "images/default_profile_image/default_gilflc.png"


# Custom User Model

class BlogUser(AbstractBaseUser):
    """
    Basic Custom User for the Blog
    """
    username = None

    email = models.EmailField(verbose_name="email", max_length=70, unique=True)
    full_name = models.CharField(max_length=150)

    date_joined = models.DateTimeField(
        verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    hide_email = models.BooleanField(default=True)

    
    objects = StudentUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name",]

    def __str__(self):
        return str(self.full_name)


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
