""" My app for password storing testing """
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    user = request.user
    return render_to_response('usermanagement/home.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
