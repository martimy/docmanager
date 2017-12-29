from django import forms

class CategoryForm(forms.Form):
    category = forms.CharField(label='Category', max_length=100)


