#jrkong's command line searcher
<<<<<<< HEAD

from urllib.parse import quote
import urllib
=======
>>>>>>> test-framework
import argparse
from search import Search

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", action="append", help="Takes a query to search for and searches it.", nargs="*", required=True)
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")

args = argparser.parse_args()

<<<<<<< HEAD
class Search:
    def __init__(self, searchIn = None, engineIn = "google", domainIn = "ca"):
        self.searchRaw = searchIn
        self.searchQuery = ""
        self.engine = engineIn
        self.domain = domainIn
        self.url = ""
        self.searchString = "/search?q="
    #end of constructor

    #set search engine
    def setEngine(self, engineIn):
        self.engine = engineIn
    #end of setEngine

    #set domain engine
    def setDomain(self, domainIn):
        self.domain = domainIn
    #end of setdomain
    
    #set search Query
    def setQuery(self, searchIn):
        self.searchRaw = searchIn
    #end of setQuery

    def buildLink(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + quote(self.searchQuery.encode('utf8'))
    #end of link building

    def openBrowser(self):
        webbrowser.open_new_tab(self.url)
    #end of openBrowser()
#end of Query

=======
>>>>>>> test-framework
searchObj = Search()

searchObj.handleArgs(args)
