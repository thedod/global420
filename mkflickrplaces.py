import json
from urllib2 import urlopen,quote
from time import sleep
from conf import *
URL_TEMPLATE = "http://api.flickr.com/services/rest/?method=flickr.places.find&api_key={key}&query={query}&format=json&nojsoncallback=1"
DELAY = 2 # Seconds. Avoid flooding API
places = json.load(file('places.json'))
flickrplaces = {}
for p in places:
    print u'==== {0} ===='.format(p)
    try:
        place = json.load(urlopen(URL_TEMPLATE.format(key=FLICKR_KEY,query=quote(p.encode('utf-8')))))
        url = place['places']['place'][0]['place_url']
        print url
        flickrplaces[p] = url
    except Exception,e:
        print e
    sleep(DELAY)
print "Done."
js = file("flickrplaces.js","w")
js.write("window.flickrplaces = ")
json.dump(flickrplaces,js,indent=1)
js.write(";\n")
js.close()
