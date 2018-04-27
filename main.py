from google.appengine.ext.webapp import template
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
        keywordList = ['Dinosaurs', 'French Fries']
        url = Sublink("http://cs467-pavo-tests.appspot.com/", keywordList)
        print("Hello ")
        newPage = WebPage(url)
        #returned = newPage.FindAllURLs()
        returned = newPage.GoSearch(url, 'BFS', 1)
        for i in returned:
            print (i)



app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/index.html', MainHandler)],
                              debug=True)
'''
from Parse import Sublink, WebPage
url = Sublink("https://cloudcsproject.appspot.com/welcome")
newPage = WebPage(url)
#returned = newPage.FindAllURLs()
returned = newPage.GoSearch(url, 'BFS', 2)
for i in returned:
    print(i)'''
