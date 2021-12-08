from django import forms

class FormularioContacto(forms.Form):
    name=forms.CharField(label="name",required=True,)
    email=forms.CharField(label="email",required=True)
    message=forms.CharField(widget=forms.Textarea,label="message",required=True)
    
    
