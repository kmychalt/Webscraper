from bs4 import BeautifulSoup
import requests
from graphviz import Digraph
        
def startScrapin(sitename):
    g1 = Digraph(comment = 'Scraper Results')
    linklist = findTheLinks(sitename, g1)
    linklist = linklist.split()
    #print (linklist)
    buildBranches(sitename, linklist, g1)
    clarifyExtensions(linklist, sitename)
    print (linklist)
    for link in linklist:
        sublinklist = findTheLinks(link, g1)
        
        #if sublinklist: #check if list is empty
            #buildBranches(link, sublinklist, g1)
    #createImage(g1)
    
def clarifyExtensions(linklist, sitename):
    for link in linklist:
        if (link[0] == '/'):
            link = sitename + link   
    
def findTheLinks(sitename, g1):
    linklist = ''
    try:
        page = requests.get("http://" +sitename)
        data = page.text
        soup = BeautifulSoup(data, "lxml")
        for link in soup.find_all('a'):
            linklist = linklist + link.get('href') + (' ')
        return linklist
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
    except requests.exceptions.HTTPError as err:
        requests.status_code = "Invalid URL"
        print (err)
     
    
def buildBranches(branch, linklist, g1):
    #print ('Branch')
    #print (branch)
    #print ('Linklist')
    #print (linklist)
    g1.node(branch)
    for link in linklist:
        g1.node(link)
        g1.edge(branch, link)
    #print (g1.source)
    
def createImage(g1):
    img = g1.render('scraper-links.gv')
    return img
    
startScrapin("www.google.com") 