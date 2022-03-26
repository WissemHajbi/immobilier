from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from immobilier.forms import register

""" class landingoPage(ListView):
    model = ""
    template_name = "" """
    
def register_view(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("you are already registred as "+ User.email)
    
    context = {}
    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = register()
    context["registration"] = form
    return render(request, "authentication\\registration.html", context) 
