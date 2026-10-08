from django.db import models


class Note(models.Model):
    """Store a sticky note's text and creation/update timestamps."""

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the note title for readable display in the admin."""
        return self.title
