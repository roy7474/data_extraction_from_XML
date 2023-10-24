'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.

1) The program will prompt for a URL, 
2) read the XML data from that URL using urllib 
3) and then parse and extract the comment counts from the XML data, 
4) compute the sum of the numbers in the file.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)

To make the code a little simpler, you can use an XPath selector string to look through the 
entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
'''

import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl
import xml.etree.ElementTree as ET


url = input('Enter the url of the website that you would like to extract the sum of counts for: ')
XML = urllib.request.urlopen(url).read()#, context=ctx).read()

# parsing the xml
tree = ET.fromstring(XML)

# find all 'count' tags
counts = tree.findall('.//count')

# loop through the tags, extract the text between the tags and convert them to integer
total = 0
for num in counts:
    total += int(num.text)

print('The sum of the numbers in the tag is:',total)