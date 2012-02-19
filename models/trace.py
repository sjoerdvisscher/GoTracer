from google.appengine.ext import db

class Trace(db.Model):  
  imageUrl = db.LinkProperty(required=True)
  corners = db.ListProperty(item_type=int)
  datetime = db.DateTimeProperty()
  match = db.FloatProperty()