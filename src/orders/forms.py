from django import forms
from django.contrib.auth import get_user_model
from orders.models import UserCheckout

User = get_user_model()

class GuestCheckoutForm(forms.Form):
	email = forms.EmailField()
	email2 = forms.EmailField(label='Verify Email')

	def clean_email2(self):
	    email = self.cleaned_data.get("email")
	    email2 = self.cleaned_data.get("email2")

	    if email == email2:
	        # Query your UserCheckout model. Not the auth one!
	        if UserCheckout.objects.filter(email=email).exists():
	            raise forms.ValidationError("This User already exists. Please login instead.")
	            print('error')
	    else:
	        raise forms.ValidationError("Please confirm emails are the same")
	        print('error')
	    return email2