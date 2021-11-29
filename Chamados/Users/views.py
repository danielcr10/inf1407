
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth.models import User, Group

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     # fields = ['first_name', 'last_name', 'email', 'group']
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
