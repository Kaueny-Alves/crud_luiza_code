from django.shortcuts import render, redirect
from app.modelsPacotes import Pacotes
from app.models import Empresas
from app.forms import EmpresasForm, PacotesForm
from django.http import HttpResponseRedirect

def home(request):
  data = {}
  search = request.GET.get('search')
  
  if search:
    data['db'] = Empresas.objects.filter(modelo__icontains = search)
  else:
    data['db'] = Empresas.objects.all()
  return render(request, 'index.html', data)

def form(request):
  data = {'form': EmpresasForm()}
  return render(request, 'form.html', data)

def create(request):
  form = EmpresasForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")
  
def view(request, pk):
  data = {'db': Empresas.objects.get(pk = pk)}
  return render(request, 'view.html', data)

def edit(request, pk):
  data = {}
  data['db'] = Empresas.objects.get(pk = pk)
  data['form'] = EmpresasForm(instance = data['db'])
  return render(request, 'form.html', data)

def update(request, pk):
  data = {}
  data['db'] = Empresas.objects.get(pk = pk)
  form = EmpresasForm(request.POST or None, instance = data['db'])
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")
  
def delete(request, pk):
  db = Empresas.objects.get(pk = pk)
  db.delete()
  return HttpResponseRedirect("/")

def createPacotes(request):
  form = PacotesForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")

def formPacotes(request):
  data = {'form': PacotesForm()}
  return render(request, 'formPacotes.html', data)

def deletePacotes(request, pk):
  db = Pacotes.objects.get(pk = pk)
  db.delete()
  return HttpResponseRedirect("/form")

def updatePacotes(request, pk):
  data = {}
  data['db'] = Pacotes.objects.get(pk = pk)
  form = PacotesForm(request.POST or None, instance = data['db'])
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")
  
def getPacotes(request,pk):
  data = {'db': Empresas.objects.get(pk = pk)}
  return render(request, 'view.html', data)