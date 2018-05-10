'''from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
import webapp2
import json

# Start page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
        newPage = WebPage(url)
        arrayKeyword = {'haveh', 'al88so'}
        returned = newPage.GoSearch(url, 'DFS', 1, arrayKeyword)
        print ('\n\n\n\n')
        for i in returned:
            print(i)
        print ('\n\n\n\n')

app = webapp2.WSGIApplication([('/', MainHandler),
                            ('/index.html', MainHandler)],
                            debug = True)

'''

from Parse import Sublink, WebPage
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")

#url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph6/a")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph8/a")
newPage = WebPage(url)
arrayKeyword = {'hav66e', 'Al7so'}
returned = newPage.GoSearch(url, 'DFS', 2, arrayKeyword)
Title = newPage.title
print (Title)
for i in returned:
    print(i)
