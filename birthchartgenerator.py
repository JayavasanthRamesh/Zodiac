import remodel

def tochar(integer):
	if(integer<10):
		return  '0'+str(integer)
	else:
		return str(integer)

def place_text(text,count):
	#match=dict()
	#match={'Ven':'venus','Ket':'Kethu','Lag':'lagna','Sun':'Sun','Mar':}
	global planet
	global pos
	text=text.encode('ascii','ignore')
	text=text.replace("RASI","")
	text=text.replace("Gul","")
	text=text.replace(" ","")
	text=text.replace(".","")
	while(text):
		temp=text[:3]
		print(" "+temp+" "+str(count))
		if(pos[count]!=12):
			planet[pos[count]].append(temp)
		text=text[3:]

def birthchart(day,month,year,hour,mins,place):
	import urllib
	import urllib2
	from BeautifulSoup import BeautifulSoup

	gmt="55"
	#10for north 20 for East
	if(place=="chennai"):
		lat="130410"
		lang="801710"

	searchphrase=tochar(day)+tochar(month)+str(year)+tochar(hour)+tochar(mins)+lat+lang+"5301"

	print(searchphrase)

	request = urllib2.Request('http://www.scientificastrology.com/tamil_astrology/tamilchart.aspx?ID='+searchphrase+'&name=jai&place='+place+'&Details=Birth-Chart')
	response=urllib2.urlopen(request)
	html=response.read()
	parse=BeautifulSoup(html)
	table=parse.findAll('table')[1]
	planetmatrix=table.findAll('td')[0]
	planets=planetmatrix.findAll('tr')
	count=0
	for row in planets:
		for cell in row.findAll('td'):
			for font in cell.findAll('font'):
				x=font.string
				print(x)
				place_text(x,count)
				count=count+1

def getplanet_matrix(day,year,month,hour,mins,place): 
	pos=[0,1,2,3,11,12,4,10,5,9,8,7,6]
	planet=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
	globals().update(locals())
	birthchart(25,7,1993,21,00,'chennai')
	#print(planet)
	personal=[]
	result=[]
	globals().update(locals())
	result=remodel.result_gen(planet,result)
	#remodel.result_display(result)
	return result
