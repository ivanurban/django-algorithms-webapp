from django import forms

class SendMailForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)