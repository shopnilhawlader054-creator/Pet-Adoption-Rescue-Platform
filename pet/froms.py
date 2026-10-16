from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from core.models import Adoptions

class Registationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']
    def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError('Email alrady registed')
            return email

class Adoptionform(forms.ModelForm):
     class Meta:
          model = Adoptions
          fields = ['phone','adders','reson','previous_pet_experience']