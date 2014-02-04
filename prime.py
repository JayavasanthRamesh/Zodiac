#planetary postions : array of 12 .. each square may have one or more planets .. so

# Jayalalitha
planet=[
		["lagna"],
		["saturn"],
		["moon","mars"],
		[],
		["kethu"],
		[],
		["jupiter"],
		[],
		["mercury","sun"],
		["venus"],
		["ragu"],
		[]
]

#the raasi of the native

raasi="libra"

# the first house is the house where "lagna" is ther ..then the second house is calculated clockwise from it .. so ffind lagna

for i1,inner_planet in enumerate(planet):
	for i2,item in enumerate(inner_planet):
		if(planet[i1][i2]=="lagna"):
			x=i1

# x denotes the array of lagna ... the [:x] splits the lists and holds it in variable k

k=planet[:x]
del planet[:x]
for i1,inner_k in enumerate(k):
	planet.append(k[i1])

#printing the matrix .. appending a [] at first .. so indexing can start from 1 .. else 1st house is to be called 0th house
#print(planet)

planet.insert(0,[])

#dict() is same as map in c .. we might wanna find the pos of moon sometimes .. so using a hash structure

pos=dict()

for i1,inner_planet in enumerate(planet):
	for i2,item in enumerate(inner_planet):
			pos[planet[i1][i2]]=i1

#print(pos)

#each raasi has a benefic , neutral and malefic lord .. to keep track of them .. 1 -> benefic , 0->neutral , -2 ->malefic 
# access them like power["leo"]["mercury"]

power=dict()
power["leo"]={'mars':1,'sun':1,"mercury":-1,"venus":-1,"moon":0,"jupiter":0,"saturn":0,"kethu":0,"lagna":0,"ragu":0}
power["taurus"]={'mars':1,'sun':1,"mercury":1,"venus":0,"moon":-1,"jupiter":-1,"saturn":1,"kethu":0,"lagna":0,"ragu":0}
power["scorpio"]={'mars':0,'sun':1,"mercury":-1,"venus":-1,"moon":1,"jupiter":1,"saturn":0,"kethu":0,"lagna":0,"ragu":0}
power["saggitarus"]={'mars':1,'sun':1,"mercury":-1,"venus":-1,"moon":0,"jupiter":0,"saturn":-1,"kethu":0,"lagna":0,"ragu":0}
power["aries"]={'mars':1,'sun':1,"mercury":-1,"venus":-1,"moon":-1,"jupiter":1,"saturn":-1,"kethu":0,"lagna":0,"ragu":0}
power["capricorn"]={'mars':-1,'sun':0,"mercury":1,"venus":1,"moon":-1,"jupiter":-1,"saturn":1,"kethu":0,"lagna":0,"ragu":0}
power["virgo"]={'mars':-1,'sun':0,"mercury":1,"venus":1,"moon":-1,"jupiter":-1,"saturn":0,"kethu":0,"lagna":0,"ragu":0}
power["libra"]={'mars':1,'sun':-1,"mercury":1,"venus":1,"moon":0,"jupiter":-1,"saturn":1,"kethu":0,"lagna":0,"ragu":0}
power["cancer"]={'mars':1,'sun':0,"mercury":-1,"venus":-1,"moon":1,"jupiter":1,"saturn":0,"kethu":0,"lagna":0,"ragu":0}
power["gemini"]={'mars':-1,'sun':-1,"mercury":0,"venus":1,"moon":0,"jupiter":-1,"saturn":-1,"kethu":0,"lagna":0,"ragu":0}
power["pisces"]={'mars':1,'sun':-1,"mercury":-1,"venus":-1,"moon":1,"jupiter":0,"saturn":-1,"kethu":0,"lagna":0,"ragu":0}
power["cancer"]={'mars':1,'sun':1,"mercury":0,"venus":1,"moon":-1,"jupiter":-1,"saturn":1,"kethu":0,"lagna":0,"ragu":0}


#function that says if the postition is occupied by a benefic planet

def is_benefic(posi):
	if(planet[posi]==[]):
		return 0
	else:
		for x1,item in enumerate(planet[posi]):
			if(power[raasi][item]==1):
				return 1
		return 0



#function that says if the postition is occupied by atleast one malefic planet
def is_malefic(posi):
	if(planet[posi]==[]):
		return 0
	else:
		for x1,item in enumerate(planet[posi]):
			if(power[raasi][item]==-1):
				return 1
			return 0



#each lord has a benefic and malefic house .. to keep track of them .. i initialsied only fr moon nw



#def score(mapl,pos,aspl,aspos):
#module to be complete after aspect values are cleared

#shift position 


def prev_pos(t,shift):
	if(t-shift<1):
		return 12+t-shift
	else:
		return t-shift

def next_pos(t,shift):
	if(t+shift>12):
		return t+shift-12
	else:
		return t+shift

def is_kendra(posi):
	if(posi==1 or posi==4 or posi==7 or posi==10):
		return 1
	else:
		return 0

#result vector 


res=[]


#now ur actual code .. 300 combos ... the result vector holds all the predicted data


#Dhrudhura yoga

m=pos['moon']

if(planet[prev_pos(m,1)]!=[] and planet[next_pos(m,1)]!=[]):
	res.append(["bountiful","wealthy and conveyance"])

#kemadruma yoga .. case pending

if(planet[prev_pos(m,1)]==[] and planet[next_pos(m,1)]==[]):
	res.append(["rogue or swindler","poor","dirty and sorrowful"])

#chandra mandal yoga

if(m==pos['mars']):
	res.append(["earns by unscrupulous means"])

#adhi yoga

if(is_benefic(next_pos(m,6)) and is_benefic(next_pos(m,7)) and is_benefic(next_pos(m,8))):
	res.append(["polite ans trustworthy","happy life","luxurious and healthy"])

#chatusagara yoga

if(planet[1]!=[] and planet[4]!=[] and planet[7]!=[] and planet[10]!=[]):
	res.append(["good reputation","health and prosperous life","good children"])

#vasumathi yoga

if(is_benefic(3) and is_benefic(6) and is_benefic(10) and is_benefic(11)):
	res.append(["command of plenty wealth"])

#rajalakshana yoga

if(is_kendra(pos["jupiter"]) and is_kendra(pos["venus"]) and is_kendra(pos["moon"]) and is_kendra(pos["mercury"])):
	res.append(["attractive appearance"])

#amala yoga

if(is_benefic(next_pos(m,10)) or is_benefic(10)):
	res.append(["ever lasting fame and reputation","spotless character"])


#parvata yoga

if(( planet[6]==[] or is_benefic(6) )and ( planet[8]==[] or is_benefic(8) )):
	res.append(["wealthy","liberal","charitable"])

#vesi yoga

if(planet[2]!=[] and pos["moon"]!=2):
	res.append(["fortunate","happy","famous"])

#vasi yoga

if(planet[2]!=[] and pos["moon"]!=2):
	res.append(["prosperous","happy"])

#obhyachari yoga

if(next_pos(m,1)!=pos['sun'] and prev_pos(m,1)!=pos['sun'] and prev_pos(pos['sun'],1)!=[] and next_pos(pos['sun'],1)!=[]):
	res.append(["eloquent speaker"])

#hamsa , malavaya,sasa,bhadra ??

if(pos['mercury']==pos['sun']):
	res.append(["highly intelligent","skilful","comfort and happiness"])

#pushkala lord of sign ??

#lakshmi - powerful ??

#gouri , bathra - lord of navamsa ?

#exalted lord - sree natha??

temp=[]

for x in pos:
		if(x!="kethu" and x!="lagna" and x!="ragu"):
			temp.append(pos[x])

setp=list(set(temp))

sorted(setp)

if(len(setp)==7):
	if(setp[0]=="1" and setp[6]=="7"):
		#lagna malika
		res.append(["ruler","wealthy"])

	elif(setp[0]=="2" and setp[6]=="8"):
		#dhana malika
		res.append(["resloute","unsympathetic","extremely wealthy"])

	elif(setp[0]=="3" and setp[6]=="9"):
		#vikrama malika
		res.append(["rich","sick"])

	elif(setp[0]=="4" and setp[6]=="10"):
		#sukha malika
		res.append(["charitable","wealthy"])

	elif(setp[0]=="5" and setp[6]=="11"):
		#putra malika
		res.append(["highly religious","famous"])

	elif(setp[5]=="6" and setp[6]=="12"):
		#satru malika
		res.append(["greedy","poor"])

	elif(setp[0]=="1" and setp[6]=="12"):
		#kalata malika
		res.append(["influential"])

	elif(setp[1]=="2" and setp[6]=="12"):
		#randhra malika
		res.append(["poor","hen-pecked"])

	elif(setp[2]=="3" and setp[6]=="12"):
		#bhagya malika
		res.append(["religious","mighty"])

	elif(setp[3]=="4" and setp[6]=="12"):
		#karma malika
		res.append(["espected","virtuous"])

	elif(setp[4]=="5" and setp[6]=="12"):
		#labha malika
		res.append(["skilful","lovely women"])

	else:
		#vraya mallika
		res.append(["honoured","liberal","respected"])


#shankra ?? mutual kendra
#gaja ?? 9th from the 11th ?
#kalanidhi ? swakeshtra
#movable sign - amsaveni

#kusuma yoga
if(pos['jupiter']==0  and m==7 and pos['sun']==next_pos(m,8)):
	res.append(["royal position"])

#matsaya yoga

if(is_malefic(0) and is_malefic(9) and is_malefic(4) and is_malefic(8) and is_malefic(5) and is_benefic(5)):
	res.append(["good-natured","famous","religious"])

#makuta yoga - 9th lord

#vidyut - exaltion deep ?

#indra yoga - lords of 5th and 11th

#trilochana - trines ?

#vajra yoga

if(is_benefic(1) and is_benefic(7) and is_malefic(4) and is_malefic(10)):
	res.append(["happy","handsome"])

#yava yoga

if(is_benefic(4) and is_benefic(10) and is_malefic(7) and is_malefic(1)):
	res.append(["happy in middle life"])

#vallaki yoga,pasa ,damni,sula,yuga ,gola

n=len(setp)

if(n==7):
	res.append(["social","happy","famous"])
elif(n==6):
	res.append(["charitable","protector of cattle"])
elif(n==5):
	res.append(["always surrounded by family and friends"])
elif(n==4):
	res.append(["will pursue argriculture"])
elif(n==3):
	res.append(["cruel","possessive","poor"])
elif(n==2):
	res.append(["drunkard","poor","heretical"])
else:
	res.append(["indolent","ugly","ignorant"])


m=pos['lagna']
n=pos['moon']
o=pos['sun']
#additions to be done

for x in pos:
		temp.append(pos[x])

setp=list(set(temp))

if(planet[next_pos(m,5)]==[] and planet[next_pos(n,5)]==[] and planet[next_pos(o,5)]==[]):
	res.append(["unbroken line of successors","healthy and wealthy"])

#chandra yoga

if(planet[1]!=[] and planet[3]!=[] and planet[5]!=[] and planet[7]!=[] and planet[9]!=[] and planet[11]!=[] and planet[2]==[] and planet[4]==[] and planet[6]==[] and planet[8]==[] and planet[12]==[]):
	res.append(["commands respect","earn and spend well"])

#vajra yoga

if(is_benefic(m) and is_benefic(next_pos(m,7)) and is_malefic(next_pos(m,4)) and is_malefic(next_pos(m,10)) ):
	res.append(["happy","handsome"])

#kamala yoga

if(planet[1]!=[] and planet[4]!=[] and planet[7]!=[] and planet[10]!=[]):
	res.append(["high prestige and fame","innumerable virtues"])

#samadura yoga

if(planet[2]!=[] and planet[4]!=[] and planet[6]!=[] and planet[8]!=[] and planet[10]!=[] and planet[12]!=[] and planet[1]==[] and planet[3]==[] and planet[5]==[] and planet[7]==[] and planet[9]==[] and planet[11]==[]):
	res.append(["will live free without care and worry"])




#vallaki yoga

if(len(setp)==7):
	res.append(["many friends","fond of music and fine arts","happy and famous"])

#damni yoga

elif(len(setp)==6):
	res.append(["highly charitable","helping tendency"])

#pasa yoga

elif(len(setp)==5):
	res.append(["acquire wealth through right means","always be surrounded by friends and relatives"])

#kedara yoga

elif(len(setp)==4):
	res.append(["related to agriculture","helpful"])


#srik yoga

if(is_benefic(2)==0 and is_benefic(3)==0 and is_benefic(5)==0 and is_benefic(6)==0 and is_benefic(8)==0 and is_benefic(9)==0 and is_benefic(11)==0 and is_benefic(12)==0 ):
	res.append(["comfortable life","possess conveyance","many enjoyments"])

####### End of this yoga shit .. up to houses


#ascending raasi calculated

sign=dict()
"""
sign["aries"]=["indepedant thinking","courageous","senstive","ambitious","stubborn and frank","quick tempered"]



sign["taurus"]=["obstinate","proud and ambitious","affectionate and loving","self-reliant","great deal of endurance,latent power","nervous complaints after 50","unhappy children"]

sign["gemini"]=["wavering mind","quickwitted","fond of writing and reading","nervous and restless","liable to fraud","clever","best occupations where ther is much activity"]

if(is_malefic(1)):
	res.append(["trickery and deceitful"])

sign["cancer"]=["extemeley senstive and inquistive","nervous and restless","deeply attatched to family","disappointment in love","talkative","self-reliant","occupations of fluctuating nature","intutitional and perceptive","strong emotions"]

sign["leo"]=["ambitious but avarcious","warm-hearted","cheerful and unimpulsive","adapt to circumstances","sincere in affection","good tempered and sensitive","forgiving nature","struggles more than successes"]

sign["virgo"]=["impulsive and emotional ","fond of learning","methodical and ingenious","specultaive nature","discriminating and influential"]

sign["libra"]=["idealistc,vindictive,forceful,positive","keen foresight","practical men","not senstitive","love justice,peace,order","lover of music","appealing truth and honesty"]

sign["scorpio"]=["sarcastic and impulsive","masculine in nature","subtle mind,hard to influence","fickle-minded","love excitement","often brutal,brusque and appreciate luxury","good conversationalist and writers"]

sign["saggitarus"]=["phlegmatic temperament""inclination for philosophy and occult studies","active ","conservative views","sympathetic and loving","restless and over-anxious","god-fearing , honest and humble","rheumatic and lung diseases in later years"]

sign["capricorn"]=["stoical to miseries of love","secretive,vindictive,cunning and determined","sympathy,self-willed and generosity","perfectionalists and adapt to circumstances","perseverance","great ambitions in life","chatter-boxes"]



sign["aquarius"]=["reserved","generous hearted","intelligent with good memory skills","highly sympathetic","friendly","interesting coversationalists","timid and funky","literary greatness","suffer from critical setbacks in life","not sufficient happiness","much devoted to family"]

sign["pisces"]=["stubborn","physically receptive and highly religious","stoical and bigotted","reserved and do immature decesion making","ambitious to be authoritative","relstles and fond of history","frugal in expenditures","lack self-confidence"]

res.append(sign[raasi])

"""
if(raasi=="aries" and pos["moon"]==1 and pos["saturn"]==1 ):
	res.append("mental affliction")

if(raasi=="capricorn" and (pos["mars"]!=3 or pos["mars"]!=8)):
	res.append(["lack confidence","funky , nervous and weak-minded"])

if(raasi=="aquarius" and is_malefic(1)==0):
	res.append(["can become great teachers,writers and lecturers"])



print("^^^^^^^^^^^^^^^^^^^^   yoga palans :   ^^^^^^^^^^^^^^^^^^^^^^^^^")

end=set()

for item in res:
	for item1 in item:
		end.add(item1)


for item in end:
	print(item)

res=[]

end=[]


#first house ... Effects of planets in first house


if(pos["sun"]==1):
	res.append(["Strong moral nature", "righteous-minded"," ambition and love of power"])
	if(pos["saturn"]==1 or pos["mars"]==1):
		res.append(["impure bood","eye infections"])


if(pos["moon"]==1):
	res.append(["fanciful and romantic","The fortune is generally changing. It makes one an idealist, a great traveller and explorer"])
	if(pos["saturn"]==1):
		res.append(["always worrying"])
	elif(pos["mars"]==1):
		res.append(["strong Sociability","succesful in professions involving conversations with masses"])
	elif(pos["ragu"]==1):
		res.append(["hysterical tendencies"])

if(pos["mars"]==1):
	res.append(["courage","self-confidence","proneness to accidents","unhappy life"]) 

if(pos["mercury"]==1):
	res.append(["humorous","Quickness of wit","mental ingenuity"])
	if(pos["kethu"]==1 or pos["ragu"]==1):
		res.append(["lot of nervous troubles"])

if(pos["jupiter"]==1):
	res.append(["magnetic personality","optimistic spirit"])
	if(pos["ragu"]==1):
		res.append(["Lawyers, professors, writers, theologians"],["can be a great leader"])


if(pos["venus"]==1):
	res.append(["cheerful temperament","interest of art,music,drama and singing","good fortune","magnetic and attractive personality"])
	if(is_malefic(1)):
		res.append(["unhappy marital life"])


if(pos["saturn"]==1):
	res.append(["Moral stability","inactive","slow progress","misfortunes in early part of life"])
	if(is_malefic(1)==0):
		res.append(["concerns over social welfare"])


if(pos["ragu"]==1):
	res.append(["ill health","hypocrite","bad for marriage"])

if(pos["kethu"]==1):
	res.append(["Psychic powers","deceitful","strange appetites","unhappy married life"])


#fourth house ... Effects of planets in first house


if(pos["sun"]==4):
	res.append(["unhappy","mentally worried"])
	if (pos["mars"]==4 or pos["saturn"]==4):
	 	res.append(["obstacles in life"])

if(pos["moon"]==4):
	res.append(["derives happiness from relatives","cheerful and contented","becomes important as a leader or ruler"])
	

if(pos["mars"]==4):
	res.append(["unhappy","successful political life"])
	if(pos["ragu"]==4 or pos["kethu"]==4):
		res.append(["suicude thoughts"]) 


if(pos["mercury"]==4):
	res.append(["good educationist or diplomat","high esteem","frequent foreign travelling","witty"])


if(pos["jupiter"]==4):
	res.append(["happy","respected","fortunate"]) 



if(pos["venus"]==4):
	res.append(["well versed in music","deep attachment to mother","happiness"])


if(pos["saturn"]==4):
	res.append(["sick during early years","unhappy","suffers from windy and phlegmatic complaints","secluded life"])


if(pos["ragu"]==4):
	res.append(["Foolish","few friends"])

if(pos["kethu"]==4):
	res.append(["deprived of mother, properties and happiness"])

#seventh house... Effects of planets in seventh house


if(pos["sun"]==7):
	res.append(["fair looking","thining hair","few friends and difficulty in getting along with people","delayed marriage","likes foreign things"]) 

if(pos["moon"]==7):
	res.append(["passionate","easily routed to jealousy","good-looking wife","narrow-minded","stingy","energetic"])
	

if(pos["mars"]==7):
	res.append(["submissive to women","intelligent","stubborn","tactless"])

if(pos["mercury"]==7):
	res.append(["man of virtue and geniality","profound knowledge of law","skilled in business tactics and trade","writing ability","good physique"])
	

if(pos["jupiter"]==7):
	res.append(["diplomatic","goodlooking wife","good education","sensitive to others' feelings","undertakes pilgrimages to distant places","good sons"])
	

if(pos["venus"]==7):
	res.append(["fond of quarreling","sensuous","passionate","unhealthy habits","charming","successful in partnerships with other sex"])
	
if(pos["saturn"]==7):
	res.append(["under wife's control","diplomatic","enterprising","has a residence abroad","political success"])

if(pos["ragu"]==7):
	res.append(["ill-repute","unconventional and heterodox","luxurious habits","suffers from ghosts and the supernatural"])

if(pos["kethu"]==7):
	res.append(["not a satisfactory marriage","passionate","sinful"])

#10th house

if(pos["sun"]==10):
	res.append(["successful in all that he undertakes","strong and happy","ancestral wealth","fond of music","personal magnetism"])

if(pos["moon"]==10):
	res.append(["religious, wealthy, intelligent and bold","succeed in all his endavours","have many friends", "lead a comfertable and long life"])

if(pos["mars"]==10):
	res.append(["fond of praise","take bold steps in governing","earn much money","skilled scientist or technician"])

if(pos["mercury"]==10):
	res.append(["happy","straightforward person","scholar","engaged in accquiring more knowledge and fame","childless"])

if(pos["jupiter"]==10):
	res.append(["high official in the government","rich","virtuous","steadfast in his spiritual life", "head of academic and research institutions"])

if(pos["venus"]==10):
	res.append(["earns through houses and buildings","influential","social, friendly and renowned","have healing powers","skilled trader"])

if(pos["saturn"]==10):
	res.append(["ruler or minister","brave, rich and famous","dispassionate in nature","will work for the downtrodden masses","visit several holly rivers and shrines"]);

if(pos["ragu"]==10):
	res.append(["skilled artist","flair for poetry and litrature","travels widely", "well learned","bold and adventurous","commits many sins"])

if(pos["kethu"]==10):
	res.append(["strong, bold and well known","commit vile deeds","face many obstacles in undertakings","very clever"])

print("^^^^^^^^^^^^^^^^^^^^   kendra palans :   ^^^^^^^^^^^^^^^^^^^^^^^^^")

end=set()

for item in res:
	for item1 in item:
		end.add(item1)


for item in end:
	print(item)

res=[]

end=[]

#second house ... Effects of planets in first house


if(pos["sun"]==2):
	res.append(["stubborn and peevish."]) 

if(pos["moon"]==2):
	res.append(["large family","reserved and not much sociable"])
	
if(pos["mars"]==2):
	res.append(["good conversationalist","befriend evil-minded","unsympathetic"])


if(pos["mercury"]==2):
	res.append(["rich","Highly intelligent","charity minded","clever"])

if(pos["jupiter"]==2):
	res.append(["a poet, a great writer, astrologer or even a scientist","good wife"])

if(pos["venus"]==2):
	res.append(["Large family","Handsome appearance","skilful and pleasant"])


if(pos["saturn"]==2):
	res.append(["Harsh speech","unsocial","sorrowful","unhappy","unpopular"]) 

if(pos["ragu"]==2):
	res.append(["Peevish","danger to eye-sight"])

if(pos["kethu"]==2):
	res.append(["Bad speaker","Loss through fraud and deception"])

#third house ... Effects of planets in first house


if(pos["sun"]==3):
	res.append(["courageous","resourceful and restive mind","successful","Subordinate to wife","Attached to children"]) 

if(pos["moon"]==3):
	res.append(["change occupation frequently","fond of travelling and active minded","attached to children"])
	if(is_malefic(3)):
		res.append(["no peace in life","unscrupulous"])
	

if(pos["mars"]==3):
	res.append(["Liability to danger and accidents by journeys","Brave","Reckless","ear defects or even deafnes","Worried on account of family misunderstandings","unprincipled"])
	if(is_malefic(3)):
		res.append(["violent"]) 


if(pos["mercury"]==3):
	res.append(["tactful and diplomatic","sharp mind","independant views","successful in trade","liked by friends and family"])
	if(is_malefic(3)):
		res.append(["nervous breakdown"])

if(pos["jupiter"]==3):
	res.append(["optimistic and philosophical","will become a miser","ill health","not much friends"])
	if(is_malefic(3)):
		res.append(["poor social life"])


if(pos["venus"]==3):
	res.append(["poor health","low in finances","troubling children"])
	if(is_malefic(3)):
		res.append(["miserly, mean, poor and highly sensual"])


if(pos["saturn"]==3):
	res.append(["Brave and courageous"," wealthy","eccentric and cruel","success only after failures","will attain high influential positions"])
	if(is_malefic(3)):
		res.append(["mental affliction"])


if(pos["ragu"]==3):
	res.append(["brave","bad sibling"])

if(pos["kethu"]==3):
	res.append(["strong and adventuourous","funky","disturbed mind"])



#fifth house ... Effects of planets in fifth house

if(pos["sun"]==5):
	res.append(["happiness","riches","associated with forests","heart problems"]) 

if(pos["moon"]==5):
	res.append(["clarity of mind","acquisition of land","has opportunities to serve the state","truthful","god-fearing"])
	
	

if(pos["mars"]==5):
	res.append(["disturbed thoughts","weak-minded","health may be affected"])

if(pos["mercury"]==5):
	res.append(["learned and happy","intelligent"])
	

if(pos["jupiter"]==5):
	res.append(["learned in logic","great discriminating power","decorous manners"])
	

if(pos["venus"]==5):
	res.append(["poetic","large number of friends","happiness through offspring"])
	


if(pos["saturn"]==5):
	res.append(["variable in profits","weak"])

if(pos["ragu"]==5):
	res.append(["mistaken by others","infriended"])

if(pos["kethu"]==5):
	res.append(["peculiar experiences with feelings","inclination towards spirituality towards the older age"])


#sixth house ... Effects of planets in sixth house


if(pos["sun"]==6):
	res.append(["good politician","illness","wealthy","successful"]) 

if(pos["moon"]==6):
	res.append(["ill-health during childhood","success as caterer"])
	
	

if(pos["mars"]==6):
	res.append(["passionate","victorius","worries from near relatives"])

if(pos["mercury"]==6):
	res.append(["Quarrelsome and showy but yet respected","lazy"])
	

if(pos["jupiter"]==6):
	res.append(["inactive","feared by enemies","health generally good","dyspeptic"])
	

if(pos["venus"]==6):
	res.append(["no enemies","favourable for getting favours from women"])
	
if(pos["saturn"]==6):
	res.append(["quarrelsome","voracious eater","courageous","sickness due to neglect"])

if(pos["ragu"]==6):
	res.append(["long lived","wealth","sickess of puzzling nature","many cousins"])

if(pos["kethu"]==6):
	res.append(["fame and authorithy","foelss","loose moral character","good intuitive power"])




#eight house... Effects of planets in eighth house
# the sun

if(pos["sun"]==8):
	res.append(["lives long"])
	

if(pos["moon"]==8):
	res.append(["subject to mental aberration","has psychological complexes","capricious and unhealthy","slender","weak eye sight","fond of amusement and is large hearted"])
	
if(pos["mars"]==8):
	res.append(["short lived unless there are other alleviating factors","few children","hates his relatives","control many people"])

if(pos["mercury"]==8):
	res.append(["known for good qualities","known for breeding and courteous disposition","inherits a lot of wealth","learned and ll get scholarships","live long but weak constitution"])
	

if(pos["jupiter"]==8):
	res.append(["ll be unhappy but generous hearted","long life","have difficulty in speech","pretends to be noble","painless death"])

if(pos["venus"]==8):
	res.append(["many blessings","much wealthy","life of comfort","emotional disappointments in early life","life of piety in later life"])
	
if(pos["saturn"]==8):
	res.append(["longetivity but more responsibilities","sheer perseverance","defective eyes","few children"])
	if(pos['moon']==8):
		res.append(["spleen troubles"])

if(pos["ragu"]==8):
	res.append(["troubled by ailments","public censure","vicious","quarrelsome",""])

if(pos["kethu"]==8):
	if(is_benefic(8)):
		res.append(["enjoy wealth","live long"])

#print(res)

#print(len(res))

if(pos["sun"]==9):
	res.append(["issues with father and family","ambitious and enterprising"])

if(pos["moon"]==9):
	res.append(["fortunate and prosperous", "principled and generous-minded","build charitable institutions","visit foreign countries"])

if(pos["mars"]==9):
	res.append(["wield authority and be affluent","have many children","not a dutiful son","famous for his good qualities","eif-seeking, stubborn and impetuous"])

if(pos["mercury"]==9):
	res.append(["accquire much education and wealth","scientific mind","fond of music","friendly relations with father"])

if(pos["jupiter"]==9):
	res.append(["exponent of law, philosophy, etc","visit foreign lands as a lecturer, preacher, etc.","conservative and principled"])

if(pos["venus"]==9):
	res.append(["born fortunate and endowed with fame","sauve and polished in speech","diplomat","notorious as a libertine"])

if(pos["saturn"]==9):
	res.append(["lonely life","valour on the battle field","untruthful and deceitfu","founder of charitable institutions"])

if(pos["ragu"]==9):
	res.append(["nagging and domineering wife","impolite and loose of morals","hate his father","famous","accquire wealth"])

if(pos["kethu"]==9):
	res.append(["short tempered","eloquet","fond of pomp and show","arrogant","good wife and children"])






if(pos["sun"]==11):
	res.append(["long life","becomes wealthy","gets royal and governmental favours","achieves success without much effort","sagacious and principled"])

if(pos["moon"]==11):
	res.append(["noble, generous and blessed","intospective by nature","make profits in business"])

if(pos["mars"]==11):
	res.append(["eloquent and forceful speaker", "clever","rich","accquire landed properties","wield influence in top cirlcles"])

if(pos["mercury"]==11):
	res.append(["learned in many sciences","possess a keen and sharp intellect" ,"wealthy" ,"truthful", "happy","prosper in engineering ventures"])

if(pos["jupiter"]==11):
	res.append(["long lived","bold and wealthy","piercing intellect","fond of music","accumulate riches","have many friends"])

if(pos["venus"]==11):
	res.append(["wandering nature","make immense profits","possess all kinds of comforts and luxuries","popular","have many friends"])

if(pos["saturn"]==11):
	res.append(["earns through employing many men","few friends","fond of enjoyment","long and healthy life","involved in politics commanding great respect"])

if(pos["ragu"]==11):
	res.append(["distinguishes himself in the army or navy","famous","wealthy","learned","few children","earn in foriegn countries"])

if(pos["kethu"]==11):
	res.append(["will have a habbit of hoarding","monetary windfall through speculations likr lottery, horse racing and stock exchange","noble","succeed in all his ventures","participate in charity"])



if(pos["sun"]==12):
	res.append(["immoral life","unsuccessful","may feel neglected","loss of limb","weal eyesight", "energetic"])

if(pos["moon"]==12):
	res.append(["suffer from deformity","narrow-minded","hard-hearted","mischievous","weak eyesight"])

if(pos["mars"]==12):
	res.append(["selfish and hateful","suffer from diseases","may lose money","liable to deception"])

if(pos["mercury"]==12):
	res.append(["suffer penury","unhappy","have few children"])

if(pos["jupiter"]==12):
	res.append(["may deride religion","evil minded","repents and reforms himself","always anxious about vehicles, ornaments and clothes"])

if(pos["venus"]==12):
	res.append(["desertion by relatives","hankering after comforts","miserable life","indulge in lying"])

if(pos["saturn"]==12):
	res.append(["dull-headed","lose all his money","make many enimies","suffer loses in trade","commit several sins"])

if(pos["ragu"]==12):
	res.append(["prosperous","immoral","helpful nature","eye troubles"])

if(pos["kethu"]==12):
	res.append(["restless and wandering mind","leave the country of birth","inherited property may be lost"])



print("^^^^^^^^^^^^^^^^^^^^   other house palans :   ^^^^^^^^^^^^^^^^^^^^^^^^^")



end=set()

for item in res:
	for item1 in item:
		end.add(item1)


for item in end:
	print(item)

#print(len(item))