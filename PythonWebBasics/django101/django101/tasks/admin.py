from django.contrib import admin

from django101.tasks.models import Model, ModelView, ModelView1


# Register your models here.
@admin.register(Model)
@admin.register(ModelView)
@admin.register(ModelView1)
class ModelAdmin(admin.ModelAdmin):
    pass




