from django import forms
from .models import Book  # Import your model or define fields here

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with your model if applicable
        fields = ['title', 'author', 'publication_year']  # Specify fields to include in the form

    # Optional: Add custom validation or widgets if needed
    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        if publication_year and publication_year < 1900:
            raise forms.ValidationError("Publication year must be 1900 or later.")
        return publication_year

    # Optional: Customize form layout with widgets
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter book title'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter author name'}))
    publication_year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter publication year'}))
