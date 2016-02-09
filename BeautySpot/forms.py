from django import forms


class ReservationForm(forms.Form):
    services = forms.CharField()
    email = forms.EmailField()
    name = forms.CharField()
    date = forms.DateField()
    time = forms.TimeField()
    phone = forms.CharField()
    description = forms.CharField()
