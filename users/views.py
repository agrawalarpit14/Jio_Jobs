from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from post.models import Post
# Create your views here.
def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Welcome to JIO Jobs')
			return redirect('user-login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance= request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.userprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated')
			return redirect('user-profile')

	else:
		u_form = UserUpdateForm(instance= request.user)
		p_form = ProfileUpdateForm(instance= request.user.userprofile) 
	context = {
		'u_form' : u_form,
		'p_form' : p_form,
		'posts': Post.objects.all()
	}
	return render(request, 'users/profile.html', context)