from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Organization, Location, BloodDetail, Transaction, Distance
from .forms import OrganizationForm, BloodDetailForm

def organization_create_view(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood_detail_create')  # Redirect to blood detail form
    else:
        form = OrganizationForm()
    return render(request, 'myapp/organization_form.html', {'form': form})


def blood_detail_create_view(request):
    blood_details = BloodDetail.objects.all()

    if request.method == 'POST':
        form = BloodDetailForm(request.POST)
        if form.is_valid():
            form.save()
            form = BloodDetailForm()
            blood_details = BloodDetail.objects.all()
            
    else:
        form = BloodDetailForm()
    
    return render(request, 'myapp/blood_detail_form.html', {'form': form,'blood_details': blood_details})


def login(request):
    return render(request,'myapp/login.html')