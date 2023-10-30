from django.core.validators import validate_integer
from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=20,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        validators=(
            validate_integer,
        )
    )

    job_title = models.IntegerField(

        choices=(
            (1, 'Software Developer'),
            (2, 'QA Engineer'),
            (3, 'DevOps Specialist'),
        )
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profiles',
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.department}'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employee
    )
