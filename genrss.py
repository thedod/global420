import json,datetime,urllib2,random
from PyRSS2Gen import RSS2, RSSItem

timezones = json.load(file('tz.json'))

def getUTC():
    return int((datetime.datetime.utcnow()-datetime.datetime(1970, 1, 1)).total_seconds())%(24*3600)

def get420offset():
    offset = 16*3600+20*60-getUTC()
    if offset<0:
        offset += 24*3600
    return offset

def next420():
    offs = get420offset()
    for tz in timezones:
        if tz[0]<=offs:
            return {'minutes':int((offs-tz[0])/60),'places':tz[1]}
    return {'minutes':666,'places':["Snafu (Yes. It's a bug)"]}



def main():
    fourtwenty = next420()
    place = random.choice(fourtwenty['places'])
    if len(fourtwenty['places'])>1:
        title = "Get ready for #fourtwenty at {0} and other fine places.".format(place)
    else:
        title = "Get ready for #fourtwenty at {0}.".format(place)
        
    file('420.rss','w').write(RSS2(
       title='Global 4:20 clock',
       link='https://zzzen.com/420',
       description='Keep up with where #FourTwenty happens next',
       language='en',
       items=[RSSItem(
           title=title,
           link='http://https://zzzen.com/420#{0}'.format(urllib2.quote(place)))]).to_xml('utf-8'))

if __name__=='__main__':
    main()
