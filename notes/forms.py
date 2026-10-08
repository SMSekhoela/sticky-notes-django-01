from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Provide validated form fields for creating and editing notes."""

    class Meta:
        """Configure the model and fields used by the note form."""

        model = Note
        fields = ['title', 'content']
