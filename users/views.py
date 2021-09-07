from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import UserForm, InfoForm
from .models import UserProfile
from django.contrib import messages
# Create your views here.

class Register(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'registration/register.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.get(user=user)
            userprofile.email = request.POST.get('email')
            userprofile.save()
            username = self.request.POST['username']
            password = self.request.POST['password1']
            #authenticate user then login
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect("covidtracker:index")
            
        return render(request, 'registration/register.html', {'form' : form})
