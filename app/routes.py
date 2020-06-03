from flask import render_template, request, redirect, url_for
from app import app, db
from app.model import URL
import random
import base62

# db.create_all()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shortUrl", methods=["POST"])
def submitUrl():
        longURL = request.form.get("originalURL")
        
        returned_URL= db.session.query(URL).filter(URL.long_URL==longURL).first()
        #check if long url in db
        if returned_URL == None:
            '''
            rationale:
                -   strings are added to the database in the order that they come from respective clients
                -   the string is first added to the db and then the id is reteirved to make an short url from it using the base62 module
                    it is done this way because:
                    -   we want to make sure that there are no race conditions; each url must be assigned a   
            '''            
            BIG_NUMBER=100000000000000 # to make the urls longer

            URL_object= URL(long_URL=longURL) # add longURL to database
            db.session.add(URL_object) # add to session 
            db.session.commit() # commit to database
    
            short_URL=base62.encode(URL_object.id+BIG_NUMBER) # create short url
            
            URL_object.short_URL=short_URL # update the recently created url object so that it now has a shortUrl
            db.session.commit() # commit to teh url database

            print("new short url", URL_object.short_URL)        
        
        else:
            print("existing short url:", returned_URL.short_URL)
        
        return redirect(url_for('index'))
        
