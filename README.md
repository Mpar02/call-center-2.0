# Call Center Dashboard

## About the Project

This project is a Python-based backend application for managing phone calls.

It uses FastAPI to expose REST API endpoints for retrieving and archiving calls. Call information and related notes are stored in memory.

## Features

- Get all non-archived calls.
- Get a specific call by ID, including its notes.
- Archive a call by ID.
- Store notes related to calls.
- Use separate models for calls and notes.
- Access call management features through REST API endpoints.
- Handle missing calls with HTTP 404 responses.
- Return HTTP 404 for non-existent or non-numeric call IDs.

## Project Structure

```text
call-center-2.0/
├── models/
│   ├── call.py
│   └── note.py
├── routes/
│   ├── __init__.py
│   └── calls.py
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
- FastAPI
- Uvicorn
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

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/calls` | Retrieve all non-archived calls |
| GET | `/calls/{call_id}` | Retrieve a call by ID, including notes |
| PATCH | `/calls/{call_id}/archive` | Archive a call by ID |


## Error Handling

- **404 Not Found:** Returned when a call ID does not exist or is non-numeric.
- **404 Not Found:** Returned when an API route does not exist.
- **405 Method Not Allowed:** Returned when an unsupported HTTP method is used.

Error responses use a consistent JSON structure with an `error` field.

Example:

```json
{
  "error": "Call not found"
}
```


## Data Storage and Known Limitations

The project currently uses in-memory data rather than a database.

Changes are not permanently saved. When the server restarts, the initial seed data is loaded again.

Authentication and persistent database storage are not implemented in this version.