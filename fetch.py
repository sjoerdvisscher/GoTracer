#!/usr/bin/env python

from google.appengine.ext.webapp import *
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api.urlfetch import fetch
import logging

class Fetch(RequestHandler):
  def get(self):
    url = self.request.query_string
    logging.info("fetching: " + url)
    data = fetch(url)
    self.response.headers["content-type"] = data.headers["content-type"]
    self.response.out.write(data.content)

# listening to ALL url's that pass by
application = WSGIApplication([ ('/fetch', Fetch) ],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
