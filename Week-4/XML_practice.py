import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def Solution():
    url = 'http://py4e-data.dr-chuck.net/comments_1663073.xml'
    print('Entering', url)
    html = urllib.request.urlopen(url)
    handle = html.read()
    print(len(handle), 'characters')

    tree = ET.fromstring(handle)
    comments = tree.findall('comments/comment')
    count = len(comments)
    sumx = 0

    for i in comments:
        m = float(i.find('count').text)
        sumx += m

    print(count)
    print(sumx)

Solution()

