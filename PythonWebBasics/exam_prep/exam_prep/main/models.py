from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep.main.validators import validate_only_letters, MaxFileSizeInMbValidator


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )
    )
    # TODO: watch the lecture how it's done
    profile_image = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    EXPENSE_MAX_LENGTH = 30
    title = models.CharField(
        max_length=EXPENSE_MAX_LENGTH,
    )

    # TODO: watch the lecture how it's done
    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
