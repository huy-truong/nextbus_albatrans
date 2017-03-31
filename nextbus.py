import http.client
import re
import datetime

import subprocess

conn = http.client.HTTPSConnection('www.vianavigo.com')

now = datetime.datetime.now()
d='%02d'%now.day
m='%02d'%now.month
y ='%04d'%now.year
h ='%02d'%now.hour
mi ='%02d'%(now.minute+7)


path = '/stif_web_carto/comp/itinerary/search.html?mrq=&id=&departure=domaine+de+corbeville%2C+Orsay&departureType=Site&departureCity=Orsay&departureCoordX=&departureCoordY=&departureExternalCode=79671&departureCityCode=91400&arrival=GARE+DE+MASSY+PALAISEAU%2C+Massy&arrivalType=StopArea&arrivalCity=Massy&arrivalCityCode=91300&arrivalCoordX=&arrivalCoordY=&arrivalExternalCode=8739357&date={date}%2F{month}%2F{year}&dateFormat=dd%2FMM%2Fyyyy&sens=1&hour={hour}&min={minute}&moreCriterions=true&via=&viaType=&viaCity=&viaCityCode=&viaExternalCode=&train=true&_train=on&rer=true&_rer=on&metro=true&_metro=on&bus=true&_bus=on&tram=true&_tram=on&walkSpeed=1&spcar=%C3%A2&hpx=1&hat=1&L=0&submitSearchItinerary=&ajid=/stif_web_carto/comp/itinerary/search.html_&ajid=/stif_web_carto/comp/itinerary/search.html_&_=1490965133060'.format(date=d,month=m,year=y,hour=h,minute=mi)


header = {'Accepted':'text/html', 'Accept-Language':'en-US;q=0.5'}

pattern = b"part : \d\d:\d\d"
conn.request("GET", path,'',header)
r1 = conn.getresponse()
reps = r1.read()
r = re.findall(pattern,reps)

t,lh,lm = str(r[0].decode('utf-8')).split(':')


sentence = 'The next bus is at {0}:{1}'.format(lh,lm)
print (sentence)


subprocess.call(['espeak','-s 100',sentence])



