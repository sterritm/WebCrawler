## Name: Michael Sterritt

import webapp2
import urllib
import urllib2
import json
from webapp2 import redirect
import os
from google.appengine.ext.webapp import template
from Parse import Sublink, Webpage


        
# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write("hello world!")

    def post(self):
        
        data = json.loads(self.request.body)
        ## Tia's code here    
        url = Sublink(data['page'])
        newPage = WebPage(url)
        returned = newPage.GoSearch(url, data['method'], data['limit'])
        self.response.write(json.dumps(data))

# [END main_page]


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
