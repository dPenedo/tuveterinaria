from django.shortcuts import render
from django.shortcuts import redirect
# from usuarios.views import username
from django.contrib.auth import authenticate
from django.contrib.auth import login

def pagina_login(request):
    params = {}
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("verimagenes")
        else:
            return render(request, "usuarios/login.html", params)
    return render(request, "usuarios/login.html", params)
