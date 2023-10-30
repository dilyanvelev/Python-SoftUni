from django.urls import path

from exam_prep.main.views import home_show, expense_create, expense_edit, expense_delete, profile_show, \
    profile_edit, profile_delete, profile_create

urlpatterns = (
    path('', home_show, name='home show'),

    path('create/', expense_create, name='expense create'),
    path('edit/<int:pk>/', expense_edit, name='expense edit'),
    path('delete/<int:pk>/', expense_delete, name='expense delete'),

    path('profile/', profile_show, name='profile show'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),

)
