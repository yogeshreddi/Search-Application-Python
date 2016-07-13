# Search-Application-Python

###1. What is your program? Give a brief description of what your program is going to do. 
-We are trying to build an application which will scrape restaurants information from webpages and plot them on a geomap.

###2. How is it going to work? Describe how you expect the program to perform its operations. 
-We will provide user a UI wherein he will be asked where and what he is searching for. For example user might want to look for a good pancakes at some xyz place, so he will search for the same on our application (xyz can be zipcode or city name or location name). Once he enters his search we will scrape the infomration from webpages using BS4(BeautifulSoup) based on search attributes, later will save the extracted data as a dataframe to csv using Pandas, subsequently will plot the top 10 results on a geomap using matplotlib.

###3. What modules are you going to use? Describe how these modules will fit into the program. 

tkinter - for creating the user interface.
BeautifulSoup - to extract information from html pages.
Pandas - saving data to csv and playing around with the dataframe.
Matplotlib - plotting the data in geomap using the available zipcode.

###4. Describe any problems you may experience and how you plan on handling it. It is good to think about what might happen so you are prepared to handle it.  

One issue that could occur while extracting/scraping the information from the html pages is that, data for all the restaurants may not be consistent. For example a few restaurants might not have the attributes we are looking for, in that case the data we save could be insufficient. To overcome this problem we will use a try/except block to avoid those particular restaurants.
