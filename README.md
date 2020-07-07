# Full Stack API Final Capstone Project - Trivial Freelance Timetracking

## Introduction

I chose to create a time tracking backend for me to keep track of personal projects. I was also curious to build every resource around a specific user.

The Freelance API is organized around **REST**. It has **resource-oriented URLs**, returns **JSON-encoded** responses and uses **standard HTTP** response codes.

## Getting Started

At present, this app is hosted on **Heroku** and can also be run locally.
You can check out the app by visiting the following URL: `https://heroku-udacity-capstone-test.herokuapp.com/`.

Authentication: This app requires authentication to be tested.
Please use the follwing users to try the hosted API:
| Role | user | pw | permissions  
| ---- | :-------------------: | ------------: | ----------------------------------:
| Freelancer | test@tst.com | 1Qay2wsx | has all permissions
| Intern | intern@test.com | Asdf1234 | has restricted permissions (e.g. can't delete projects)

### Prerequisits & Installation

Developers using this project should already have Python3 and pip installed on their local machines.

## Key Dependencies

**Flask** is a lightweight backend microservices framework. Flask is required to handle requests and responses.

**SQLAlchemy** and **Flask-SQLAlchemy** are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in ./src/database/models.py. We recommend skimming this code first so you know how to interface with the Drink model.

**jose** JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Database Setup

Create a new database in Postgress:

```
createdb casting_agency
```

With Postgres running, restore the database

```
psql Capstone < initial_db.sql
```

### Backend

from the backend folder run `pip install requirements.txt` to download the dependencies. All required packages are included in the requirements file.

From within the backend directory first ensure you are working using your created virtual environment.

To run the application locally, run the the following command from the root folder of this project:

```
source setup.sh
```

Local, the application is running on `http://localhost:5000/`. All API routes are using the default `http://localhost:5000/api/`.

## Testing

To run the tests locally, run the following commands from the backend folder:

```
dropdb test_db
createdb test_db
psql test_db < init_db.sql
python -m unittest test.py
```

## Live Server

Live server can be found in

```
Base URL https://heroku-udacity-capstone-test.herokuapp.com/
```

## Permissions

| Permissions     |             Details              |
| --------------- | :------------------------------: |
| get:profile     | Gets access to the users profile |
| get:projects    |  Get access to a users projects  |
| post:projects   |   Add a new project to the db    |
| delete:project  |      Delete a users project      |
| get:project     |  Get access to a users project   |
| get:workspaces  | Get access to a users workspaces |
| post:workspaces |  Add a new workspace to the db   |
| get:workspace   | Get access to a users workspace  |
| post:workitems  |   Add a new workitem to the db   |
| get:workitems   | Get access to a users workitems  |
| get:workitem    |  Get access to a users workitem  |
| patch:workitems |     Update a users workitem      |

## Roles

| Role       |                                                                                    Permissions                                                                                     |
| ---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Freelancer | get:profile, get:projects, post:projects, delete:project, get:project, get:workspaces, post:workspaces, get:workspace, get:workitems, post:workitems, patch:workitem, get:workitem |
| Intern     |                                      get:projects, get:project, get:workspaces, get:workspace, get:workitems, post:workitems, patch:workitem                                       |

## Test Tokens

The following tokens are also included in the .env file of this project for testing purposes.

### Freelancer

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWUzNDRlMDFmYjhjMzAwMTQ3MTQxM2MiLCJhdWQiOlsiZnJlZXRpbWUiLCJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTQxMTA1OTksImV4cCI6MTU5NDE5Njk5OSwiYXpwIjoidk96YW9uanJmZmdQZGE3dUhOUTRxR3FySDRJdkV2aFUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6d29ya2l0ZW0iLCJnZXQ6cHJvZmlsZSIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3RzIiwiZ2V0OndvcmtpdGVtIiwiZ2V0OndvcmtpdGVtcyIsImdldDp3b3Jrc3BhY2UiLCJnZXQ6d29ya3NwYWNlcyIsIm9wZW5pZDplbWFpbCIsInBhdGNoOnByb2plY3QiLCJwYXRjaDp3b3JraXRlbSIsInBvc3Q6cHJvamVjdHMiLCJwb3N0OndvcmtpdGVtcyIsInBvc3Q6d29ya3NwYWNlcyJdfQ.eIwXoMiLaAteqY3_0JBM3gwll0NE0L9V8YMGVfCk5AdkOviQ1ilKrU9jqEe0dwD9kloEWEm20one3o6SkDNwnzHRTgqVq72wHF6gC4dJrRIVcAm2Cyyi3qOStwP3fYk9NxPpP95u2gHBG55G-jkRLbnC4ZCUeWV_vuvp7mzKC57PDKu9okp4Cfw40lsz9Qm5mH-8QPu0LSUKkXbUr8IFqVlt7Le7Uc9DN9FWncV4osKYTgdPIa8SiQozLSS2lx5AhVADYlNJOma6SRx-Q5424qfDWSo1DeeU0Uv8eH9y8pGWOP1g6oRF6p-4Wg3tPtEDjtM8eIz-FzTjUsAPHFG8Ag
```

### Intern

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWZlZGNhY2E5Y2VkOTAwMTljYWVmMTgiLCJhdWQiOlsiZnJlZXRpbWUiLCJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTQxMTA3MTIsImV4cCI6MTU5NDE5NzExMiwiYXpwIjoidk96YW9uanJmZmdQZGE3dUhOUTRxR3FySDRJdkV2aFUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OnByb2plY3QiLCJnZXQ6cHJvamVjdHMiLCJnZXQ6d29ya2l0ZW0iLCJnZXQ6d29ya2l0ZW1zIiwiZ2V0OndvcmtzcGFjZSIsImdldDp3b3Jrc3BhY2VzIiwicGF0Y2g6d29ya2l0ZW0iLCJwb3N0OndvcmtpdGVtcyJdfQ.COoTa0pgkTo-GsaNQ8zCyhLdgRcymzCRGNiosTmENyS5ocXlN-ZzQ2I_-xErR1pXErAqKDRQiMAAZrkPNsgqLc0KsGfM9dEWqyjIVxhsKjtju2kzGYWzVriv7sVaTXOwlfjQDHGdsYWBbm_v7Rq9RlZIRMM9KNOC4grlYgz_py3ygRhqmPB2di82T_SuqqY62c-ifbL92OV__-MEFk9rKS13TGDPf34eOzJ0y8h8Vs9HO_15FoJqkYEJ06LH5SKSwZzG9vEid50ZuKif4oWmXeen7lL_B1PSlljitvMZBITrsojsVrfufHckytvrOwH6nZr5aRmZ7cQz0D8nQ3LWXA
```

## Intern without openId scope

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWZlZGNhY2E5Y2VkOTAwMTljYWVmMTgiLCJhdWQiOiJmcmVldGltZSIsImlhdCI6MTU5NDExMDgwMCwiZXhwIjoxNTk0MTk3MjAwLCJhenAiOiJ2T3phb25qcmZmZ1BkYTd1SE5RNHFHcXJINEl2RXZoVSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnByb2plY3QiLCJnZXQ6cHJvamVjdHMiLCJnZXQ6d29ya2l0ZW0iLCJnZXQ6d29ya2l0ZW1zIiwiZ2V0OndvcmtzcGFjZSIsImdldDp3b3Jrc3BhY2VzIiwicGF0Y2g6d29ya2l0ZW0iLCJwb3N0OndvcmtpdGVtcyJdfQ.CUd9CHmM6tGtXOLIYPaK_F7FxKCh1C7seMCL1J1D2mTyc7O2mGF1vSLuKWlFwbsXT9zn_i4HHEA0Z9eMxAzDo-8Qs5L6hR5E2agRY-4h44Hke3-2Rwfd5z3BB3qCXHGU5JGBK5l0gEdQSay8YmMqouflmvECS9TLI5V1IjjJaigXc9PaFezyGyP0pLjqPCghbOy6MriRl824eKxhtbUljT2GZRlTJ9PDC9N0lg-4YAa-cE88_kPwXVDrIBFDXd4PIGdlVZI1MNW547SsfGMB0lDJXZ5i4nu2MJnfDGnwMwe7TUMIhEGY70PDSOPW5mf4ollG8dt_vcZBOD4y_UoHcw
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

### GET /

General:

- Test route and intro to the capstone API:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/`

```
My Capstone Project
```

### GET /api/projects

General:

- Returns all user specific projects:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects -H 'Authorization: Bearer auth_token`

```
{
    "success": true,
    "projects": [
        {
            "name": "Client #1",
            "description": "heroku test",
            "start_date": "\"2020-07-05 00:00:00\"",
            "end_date": "\"2020-07-19 00:00:00\"",
            "user_id": "5ee344e01fb8c3001471413c"
        },
        {
            "name": "Client #2",
            "description": "heroku test",
            "start_date": "\"2020-07-05 00:00:00\"",
            "end_date": "\"2020-07-19 00:00:00\"",
            "user_id": "5ee344e01fb8c3001471413c"
        },
        {
            "name": "Client #3",
            "description": "heroku test",
            "start_date": "\"2020-07-05 00:00:00\"",
            "end_date": "\"2020-07-19 00:00:00\"",
            "user_id": "5ee344e01fb8c3001471413c"
        }
    ]
}
```

### POST /api/projects

General:

- Add user specific project:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects -H "Content-Type: application/json " -H "Authorization: Bearer auth_token" -X POST -d '{"name": "Client #4","description": "marketing and biz work"}'`

```
{
    "success": true,
    "projects": [
        {
            "name": "Client #4",
            "description": "marketing and biz work",
            "start_date": "\"2020-07-05 00:00:00\"",
            "end_date": "\"2020-07-19 00:00:00\"",
            "user_id": "5ee344e01fb8c3001471413c"
        },
    ]
}
```

### GET /api/projects/<int:project_id>

General:

- Returns one user specific project:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/6 -H 'Authorization: Bearer auth_token'`

```
{
    "project": {
        "description": "marketing and biz work",
        "end_date": "Sun, 19 Jul 2020 00:00:00 GMT",
        "id": 6,
        "name": "Client #4",
        "start_date": "Sun, 05 Jul 2020 00:00:00 GMT",
        "user_id": "5ee344e01fb8c3001471413c"
    },
    "success": true,
    "workspaces": []
}
```

### DELTE /api/projects/<int:project_id>

General:

- Deletes one user specific project:
  Sample:
  `curl -X DELETE https://heroku-udacity-capstone-test.herokuapp.com/api/projects/6 -H 'Authorization: Bearer auth_token'`

```
{
     "projects": [],
    "success": true,
}
```

### GET /api/projects/<int:project_id>/workspaces

General:

- Returns all user and project specific workspaces:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces -H 'Authorization: Bearer auth_token`

```
{
    "success": true,
    "workspaces": [
        {
            "description": "Social Media Stuff",
            "name": "Social Media",
            "price": 100.0,
            "project_id": 8
        },
        {
            "description": "SEO Stuff",
            "name": "SEO Work",
            "price": 120.0,
            "project_id": 8
        },
        {
            "description": "SEA Stuff",
            "name": "SEA Work",
            "price": 110.0,
            "project_id": 8
        }
    ]
}
```

### POST /api/projects/<int:project_id>/workspaces

General:

- Add user and project specific workspace:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces -H "Content-Type: application/json " -H "Authorization: Bearer auth_token" -X POST -d '{"name": "Instagram Work", "description": "Insta Stuff", "price": 20}'`

```
{
    "success": true,
    "workspaces": [
        {
            "description": "SEA Stuff",
            "name": "SEA Work",
            "price": 90.0,
            "project_id": 9
        },
        {
            "description": "Insta Stuff",
            "name": "Instagram Work",
            "price": 20.0,
            "project_id": 9
        }
    ]
}
```

### GET /api/projects/<int:project_id>/workspaces/<int:workspace_id>

General:

- Returns one user and project specific workspace:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces/4 -H 'Authorization: Bearer auth_token'`

```
{
    "success": true,
    "workspace": {
        "id": 4,
        "name": "SEO Work",
        "description": "SEO Stuff",
        "price": 120.0,
        "project_id": 8
    },
    "workitems": [
        {
            "id": 2,
            "name": "task #1",
            "description": "heroku initial design",
            "duration": 9.0
        }
    ]
}
```

### GET /api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems

General:

- Returns all user, project and workspace specific workitems:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces/4/workitems -H 'Authorization: Bearer auth_token`

```
{
    "success": true,
    "workitems": [
        {
            "name": "task #1",
            "description": "heroku initial design",
            "duration": 9.0,
            "workspace_id": 4
        }
    ]
}
```

### POST /api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems

General:

- Add a user, project and workspace specific workitem:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces/4/workitems -H "Content-Type: application/json " -H "Authorization: Bearer auth_token" -X POST -d '{"name": "task #2", "description": "Create new post", "duration": 1}'`

```
{
    "success": true,
    "workitems": [
        {
            "name": "task #1",
            "description": "heroku initial design",
            "duration": 9.0,
            "workspace_id": 4
        },
        {
            "name": "task #2",
            "description": "Create new post",
            "duration": 1.0,
            "workspace_id": 4
        }
    ]
}
```

### GET /api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems/<int:workitem_id>

General:

- Returns a user, project and workspace specific workitem:
  Sample:
  `curl https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces/4/workitems/3 -H 'Authorization: Bearer auth_token'`

```
{
    "success": true,
    "workitem": {
        "id": 3,
        "name": "task #2",
        "description": "Create new post",
        "duration": 1.0,
        "workspace_id": 4
    }
}
```

### PATCH /api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems/<int:workitem_id>

General:

- Updates a user, project and workspace specific workitem:
  Sample:
  `curl -X PATCH https://heroku-udacity-capstone-test.herokuapp.com/api/projects/8/workspaces/4/workitems/3 -H 'Authorization: Bearer auth_token' -d '{"name": "Write capstone docs", "description": "Create the docs for the Udacity capstone project", "duration": 2}'`

```
{
    "success": true,
    "workitem": {
        "id": 3,
        "name": "Write capstone docs",
        "description": "Create the docs for the Udacity capstone project",
        "duration": 2.0,
        "workspace_id": 4
    }
}
```

## Author

Mike Schertl (Student)

## Acknowledgements

The awesome team at Udacity!
