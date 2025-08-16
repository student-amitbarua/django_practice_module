from django import  forms
from django.forms.widgets import NumberInput


Birth_year_choices = ['1980', '1981', '1981']

class ContactForm(forms.Form):

    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    ok = forms.BooleanField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type' : 'date'}))
    birth_year = forms.DateField(widget= forms.SelectDateWidget(years=Birth_year_choices))