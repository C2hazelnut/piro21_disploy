from django.shortcuts import render, redirect
from .models import LocalUser
from .forms import LocalUserForm

# Create your views here.
def list(req):
    users = LocalUser.objects.all()
    search_txt = req.GET.get('search_txt')
    
    if search_txt:
        users = users.filter(name__contains = search_txt)
    ctx = {
        'users': users
    }
    return render(req, 'users/list.html', ctx)

def create(req):
    if req.method == "GET":
        form = LocalUserForm()
        ctx = {
            'form': form
        }
        return render(req, 'users/create.html',ctx)
    form = LocalUserForm(req.POST)
    if form.is_valid():
        form.save()
    return redirect("users:list")

def delete(req, pk):
    LocalUser.objects.get(id=pk).delete()
    return redirect("users:list")

def update(req, pk):
    user = LocalUser.objects.get(id=pk)
    if req.method == "GET":
        form = LocalUserForm(instance=user)
        ctx = {
            'form': form
        }
        return render(req, 'users/update.html', ctx)
    form = LocalUserForm(req.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect("users:list")