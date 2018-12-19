from django import forms
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .models import Review

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['gender', 'age', 'skills', 'mobile', 'location', 'priceperday']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['gender', 'age', 'skills', 'mobile', 'location', 'priceperday']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']