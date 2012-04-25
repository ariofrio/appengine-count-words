from google.appengine.ext import db

class WordCount(db.Model):
    count = db.IntegerProperty(required=True)
