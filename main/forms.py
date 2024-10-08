from django import forms
from .models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'author', 'description', 'stock_quantity', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)
    
    def clean_author(self):
        author = self.cleaned_data['author']
        return strip_tags(author)
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)