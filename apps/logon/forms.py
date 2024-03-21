from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
   remember_me = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput)
   
   def __init__(self, *args, **kwargs):
      super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
      #Add style class on form fields
      self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
      self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
      self.fields['remember_me'].widget.attrs['class'] = 'form-check-input'