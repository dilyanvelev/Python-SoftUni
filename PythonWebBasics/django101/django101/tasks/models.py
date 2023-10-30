from django.db import models


# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class ModelView(models.Model):
    name = models.CharField(max_length=78)

    def __str__(self):
        return f'name: {self.name}'


class ModelView1(models.Model):
    name = models.CharField(max_length=78)

    def __str__(self):
        return f'name: {self.name}'
