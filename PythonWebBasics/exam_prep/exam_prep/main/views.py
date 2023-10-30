from django.shortcuts import render, redirect

from exam_prep.main.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, ExpenseCreateForm, \
    ExpenseEditForm, ExpenseDeleteForm
from exam_prep.main.models import Profile, Expense


def get_profile():
    profile_set = Profile.objects.all()
    if profile_set:
        return profile_set[0]

    return None


def home_show(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(item.price for item in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home show')
    else:
        form = ExpenseCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home show')
    else:
        form = ExpenseEditForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home show')
    else:
        form = ExpenseDeleteForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def profile_show(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget = profile.budget - sum(item.price for item in expenses)
    context = {
        'profile': profile,
        'expenses_count': len(expenses),
        'budget_left': budget,
    }

    return render(request, 'profile.html', context)


def profile_create(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home show')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile show')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home show')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
