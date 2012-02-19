#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, logging
from models.trace import Trace

class MainPage(webapp.RequestHandler):
  def getTrace(self, image):
    trace = None
    query = Trace.all().filter("imageUrl = ", image).order("-match")
    for result in query.fetch(1):
      trace = result
      break    
      
    if trace:
      corners = ",".join( [ str(c) for c in trace.corners] ) 
      match = str(trace.match)
      logging.info("found trace: " + str(trace.imageUrl) + ", date:" + str(trace.datetime) + ", corners: " + corners + ", match: " + match  )
    else:
      logging.info("no trace for " + str(image))
    
    return trace
  
  def get(self):
    trace = None
    image = self.request.get("image")
    if image:
      try:
        trace = self.getTrace(image)
      except Exception, e:
        logging.error(e)
        trace = None
    
    # log ip & browser
    logging.info(self.request.remote_addr + ": " + self.request.headers["user-agent"])
    
    path = os.path.join(os.path.dirname(__file__), 'templates/gotracer.html')
    
    if trace:
      self.response.out.write(template.render(path, { "image": image, "corners": ",".join( [ str(c) for c in trace.corners] ), "match": str(trace.match) }))
    else:
      self.response.out.write(template.render(path, { "image": image }))


application = webapp.WSGIApplication([ ('/', MainPage)],debug=True)


def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
