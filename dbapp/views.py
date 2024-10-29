from django.shortcuts import render, redirect
from .models import Corporations
from .forms import CorporationForm


#Create Model
def corporation_create(request):
    if request.method == 'POST':
        form = CorporationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corporation_list')
    else:
        form = CorporationForm()
    return render(request, 'corp_views/create.html', {'form': form})

# Update Model
def corporation_update(request):
    if request.method == 'POST':
        form = CorporationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corporation_list')
    else:
        form = CorporationForm()
    return render(request, 'corp_views/update.html', {'form': form})

#Delete Model
def corporation_delete(request):
    if request.method == 'POST':
        form = CorporationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corporation_list')
    else:
        form = CorporationForm()
    return render(request, 'corp_views/delete.html', {'form': form})

#List view to display all corporations
def corporation_list(request):
    corporations = Corporation.objects.all()
    return render(request, 'corp_views/list.html', {'corporations': corporations})