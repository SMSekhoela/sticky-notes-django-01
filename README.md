# Sticky Notes

A simple sticky-notes application built with Django. Create, browse, edit, and
delete notes through a web interface.

## Features

- List notes, with the newest notes shown first.
- View a note's full content.
- Create and edit notes.
- Confirm before deleting a note.
- Store notes in a local SQLite database.

## Requirements

- Python 3.12 or newer
- pip

The required Python packages are listed in [`requirements.txt`](requirements.txt).

## Setup

From the repository root, create and activate a virtual environment.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation scripts, either run the environment's Python
directly as shown below or allow activation for this PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and initialize the database:

```shell
python -m pip install -r requirements.txt
python manage.py migrate
```

## Run the application

Start Django's development server:

```shell
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. The notes list is also available
at <http://127.0.0.1:8000/notes/>.

## Tests and checks

Run the test suite and Django's system checks:

```shell
python manage.py test
python manage.py check
```

## Build the documentation

Install the documentation dependencies:

```shell
python -m pip install -r docs/requirements.txt
```

Build the HTML documentation with Sphinx:

```shell
python -m sphinx -b html docs docs/_build/html
```

On Windows, use backslashes in the output path if needed:

```powershell
python -m sphinx -b html docs docs\_build\html
```

Open `docs/_build/html/index.html` to view the generated documentation.
