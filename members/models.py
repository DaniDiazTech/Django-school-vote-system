from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Grade class linked to the User Model



# Used to create the Custom User and it's manager
class Grade(models.Model):
    PRIMARY = 1
    HIGH = 2

    level_choices = (
        (PRIMARY, 'Primaria'),
        (HIGH, 'Bachillerato'),
    )

    level = models.PositiveSmallIntegerField(
        choices=level_choices,
        default=PRIMARY,
    )

    grade = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        Show the grade name in the admin Page
        """
        return self.grade


class StudentUserManager(BaseUserManager):
    """
    Manage the blog user, email is the login identifier and first name and last name are mandatory
    """

    def create_user(self, email, full_name, password=None):
        """
        Create and save an User with the given EMAIL, FULL_NAME and Password.
        """
        if not email:
            raise ValueError("Cada estudiante debe tener un email valido")
        if not full_name:
            raise ValueError("Cada estudiante debe tener nombre completo")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        """
        Create and save an Super User with the given EMAIL, FIRST_NAME, LAST_NAME and Password.
        """

        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# KINDER = 1
# TRANSICION = 2
# PRIMERO = 3
# SEGUNDO = 4
# TERCERO = 5
# CUARTO = 6
# QUINTO = 7
# SEXTO = 8
# SEPTIMO = 9
# OCTAVO = 10
# NOVENO = 11
# DECIMO = 12
# ONCE = 13

# GRADES = (
#     (KINDER, 'Kinder'),
#     (TRANSICION, 'Transición'),
#     (PRIMERO, '1°'),
#     (SEGUNDO, '1°'),
#     (TERCERO, '1°'),
#     (CUARTO, '1°'),
#     (QUINTO, '1°'),
#     (SEXTO, '1°'),
#     (SEPTIMO, '1°'),
#     (OCTAVO, '1°'),
#     (NOVENO, '1°'),
#     (DECIMO, '1°'),
#     (ONCE, '1°'),
# )

# grade = models.PositiveSmallIntegerField(
#     choices=STATUS,
#     default=ONCE,
# )


# Custom User Model
class StudentUser(AbstractBaseUser):
    """
    Basic Custom User for the Blog
    """
    username = None


    email = models.EmailField(verbose_name="email", max_length=70, unique=True)
    full_name = models.CharField(max_length=150)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)

    date_joined = models.DateTimeField(
        verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)

    has_voted = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    hide_email = models.BooleanField(default=True)

    objects = StudentUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", ]

    def __str__(self):
        return str(self.full_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
