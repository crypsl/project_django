from django import forms
from .models import Publication, Book

# class BookForm(forms.Form):
#     name = forms.CharField()
#     publication = forms.ModelChoiceField(queryset=Publication.objects.all())

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'contact', 'address', )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('created', 'modified', )
