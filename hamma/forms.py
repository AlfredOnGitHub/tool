from django import forms 
   
# creating a form  
class Registro(forms.Form): 
    username = forms.CharField(max_length = 15, min_length=6, required=True)  
    password = forms.CharField(widget = forms.PasswordInput(), required=True) 
    email = forms.EmailField(required=True)