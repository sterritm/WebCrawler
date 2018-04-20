'''from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import webapp2
import json
import os
import urllib
import random
import string


from Parse import Sublink, WebPage

# Start page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = Sublink("https://stackoverflow.com/questions/15081542/python-creating-objects")
        print("Hello ")
        newPage = WebPage(url)
        returned = newPage.CollectSublinks()
        for i in returned:
            print(i)


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/index.html', MainHandler)],
                              debug=True)
'''
from Parse import Sublink, WebPage
url = Sublink("https://stackoverflow.com/questions/15081542/python-creating-objects")
newPage = WebPage(url)
returned = newPage.FindAllURLs()
for i in returned:
    print(i)