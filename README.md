# Full Stack API Final Capstone Project - Trivial Freelance Timetracking

## Introduction

I chose to create a time tracking backend for me to keep track of personal projects. I was also curious to build every resource around a specific user.

The Freelance API is organized around **REST**. It has **resource-oriented URLs**, returns **JSON-encoded** responses and uses **standard HTTP** response codes.

## Getting Started

At present, this app is hosted on **Heroku** and can also be run locally.
You can check out the app by visiting the following URL: `http://xxxxxxxxxx`.

Authentication: This app requires authentication to be tested.
Please use the follwing users to try the hosted API:
| Role | user | pw | permissions  
| ---- | :-------------------: | ------------: | ----------------------------------:
| Freelancer | test@tst.com | 1Qay2wsx | has all permissions
| Intern | intern@test.com | Asdf1234 | has restricted permissions (e.g. can't delete projects)

### Prerequisits & Installation

Developers using this project should already have Python3 and pip installed on their local machines.

### Backend

from the backend folder run `pip install requirements.txt` to download the dependencies. All required packages are included in the requirements file.

To run the application locally, run the the following commands:

```
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```

The application is running on `http://localhost:5000/`. All API routes are using the default `http://localhost:5000/api/`.

## Testing

To run the tests, run the following commands from the backend folder:

```
dropdb test_db
createdb test_db
psql test_db < init_db.sql
python -m unittest test.py
```

## Error Handling

Errors are returned as JSON object in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

### Error Codes, Types, Messages

The API will return the following error codes and types in case a request fails:

| Code |      Error Type       |            Message |
| ---- | :-------------------: | -----------------: |
| 200  |          ok           |  works as expected |
| 400  |      bad_request      |        bad request |
| 401  |     unauthorized      |       unauthorized |
| 404  |       not_found       | resource not found |
| 405  |  method_not_allowed   | method not allowed |
| 500  | internal_server_error |       SERVER ERROR |

## Endpoints

### GET /api/projects

General:

- Returns all user specific projects:
  Sample:
  `curl
