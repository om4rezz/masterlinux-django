from django import forms
from .models import Subscription

class EmailForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription