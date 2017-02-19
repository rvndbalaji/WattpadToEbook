#Pytho script to web-scrape Wattpad Books and prepare a HTML file of the book
#The HTML file itself is the entire eBook
#It can later be converted to EPUB or MOBI formats using eBook Generators such as KindleGen


#AUTHOR : Aravind Balaji
#CREATED : 19th Feb 2017 4:00pm IST
#Libraries/Imports used :
    #1. Urllib
    #2. Requests
    #3. BeautifulSoup
    #4. Codecs
#INPUT : 9-Digit Number in the URL of any chapter of a Wattpad Book
#OUTPUT: A HTML file containing the entire eBook with all chapters.
        #This can later be converted to any eBook using third-party tools
        #such as KindleGen or Calibre

from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import codecs

#ID is the 9 digit number that is present in the address bar [link of the Book] after visiting any of the chapters
BOOK_ID = input("Enter the ID of the first (or any) chapter of the book : ")

#The name that is entered is given as the filename later
BOOK_NAME = input("Enter the name of the book : ")

#Use the Wattpad Info API to gather the list of all chapter IDs and their names

REQUEST_INFO = requests.get('https://www.wattpad.com/apiv2/info?id=' + BOOK_ID, headers={'User-Agent': 'Mozilla/5.0'})

#The returned object must be parsed from JSON into an object
ALL_CHAPTERS = REQUEST_INFO.json()['group']

#Open a file by specifying the location and extension with Byte-Write Mode

file = codecs.open(str(BOOK_NAME) +".html","wb")

#Insert the  HTML and BODY tags to the beginning of the file
file.write(bytearray("<html><body>".encode(encoding='utf-8')))

#A GROUP is a set Group={ID,TITLE} which represents each Chapter
#For each GROUP get the ID and CHAPTER NAME

for CHAPTER in ALL_CHAPTERS:
    CHAP_ID = str(CHAPTER['ID'])
    CHAP_TITLE =CHAPTER['TITLE']

    print("Parsing Chapter : " + CHAP_TITLE)


    #The Chapter name will be written to the file as a Heading
    HEADING = "<br><br><div align='center'><h2>" + CHAP_TITLE +"</h2></div><br><br>"

    #Since we've opened the file in Byte-Write mode, we need to convert strings to a ByteArray
    file.write(bytearray(HEADING.encode(encoding='utf-8')))

    #Using the ID, gather the HTML from the chapter and get the text

    STORY_REQUEST = Request('https://www.wattpad.com/apiv2/storytext?id=' + CHAP_ID, headers={'User-Agent': 'Mozilla/5.0'})
    TEXT = urlopen(STORY_REQUEST).read()

    #The HTML is parsed and structured into a neat Parse-tree using prettify()

    psoup = BeautifulSoup(TEXT)

    #It is possible there maybe some UNICODE characters such as smileys. Encode them using ASCII
    ACTUAL_CONTENT = psoup.prettify().encode('ascii','ignore')

    #Append the Chapter to the HTML file
    file.write(ACTUAL_CONTENT)

#Add the HTML and BODY closing tags to the end
file.write(bytearray("</body></html>".encode(encoding='utf-8')))

#Close the file
file.close()
print("HTML file eBook is ready!")