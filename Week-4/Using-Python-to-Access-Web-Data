
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE     


# My solution
url = 'http://py4e-data.dr-chuck.net/known_by_Gael.html'

n = int(input('Enter count: '))
y = int(input('Enter pos: '))
# http://py4e-data.dr-chuck.net/known_by_Gael.html



for i in range(0,n):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a')
    lst = []
    

    for tag in tags:

        lst.append(tag.get('href'))
        

    url = lst[y-1]
    print('Retrieving... ', url)
    continue

o = url.split("_")
p = o[2].split('.')
name = p[0]

print('Your search is', name)
