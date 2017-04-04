#coding : utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

r = requests.get("http://music.naver.com/listen/top100.nhn?domain=TOTAL")
_html = lxml.html.fromstring(r.text)

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
# Apply the selector to the DOM tree.
nodes = sel(_html)

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist') 
_selRank= CSSSelector('.ranking')
for node in nodes:
    #print lxml.html.tostring(item)
    _rank=_selRank(node)
    _artist=_selArtist(node)
    _name=_selName(node)
    if _rank:
        print _rank[0].text_content(),
        print ".  ",
        print _artist[0].text_content().strip(),
        print " : ",
        print _name[0].text_content()
       