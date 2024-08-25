from django import forms
from .models import Book  # Import your model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # Fields to include in the form

    # Optional: Add custom validation or widgets if needed
    def clean_publication_year(self):
        publication_year = self.cleaned_data.get('publication_year')
        if publication_year and publication_year < 1900:
            raise forms.ValidationError("Publication year must be 1900 or later.")
        return publication_year
