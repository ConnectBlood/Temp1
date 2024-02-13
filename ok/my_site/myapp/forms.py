from django import forms
from .models import Organization , BloodDetail

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'email', 'state', 'district', 'city', 'landmark', 'zipcode', 'size']

class BloodDetailForm(forms.ModelForm):
    class Meta:
        model = BloodDetail
        fields = ['blood_type', 'amount_available', 'donation_date']