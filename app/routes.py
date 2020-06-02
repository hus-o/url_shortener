from flask import render_template, request
from app import app, db
from app.model import URLs

db.create_all()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        originalURL = request.form.get("originalURL")
        # print("orig url exists",db.session.query(URLs).filter(URLs.url == originalURL).one())
        # input("check print")
        db.session.add(originalURL)
        db.session.commit()
        # server-side
            # add originalUrl to database
            # get primary key and encode to shortURL 
            # add shortURL to field in database
            # return shortURL to client
        
        shortURL = "1"
        return render_template("index.html", originalURL=originalURL, shortURL=shortURL)
        
    return render_template("index.html")

