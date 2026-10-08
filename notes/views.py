from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Render notes ordered from newest to oldest.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: The rendered notes list.
    :rtype: HttpResponse
    """
    ordered_notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': ordered_notes})


def note_detail(request, pk):
    """Render the full content of one note.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param pk: Primary key of the note to display.
    :type pk: int
    :returns: The rendered note detail page.
    :rtype: HttpResponse
    :raises Http404: If no note exists with the given primary key.
    """
    selected_note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': selected_note})


def note_create(request):
    """Create a note from submitted form data.

    A valid POST request saves the note and redirects to the notes list.
    Otherwise, render the form, including any validation errors.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: The rendered form or a redirect to the notes list.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('note_list')
    else:
        note_form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': note_form})


def note_update(request, pk):
    """Update a note from submitted form data.

    A valid POST request saves the changes and redirects to the notes list.
    Otherwise, render the form, including any validation errors.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param pk: Primary key of the note to update.
    :type pk: int
    :returns: The rendered form or a redirect to the notes list.
    :rtype: HttpResponse
    :raises Http404: If no note exists with the given primary key.
    """
    existing_note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=existing_note)
        if note_form.is_valid():
            note_form.save()
            return redirect('note_list')
    else:
        note_form = NoteForm(instance=existing_note)
    return render(request, 'notes/note_form.html', {'form': note_form})


def note_delete(request, pk):
    """Show a confirmation page or delete a note after confirmation.

    A POST request deletes the note and redirects to the notes list. Other
    requests render the confirmation page.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param pk: Primary key of the note to delete.
    :type pk: int
    :returns: The confirmation page or a redirect to the notes list.
    :rtype: HttpResponse
    :raises Http404: If no note exists with the given primary key.
    """
    note_to_delete = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('note_list')
    return render(
        request,
        'notes/note_confirm_delete.html',
        {'note': note_to_delete},
    )
