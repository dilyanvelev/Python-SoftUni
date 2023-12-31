from django.shortcuts import render, redirect

from petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto, Profile, Pet


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))
    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()

    total_likes = sum(pet_photo.likes for pet_photo in pet_photos)
    total_pet_photos_count = len(PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
    context = {
        'profile': get_profile(),
        'total_likes': total_likes,
        'total_pet_photos_count': total_pet_photos_count,
        'pets': pets
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        # create form with post
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        # create empty form
        form = form_class(instance=instance)

    context = {
        'form': form,
    }
    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


# if request.method == 'POST':
#     # create form with post
#     form = CreateProfileForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
# else:
#     # create empty form
#     form = CreateProfileForm()
#
# context = {
#     'form': form,
# }
# return render(request, 'profile_create.html', context)


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')


# profile = get_profile()
# if request.method == 'POST':
#     form = EditProfileForm(request.POST, instance=profile)
#     if form.is_valid():
#         form.save()
#         return redirect('profile details')
# else:
#     form = EditProfileForm(instance=profile)
#
# context = {
#     'form': form,
# }
# return render(request, 'profile_edit.html', context)


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
