""" My app for password storing testing """
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    return render_to_response('usermanagement/home.html', {'user': user})
