from bs4 import BeautifulSoup
import requests
from graphviz import Graph
        
def startScrapin(sitename):
    g1 = Graph(comment = 'Scraper Results')
    linklist = findTheLinks(sitename, g1)
    linklist = linklist.split()
    buildBranches(sitename, linklist, g1)
    #for link in linklist:
        #print (link)
        #sublinklist = findTheLinks(link, g1)
        #print (sublinklist)
        #if sublinklist: #check if list is empty
            #buildBranches(link, sublinklist, g1)
    createImage(g1)
    
def clarifyExtension(link, sitename):
    if (link[0] == '/'):
        link = 'http://' + sitename + link
    return link
    
def findTheLinks(sitename, g1):
    linklist = ''
    try:
        page = requests.get("http://" +sitename)
        data = page.text
        soup = BeautifulSoup(data, "lxml")
        for link in soup.find_all('a'):
            link = clarifyExtension(link.get('href'), sitename)
            linklist = linklist + link + (' ')
        return linklist
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
    except requests.exceptions.HTTPError as err:
        requests.status_code = "Invalid URL"
        print (err)
     
    
def buildBranches(sitename, linklist, g1):
    g1.node(sitename)
    for link in linklist:
        g1.node(link)
        g1.edge(sitename, link)
    #print (g1.source)
    
def createImage(g1):
    img = g1.render('scraper-links.gv')
    return img
    
startScrapin("www.google.com") 