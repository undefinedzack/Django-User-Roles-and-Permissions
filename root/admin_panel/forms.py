from django import forms
from .models import Userz

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_no = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    department_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Userz
        fields = '__all__'