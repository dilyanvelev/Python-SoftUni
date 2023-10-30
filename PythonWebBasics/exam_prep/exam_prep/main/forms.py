import os

from django import forms

from exam_prep.main.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class ExpenseEditForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class ExpenseDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
