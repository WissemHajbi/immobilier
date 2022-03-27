from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from immobilier.forms import register
from django.contrib import messages
from .models import sale

class landing_page(ListView):
    model = sale
    template_name = "landing_page\\landing_page.html"
    
def register_view(request):
    user = request.user
    if user.is_authenticated:
        messages.success(request, f"you are already logged in as {user.username}" )
        return redirect("landing_page")
    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("login")
    else:
        form = register()
    return render(request, "authentication\\registration.html", context={"registration":form}) 

class login_view(LoginView):
    template_name = "authentication\\login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("landing_page")