import json
from Parse import Sublink, WebPage
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse4")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse6")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse8")
#url = Sublink("http://cs467-pavo-tests.appspot.com/parse9")

#url = Sublink("http://cs467-pavo-tests.appspot.com/graph1")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph2")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph3")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph4")
url = Sublink("http://cs467-pavo-tests.appspot.com/graph5")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph6") #uncertain
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph7")
#url = Sublink("http://cs467-pavo-tests.appspot.com/graph8")  #uncertain
newPage = WebPage(url)
urls = newPage.GoSearch(url, 'BFS', 3)
dict = {}
dict['URLs'] = urls
dict['start'] = url.getUrl()
dict['cookie'] = 'temp'
print json.dumps(dict, indent=4, sort_keys=True)


