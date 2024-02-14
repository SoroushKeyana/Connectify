# userprofile/views.py

from django.shortcuts import render, redirect
from .forms import AboutMeForm, ChangeCoverPicForm, ChangeProfilePicForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required
def change_cover_pic(request, username):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ChangeCoverPicForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:user_profile', username=request.user.username)
    else:
        form = ChangeCoverPicForm(instance=user_profile)

    return render(request, 'change_cover_pic.html', {'form': form})

@login_required
def change_profile_pic(request, username):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ChangeProfilePicForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:user_profile', username=request.user.username)
    else:
        form = ChangeProfilePicForm(instance=user_profile)

    return render(request, 'change_profile_pic.html', {'form': form})

@login_required
def user_profile_view(request, username):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'user_profile.html', {'username': username})

@login_required
def about_me(request, username):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:user_profile', username=request.user.username)
    else:
        form = AboutMeForm(instance=user_profile)

    return render(request, 'about_me.html', {'form': form})

