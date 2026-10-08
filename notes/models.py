from django.db import models


class Note(models.Model):
    """Represent a sticky note and its timestamps.

    :ivar title: The note's title.
    :vartype title: str
    :ivar content: The note's body text.
    :vartype content: str
    :ivar created_at: The date and time when the note was created.
    :vartype created_at: datetime
    :ivar updated_at: The date and time when the note was last updated.
    :vartype updated_at: datetime
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the note title for readable display in the admin.

        :returns: The note's title.
        :rtype: str
        """
        return self.title
