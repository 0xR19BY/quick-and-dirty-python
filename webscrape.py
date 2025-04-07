# This is from when I started learning python. Adding it to the repo as its utility is scalable for future projects.
from bs4 import BeautifulSoup
import requests

#Dictionary containing URLs to scrape.
urls = {
    "google" : "https://www.google.com" #this is an example.
}

url_prefixes = {
    "google" : "https://www.google.com"
}

#Creating a class with methods for scraping sites.
class scraping:
    def __init__(self, url, urlprefix):
        self.url = url
        self.urlprefix = urlprefix

    #method to retrieve links from a webpage
    def linkscraping(self):
        scrape = requests.get(self.url)
        soup = BeautifulSoup(scrape.text, "html.parser")

        #Creates a list of links that exist on the webpage
        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        #It has come to my attention that sometimes our links list can have none types. We need to filter this out.
        sanitised_links = []
        for elem in links:
            if elem != None and 'crn' not in elem: #Did the and strictly because of some other site. This will probably change for the sake of convention.
                sanitised_links.append(elem)

        #This section searches for keywords within a link and if it exists, it adds it to a list. EDIT: When I wrote this it was for a discord bot to bring news of cyber incidents.
        conditional_links = []
        for elem in sanitised_links:
            if 'data-breach' in elem or 'databreach' in elem or 'dataleak' in elem or 'data-leak' in elem:
                conditional_links.append(elem)
            else:
                pass
        
        return conditional_links
        
    def appendlinks(self, linkset):
        prepended_links = []
        for elem in linkset:
            x = self.urlprefix + elem
            prepended_links.append(x)

        return prepended_links

    def log_links(self, unsanitised_links):
        with open('log.txt', 'r+') as logs:
            linklist_raw = logs.readlines()
            linklist = []
            for elem in linklist_raw:
                linklist.append(elem.strip())
            conditional_links = list(set(unsanitised_links) - set(linklist))
            for elem in conditional_links:
                logs.write(elem)
                logs.write('\n')

        return conditional_links

    def scrape_procedure(self):
        raw_scrape = self.linkscraping()
        prepend = self.appendlinks(raw_scrape)
        filter_links = self.log_links(prepend)
    
        return filter_links
    

'''
Example Usage
def google_scrape():
    google = scraping(urls['google'], url_prefixes['google'])
    return google.scrape_procedure()'
'''
