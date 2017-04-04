#coding : utf-8
from urllib import urlopen
from urllib import FancyURLopener
import re
import urllib2

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q=psy')
html=page.read()
p=re.compile('href="https://www.youtube.*?"')

res=p.findall(html)
for item in res:
    print item[:100]