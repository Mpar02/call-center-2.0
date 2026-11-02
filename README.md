# Call Center Dashboard

## About the Project

This project is a Python-based backend data layer for managing phone calls.

It stores call information and related notes using in-memory data. No server or API is required.

## Features

- Get all non-archived calls.
- Get a specific call by ID, including its notes.
- Archive a call by ID.
- Store notes related to calls.
- Use separate models for calls and notes.

## Project Structure

```text
call-center-2.0/
├── models/
│   ├── call.py
│   └── note.py
├── seed/
│   └── data.py
├── services/
│   ├── def_get_all_not_archived_calls.py
│   ├── def_get_callinfo_by_id.py
│   └── def_archive_call.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies

- Python
- Git
- GitHub

## Installation

1. Clone the repository.
2. Open the project folder.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

## Data Storage

The project uses in-memory data. This means that changes are not permanently saved and the initial seed data is loaded again when the program starts.