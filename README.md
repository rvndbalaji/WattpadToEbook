Python script to web-scrape Wattpad Books and prepare a HTML file of the book
The HTML file itself is the entire eBook
It can later be converted to EPUB or MOBI formats using eBook Generators such as KindleGen

Libraries/Imports used :
    1. Urllib
    2. Requests
    3. BeautifulSoup
    4. Codecs
OUTPUT: A HTML file containing the entire eBook with all chapters.
        This can later be converted to any eBook using third-party tools
        such as KindleGen or Calibre


TO RUN: 
```
python watty_ebook.py
```

>> ID is the 9 digit number that is present in the address bar [link of the Book] after visiting any of the chapters
![alt tag](https://github.com/rvn-balaji/WattpadToEbook/blob/master/Capture.PNG)

>> The name that is entered is given as the filename later
![alt tag](https://github.com/rvn-balaji/WattpadToEbook/blob/master/Capture-2.PNG)
