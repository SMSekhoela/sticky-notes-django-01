from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Display all notes in reverse chronological order."""
    ordered_notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': ordered_notes})


def note_detail(request, pk):
    """Display the full content of a single note."""
    selected_note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': selected_note})


def note_create(request):
    """Create a new note using the note form."""
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('note_list')
    else:
        note_form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': note_form})


def note_update(request, pk):
    """Update an existing note with the submitted form data."""
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
    """Delete a note after the user confirms the action."""
    note_to_delete = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('note_list')
    return render(
        request,
        'notes/note_confirm_delete.html',
        {'note': note_to_delete},
    )
