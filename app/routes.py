from flask import render_template, request, redirect, url_for
from app import app, db
from app.model import URL
import random
import base62

db.create_all()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shortUrl", methods=["POST"])
def submitUrl():
        longURL = request.form.get("originalURL")
        
        returned_URL= db.session.query(URL).filter(URL.long_URL==longURL).first()
        #check if long url in db
        if returned_URL == None:
                 
            # BIG_NUMBER=100000000000000 # to make the urls longer

            URL_object= URL(long_URL=longURL) # add longURL to database
            db.session.add(URL_object) # add to session 
            db.session.commit() # commit to database
    
            short_URL=base62.encode(URL_object.id) # create short url
            
            URL_object.short_URL=short_URL # update the recently created url object so that it now has a shortUrl
            db.session.commit() # commit to teh url database
        
            short_URL= URL_object.short_URL

        else:
            short_URL=returned_URL.short_URL


        return render_template("index.html", shortURL = f"http://localhost:5000/{short_URL}", originalURL = longURL)

@app.route("/<short_URL_client>", methods=["GET"])
def shortAPI(short_URL_client):
    og_URL = db.session.query(URL).filter(URL.short_URL==short_URL_client).first()

    if og_URL is None:

        return render_template("error.html")
    
    else:
        return redirect(f"https://{og_URL.long_URL}")



        
