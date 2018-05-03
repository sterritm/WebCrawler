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
        keywordList = ['Dinosaurs', 'French Fries']
        url = Sublink("http://cs467-pavo-tests.appspot.com/parse5", keywordList)
        print("Hello ")
        newPage = WebPage(url)
        #returned = newPage.FindAllURLs()
        returned = newPage.GoSearch(url, 'BFS', 3)
        for i in returned:
            print (i)



app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/index.html', MainHandler)],
                              debug=True)
'''
from Parse import Sublink, WebPage
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")

#url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph6")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph8")  #uncertain
newPage = WebPage(url)
returned = newPage.GoSearch(url, 'BFS', 3)
for i in returned:
    print(i)
