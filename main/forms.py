from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = {'title', 'author', 'cateogory', 'price', 'description', 'condition', 'image'}
