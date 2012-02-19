#!/usr/bin/env python

from google.appengine.ext.webapp import *
from google.appengine.ext.webapp.util import run_wsgi_app
from urllib import unquote

from google.appengine.ext import db
from google.appengine.api import users

from models.trace import Trace
import datetime

class MakeSGF(RequestHandler):
  def get(self):
    
    url = self.request.get("image")
    
    corners = [ int(coord) for coord in  self.request.get("corners").split(",") ]

    trace = Trace(imageUrl=url, corners = corners, datetime=datetime.datetime.today() , match=float(self.request.get("match")))
    trace.put()
    
    data = unquote(self.request.get("sgf"))
    self.response.headers["content-type"] = "application/x-go-sgf"
    self.response.out.write(data)

# listening to ALL url's that pass by
application = WSGIApplication([ ('/game.sgf', MakeSGF) ],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
