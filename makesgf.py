#!/usr/bin/env python

from google.appengine.ext.webapp import *
from google.appengine.ext.webapp.util import run_wsgi_app
from urllib import unquote

class MakeSGF(RequestHandler):
  def get(self):
    data = unquote(self.request.query_string)
    self.response.headers["content-type"] = "application/x-go-sgf"
    self.response.out.write(data)

# listening to ALL url's that pass by
application = WSGIApplication([ ('/game.sgf', MakeSGF) ],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
