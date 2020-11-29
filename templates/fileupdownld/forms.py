from django import forms

class FileUpLdForm(forms.Form):
    upfile = forms.FileField()