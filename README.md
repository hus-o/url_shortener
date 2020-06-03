### URL-Shortener
#### Helder & Huseyin

### How to run:
Before running please install pipenv: [https://pypi.org/project/pipenv/]

After repo is cloned, run these commands in the project directory:

```pipenv install```

```pipenv shell```

```flask run```

Note: You may need to set the FLASK_APP as app and FLASK_ENV as development BEFORE running "flask run", discussed here [https://flask.palletsprojects.com/en/1.1.x/cli/]

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

# Rationale for checking if URL already exists in db:
  - original url strings are added to the database in the order that they come from respective clients (ie users)
  - the orignal url string is first added to the db and then the id (autoincremented by databse) is retrivied. 
  - this is is encode to base62 to make an short url
  - by making sure we commit to the database first and then get the id (i.e. the number used for encoding) from the database, we can be sure    that any 2 unique original urls will not have the same umberic id for encoding of short url

We then made a route to grab the shortened URL and search the database for it's respective original form to which the user would be redirected to. This wasn't much of a struggle.
