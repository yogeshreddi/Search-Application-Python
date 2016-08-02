#Imporitng required libraries, requests for requesting/getting for the html content.
#BeautifulSoup for scraping the content for the html pages we fecthed using tag names.
#Pandas for playing with the data we scraped.

import requests
from bs4 import BeautifulSoup
import pandas
import sys


#Definning Class which will contain our scraping method
class GetDetailsFromYp:

    def ScrapeYp(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content)
        for link in soup.find_all("div",{"class":"info",}):

            #Scraping for the name of the restaurents we search for
            try:
                business_name.append(str(link.contents[0].find_all("a",{"class":"business-name"})[0].text))
            except:
                business_name.append("NA")
                pass

            #Scraping for the full address of the restaurents people search for
            try:
                business_address.append(link.contents[1].find_all("p",{"class":"adr"})[0].text.strip())
            except:
                business_address.append("NA")
                pass

            #Scraping for the street address of the restaurents people search for
            try:
                business_street.append(str(link.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text))
            except:
                business_street.append("NA")
                pass

            #Scraping for the locality of the restaurents people search for
            try:
                business_locality.append(str(link.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text))
            except:
                business_locality.append("NA")
                pass


            #Scraping for the region/State of the restaurents people search for
            try:
                business_region.append(str(link.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text))
            except:
                business_region.append("NA")
                pass

            #Scraping for the zipcode/postalcode of the restaurents people search for
            try:
                business_zipcode.append(str(link.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text))
            except:
                business_zipcode.append("NA")
                pass

            #Scraping for the phone of the restaurents people search for
            try:
                business_phone.append(str(link.contents[1].find_all("div",{"class":"phone"})[0].text).replace('  ','-').replace(' ','-'))
            except:
                business_phone.append("NA")
                pass

            #Scraping for the category of the restro
            try:
                business_catelog.append(str(link.contents[2].find_all("div",{"class":"categories"})[0].text+"\n"))
            except:
                business_catelog.append("NA")
                pass

            #in the exception block we are appening "NA" to the list, for None type found during the scraping

    #Constructor for our class
    def __init__(self,url):
        self.url = url
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content)


##what = "Shawarma"
##where = "New York, NY"

#Asking what people would like to search Yellow pages for

arguments = " ".join(sys.argv[1:]) 
arguments = arguments.split()

what = arguments[0]
where = arguments[1]


#Initializing all our variables with emtpty list/arrays
business_name = []
business_address = []
business_street = []
business_locality = []
business_region = []
business_zipcode = []
business_phone = []
business_catelog = []


#Fetching how many pages available revelant to the customer search
#Have to add a block of code to get the no of pages avilable relevant to the search  
n=5

#for loop for forming the url for all the relevant pages available
for i in range(1,n+1):
    url = "http://www.yellowpages.com/search?search_terms="+what+"&geo_location_terms="+where
    if i>1:
        url = url+"&page="+str(i)
    #Creating our class object, which will evoke the constructor 
    MyObject = GetDetailsFromYp(url)
    #Calling the class method to scrape the required data from YellowPages
    MyObject.ScrapeYp()


#Forming a data frame from the scraped data and saving it into a csv file
YellowPagesData = pandas.DataFrame({'RestroName':business_name,'FullAddress':business_address,'Street':business_street,'Locality':business_locality,'Region':business_region,'Zipcode':business_zipcode,'Phone':business_phone,'Categories':business_catelog})
YellowPagesData = YellowPagesData[['RestroName','FullAddress','Street','Locality','Region','Zipcode','Phone','Categories']]
YellowPagesData.to_csv("YellowPagesData.csv")