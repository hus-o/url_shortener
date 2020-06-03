### URL-Shortener
#### Helder & Huseyin

### How to run:
Before running please install pipenv: [https://pypi.org/project/pipenv/]

After repo is cloned, run these commands in the project directory:
```pipenv install```

```flask run```

Note: You may need to set the FLASK_APP as app and FLASK_ENV as development, discussed here [https://flask.palletsprojects.com/en/1.1.x/cli/]

### User Story:
* Enter a URL, click a button, get a shorter URL

### MVP:
* Single input and button.
* Input is taken, stored in database, encoded to shorter (base62) url
* Shortened URL outputted to user on homepage

### Working Notes:

Installed necessary libraries and made an initial structure.

Made sure we can both install and run on separate machines.

Created basic model, which was working. But later on we needed to amend this as the table wasn't being created on running the app. We fixed this with a ```db.create_all()``` in the routes file.

-- HELDER YOUR ROUTES --
Rationale for checking if URL already exists in db:
strings are added to the database in the order that they come from respective clients
the string is first added to the db and then the id is reteirved to make an short url from it using the base62 module
it is done this way because:
we want to make sure that there are no race conditions; each url must be assigned a unique id

We then made a route to grab the shortened URL and search the database for it's respective original form to which the user would be redirected to. This wasn't much of a struggle.
