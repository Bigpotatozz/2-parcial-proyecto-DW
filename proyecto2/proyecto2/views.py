from django.shortcuts import render, redirect
from django.contrib.auth import login
from proyecto2.forms import RegistroForm
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Group

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, created = Group.objects.get_or_create(name='cliente')
            user.groups.add(grupo)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request,"registration/registro.html",{"form":form})

class Home_page_view(TemplateView):
    template_name = 'home.html'