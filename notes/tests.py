from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteViewsTests(TestCase):
    """Test the user-facing note views.

    :cvar note: A note created as shared test setup.
    :vartype note: Note
    """

    def setUp(self):
        """Create a note used by each view test.

        :returns: None.
        :rtype: None
        """
        self.note = Note.objects.create(
            title='Test note',
            content='This is a test note.',
        )

    def test_note_list_page_loads(self):
        """Ensure the notes list renders and includes the saved note.

        :returns: None.
        :rtype: None
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note')

    def test_note_delete_requires_confirmation(self):
        """Require confirmation before deleting a note.

        :returns: None.
        :rtype: None
        """
        delete_url = reverse('note_delete', args=[self.note.pk])

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_confirm_delete.html')

        response = self.client.post(delete_url)
        self.assertRedirects(response, reverse('note_list'))
        self.assertFalse(
            Note.objects.filter(pk=self.note.pk).exists()
        )
