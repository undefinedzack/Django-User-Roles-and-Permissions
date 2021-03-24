from django import forms
from .models import Userz

class UserForm(forms.ModelForm):

    class Meta:
        model = Userz
        fields = '__all__'