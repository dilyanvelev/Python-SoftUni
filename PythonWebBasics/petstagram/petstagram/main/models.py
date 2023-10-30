import datetime

from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main.validators import only_letters_validator, image_max_size_validator, ValidateFileMaxSizeInMb, \
    MinDateValidator, MaxDateValidator


# Create your models here.

class Profile(models.Model):
    # Constants
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    # generating tuples for choices
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # Fields(Cols)
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,

    )

    # One-to-one relations

    # One-to-many relations

    # Many-to-many relation

    # Properties

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # dunder methods

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # Meta class


class Pet(models.Model):
    # Constants
    NAME_MAX_LENGTH = 30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    MIN_DATE = datetime.date(1920,1,1)

    # Fields(Cols)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,

    )

    type = models.CharField(
        # to set max_length to the len() of the biggest word in TYPES
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(),
        )
    )

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}: {self.type}'

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # image_max_size_validator(5),
            ValidateFileMaxSizeInMb,
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )

    description = models.TextField(
        null=True,
        blank=True,

    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
