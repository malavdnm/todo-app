# WorkIndia-todo app
An API application that can take Notes with title, due date and other details and display all Notes of a user while stroing encrypted data in database

## Requirements:

### User account registration:
Create a user account. These credentials will be used to log into this panel.

[POST] /app/user

Request Data: {
    'username': str,
    'password': str
}

Response Data: {
    'status': 'account created'
}

***Curl command to test account registration***:
```
curl -H 'Content-Type: application/json' -d '{"username": "<username>","password":"<password>"}' -X POST http://127.0.0.1:8000/notesapp/user
```
 

### User account login:
Provide the ability to log into the panel using the user credentials.

[POST] /app/user/auth

Request Data: {
    'username': str,
    'password': str
}

Response Data: {
    'status': 'success',
    'userId': int
}
 
***Curl command to test user login***:
```
curl -H 'Content-Type: application/json' -d '{"username": "<username>","password":"<password>"}' -X POST http://127.0.0.1:8000/notesapp/auth
```

### List Saved Notes:
Provide list of stored notes for the logged-in user

[GET] /app/sites/list/?user={userId}

Request Data: None
Response Data: [List of saved notes]
The list returned should belong to the userId passed with the request


***Curl command to test list the notes***:
```
curl -H 'Content-Type: application/json' -X GET http://127.0.0.1:8000/notesapp/sites/list/<UserId>
```


### Save a new note:
Provide the ability for users to add a new note.

[POST] /app/sites?user={userId}

Request Data: {
    'title': str,
    'category': str,
    'description': str,
    'due_date' : str
}

Response Data: {
    'status': 'success'
}

***Curl command to test save the note***:
```
curl -H 'Content-Type: application/json' -d '{"title":"kill", "description":"Mission kaboom", "category":"war", "due_date":"2020-12-10"}' -X POST http://127.0.0.1:8000/notesapp/sites/<userId>
```
