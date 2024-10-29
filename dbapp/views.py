from django.shortcuts import render, redirect
from .models import Corporation
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
    return render(request, 'corporations/create.html', {'form': form})

# Update Model
def corporation_update(request):
    if request.method == 'POST':
        form = CorporationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corporation_list')
    else:
        form = CorporationForm()
    return render(request, 'corporations/update.html', {'form': form})