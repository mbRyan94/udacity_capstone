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

### Freelancer

```

```

### Intern

```

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
