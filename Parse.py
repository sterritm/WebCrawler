#from the web
import re
import hashlib
import requests
#sitePackages.path.append('/path/to/application/app/folder')
from lxml import html

#from urllib.parse import urljoin
import urlparse
from lxml.html.clean import Cleaner



#The web page object- any page available on the world wide web,
#or used for testing purposes.
class WebPage(object):


    #Creates a new WebPage object from a link
    def __init__(self, sublink):

        #If the link is not valid, say so
        if not isinstance(sublink, Sublink) or not sublink.legal:
            raise Exception("Invalid link. Please provide a valid link")


        #Get the web page
        self.link = sublink
        response = requests.get(sublink.URL)
        self.encoding = response.encoding
        self.Tags = response.text.encode('utf8')

        #removes tags from words in web page
        NoTags = HTMLUtils.HTML_CLEANER.clean_html(self.Tags)

        JustWords = html.fromstring(NoTags).text_content()
        JustWords = re.sub(r'/\s+/g', ' ', JustWords).strip()
        self.Text = JustWords
        self.Code = response.status_code

        #Get the links for the children
        self.child_links = self.FindAllURLs()

    #Find all of the URLs connected to that site
    def FindAllURLs(self):
        returned = html.fromstring(self.Tags)
        WebSite = set([urlparse.urldefrag(url)[0] for url in returned.xpath('//a[@href]/@href')])
        return [Sublink(url, self.link) for url in WebSite]

#Class to represent all sublinks
class Sublink(object):

    def __init__(self, url, parent=None):

        # If the parent is not a valid WebPage, say so
        if parent:
            if not isinstance(parent, Sublink):
                raise Exception("Invalid WebPage Object. ")
            #returns the full URL
            url = urlparse.urljoin(parent.URL, url)

        # Set the sublink's contents
        self.ancestor = parent

        #defragment the URL
        self.URL = urlparse.urldefrag(url)[0]

        #parse the URL
        self.authority = urlparse.urlparse(url).netloc

        #validate the URL
        try:
            result = urlparse.urlparse(url)
            self.legal = all([result.scheme, result.netloc])
        except:
            self.legal = False

        #encode it properly
        encoded = self.URL
        encoded.encode('utf-8')

        # use md5 to return a hash for the given url
        self.id = hashlib.md5(url.encode('utf-8')).hexdigest()
        self.position = 0 if parent is None else parent.position + 1

    #have str return the url, the domain, whether the url was valid, and the level (child, grandchild, etc.)
    def __str__(self):
        return "ancestors:%s . legal:%s . id:%s . url: %s . authority:%s "  \
            %(self.position, self.legal, self.id, self.URL, self.authority)

#Source: https://stackoverflow.com/questions/3073881/clean-up-html-in-python/6482979
#Removes html tags, such that only words are reviewed (such that we can find the keyword)
#All methods are staticmethods, so that no object needs to be built.
class HTMLUtils(object):
    HTML_CLEANER = Cleaner(**{
        'scripts': True,
        'embedded': True,
        'inline_style': True,
        'javascript': True,
        'remove_unknown_tags': True,
        'style': True,
        'comments': True,
        'meta': True
    })
