def hardcode_chart():
	
	planet=[
		["Lag","Mar"],
		[],
		[],
		["Jup"],
		["Mon"],
		["Rah"],
		[],
		[],
		["Mer","Sat"],
		["Sun","Ven"],
		[],
		['Ket'],
	]
	raasi="taurus"
	globals().update(locals())

def initialize(planet,raasi):	

	planet=planet[:12]

	for i1,inner_planet in enumerate(planet):
		for i2,item in enumerate(inner_planet):
			if(planet[i1][i2]=="Lag"):
				x=i1

	k=planet[:x]
	del planet[:x]
	for i1,inner_k in enumerate(k):
		planet.append(k[i1])

	planet.insert(0,[])

	print(planet)
	pos=dict()

	for i1,inner_planet in enumerate(planet):
		for i2,item in enumerate(inner_planet):
				pos[planet[i1][i2]]=i1

	#check point 1:  checking positions of lagna
	print(pos)

	lagna=pos['Lag']
	sun=pos["Sun"]
	moon=pos['Moo']
	mars=pos['Mar']
	venus=pos['Ven']
	jupiter=pos['Jup']
	saturn=pos['Sat']
	kethu=pos['Ket']
	ragu=pos['Rah']
	mercury=pos['Mer']
	kethu=pos['Ket']

	temp=[]

	for x in pos:
			if(x!='Ket' and x!='Lag' and x!='Rah'):
				temp.append(pos[x])

	setp=list(set(temp))

	res=[]
	person=[]
	wealthy = 0 
	happy = 0
	healthy = 0

	length_of_planets=len(setp)

	power=dict()
	
	power["leo"]={'Mar':1,"Sun":1,"Mer":-1,'Ven':-1,'Moo':0,'Jup':0,'Sat':0,'Ket':0,'Lag':0,'Rah':0}
	power["taurus"]={'Mar':1,"Sun":1,"Mer":1,'Ven':0,'Moo':-1,'Jup':-1,'Sat':1,'Ket':0,'Lag':0,'Rah':0}
	power["scorpio"]={'Mar':0,"Sun":1,"Mer":-1,'Ven':-1,'Moo':1,'Jup':1,'Sat':0,'Ket':0,'Lag':0,'Rah':0}
	power["saggitarus"]={'Mar':1,"Sun":1,"Mer":-1,'Ven':-1,'Moo':0,'Jup':0,'Sat':-1,'Ket':0,'Lag':0,'Rah':0}
	power["aries"]={'Mar':1,"Sun":1,"Mer":-1,'Ven':-1,'Moo':-1,'Jup':1,'Sat':-1,'Ket':0,'Lag':0,'Rah':0}
	power["capricorn"]={'Mar':-1,"Sun":0,"Mer":1,'Ven':1,'Moo':-1,'Jup':-1,'Sat':1,'Ket':0,'Lag':0,'Rah':0}
	power["virgo"]={'Mar':-1,"Sun":0,"Mer":1,'Ven':1,'Moo':-1,'Jup':-1,'Sat':0,'Ket':0,'Lag':0,'Rah':0}
	power["libra"]={'Mar':1,"Sun":-1,"Mer":1,'Ven':1,'Moo':0,'Jup':-1,'Sat':1,'Ket':0,'Lag':0,'Rah':0}
	power["aquarius"]={'Mar':1,"Sun":0,"Mer":-1,'Ven':-1,'Moo':1,'Jup':1,'Sat':0,'Ket':0,'Lag':0,'Rah':0}
	power["gemini"]={'Mar':-1,"Sun":-1,"Mer":0,'Ven':1,'Moo':0,'Jup':-1,'Sat':-1,'Ket':0,'Lag':0,'Rah':0}
	power["pisces"]={'Mar':1,"Sun":-1,"Mer":-1,'Ven':-1,'Moo':1,'Jup':0,'Sat':-1,'Ket':0,'Lag':0,'Rah':0}
	power["cancer"]={'Mar':1,"Sun":1,"Mer":0,'Ven':1,'Moo':-1,'Jup':-1,'Sat':1,'Ket':0,'Lag':0,'Rah':0}

	malefic=[]
	benefic=[]
	globals().update(locals())

	for i in range(1,12):
		if(is_malefic_check(i)):
			malefic.append(1)
		else:
			malefic.append(0)

	for i in range(1,12):
		if(is_benefic_check(i)):
			benefic.append(1)
		else:
			benefic.append(0)
	
	#check point 2: Checking benefic and malefic positions 
	#print(malefic)
	#print(benefic)

	globals().update(locals())

def is_benefic_check(posi):
	if(planet[posi]==[]):
		return 0
	else:
		for x1,item in enumerate(planet[posi]):
			if(power[raasi][item]==1):
				return 1
		return 0

def is_malefic_check(posi):
	if(planet[posi]==[]):
		return 0
	else:
		for x1,item in enumerate(planet[posi]):
			if(power[raasi][item]==-1):
				return 1
			return 0

def is_malefic(posi):
	return malefic[posi-1]

def is_benefic(posi):
	return benefic[posi-1]

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

def fame():

	global result

	if(planet[1]!=[] and planet[4]!=[] and planet[7]!=[] and planet[10]!=[]):
		result.append(["He/She will have good reputation in the society."])

	elif( (planet[2]!=[] and moon!=2 ) or (setp[0]=="5" and setp[6]=="11") or (length_of_planets==7) or (venus==9) or venus==11):
		result.append(["The person will be very famous."])
	
	elif(planet[1]!=[] and planet[4]!=[] and planet[7]!=[] and planet[10]!=[]):
		result.append(["He will earn high prestige and fame."])

	if ( (setp[0]=="1" and setp[6]=="12") or venus==10):
		result.append(["He will be very influential."])

	if((setp[3]=="4" and setp[6]=="12" ) or jupiter==7 ):
		result.append(["He will be highly respected and virtuous."])

def life():

	global result

	if((planet[2]!=[] and moon!=2) or moon==9):
		result.append(["Fortune knocks his door every day."])
	
	if(planet[1]!=[] and planet[3]!=[] and planet[5]!=[] and planet[7]!=[] and planet[9]!=[] and planet[11]!=[] and planet[2]==[] and planet[4]==[] and planet[6]==[] and planet[8]==[] and planet[12]==[]):
		result.append(["He commands respect."])
		result.append(["The native will earn and spend well."])

	if(planet[2]!=[] and planet[4]!=[] and planet[6]!=[] and planet[8]!=[] and planet[10]!=[] and planet[12]!=[] and planet[1]==[] and planet[3]==[] and planet[5]==[] and planet[7]==[] and planet[9]==[] and planet[11]==[]):
		result.append(["The native will live free without care and worry."])

	if(len(setp)==7 or mercury==9 or jupiter==11 or sun==10):
		result.append([" He will be fond of music and fine arts."])

	if(sun==11 or jupiter==11):
		result.append(["The native will lead a long life."])
	
	if(mars==11):
		result.append(["The native will accquire landed properties.The native will have influence in top cirlcles."])

	if(kethu==11):
		result.append(["The native will go through monetary windfall through speculations like lottery, horse racing and stock exchange."])

	if(sun==10):
		result.append(["The native will have success in all that he undertakes.He will possess ancestral wealth."])

	elif(moon==10 or sun==10):
		result.append(["The native will succeed in his endeavors."])
           
	if(venus==8):
		result.append(["The native will have many blessings ,life of comfort,emotional disappointments in early life and life of piety in later life."])

	if(saturn==8):
		result.append(["The native will have longetivity but with more responsibilities."])


	if(planet[2]!=[] and planet[4]!=[] and planet[6]!=[] and planet[8]!=[] and planet[10]!=[] and planet[12]!=[] and planet[1]==[] and planet[3]==[] and planet[5]==[] and planet[7]==[] and planet[9]==[] and planet[11]==[]):
		result.append(["The native will live free without care and worry."])
	
	elif(sun==4):
		result.append(["The native will be mentally worried."])
	
	if (sun==4 and (mars==4 or saturn==4)):
		result.append(["The native will face obstacles in life."])
	
	if(mars==4 and (ragu==4 or kethu==4)):
		result.append(["The native will have suicidal thoughts."]) 	
	
	if(jupiter==7):
		result.append(["The native will undertake pilgrimages to distant places."])

	elif(ragu==10):
		result.append(["The native will travel widely."])
	
	elif(saturn==7):
		result.append(["The native will have a residence abroad."])
	
	elif(moon==3):
           	result.append(["The native will be fond of travelling and is active minded."])

	if(jupiter==10):		
		result.append(["The native will be steadfast in his spiritual life.", ])

	elif(kethu==5):
		result.append(["The native will have peculiar experiences with feelings and inclination towards spirituality towards the older age."])

	elif(jupiter==3):
           	result.append(["The native will have a philosophical outlook on life."])

	if(ragu==5):
		result.append(["The native will be mistaken by others."])
	
	if(moon==8):
		result.append(["The native will be fond of amusement."])

	if(kethu==2):
           	result.append(["The native will experience loss through fraud and deception."])

	if(moon==5):
			result.append(["The native will have acquisition of land and oppotunities to serve the state."])

def beauty():

	global result 

	if(is_kendra(jupiter) and is_kendra(venus) and is_kendra(moon) and is_kendra(mercury)):
		result.append(["The native will have attractive appearance."])

	elif(is_benefic(1) and is_benefic(7) and is_malefic(4) and is_malefic(10)):
		result.append(["He/She will be extremely good looking."])
	
	elif ( (is_benefic(1) and is_benefic(8) and is_malefic(5) and is_malefic(11) ) or venus==2 ):
		result.append(["He/She will be handsome."])

	elif(sun==7):
		result.append(["The native will be fair looking and will have thining hair."])
	
	if(mercury==7):
		result.append(["The native will have a good physique."])

#end of jai

#hema
def character():
		
	good=0
	global result

	if((jupiter==1 or venus==1) and good!=-1):
		good=1
		result.append(["The native will have a magnetic personality and optimistic spirit."])
				
	if(is_malefic(3) and good!=1):
		good=-1
		result.append(["The native will be miserly, mean  and highly sensual."])
				
	if(length_of_planets==7 and setp[5]=="6" and setp[6]=="12" and good!=1):
		good=-1
		result.append(["He will be greedy."])

	if(length_of_planets==7 and setp[2]=="3" and setp[6]=="12" and good!=-1):
		good=1
		result.append(["He will be religious and mighty."])				

	if(moon==10 and good!=-1):
		good=1
		result.append(["he will be religious."])
					
	if(moon==1 and good!=-1):
		good=1
		result.append(["The fortune is generally changing. It makes one an idealist, a great traveller and explorer."])
		result.append(["The native will be fanciful and romantic."])
					
	if(mars==1 and good!=-1):
		good=1
		result.append(["The person will be couragious and self-confident."])	
					
	if(mercury==1 and good!=-1):
		good=1
		result.append(["The native will show traits of humor, wit and mental ingenuity."])
					
	if(mercury==4 and good!=-1):
		good=1
		result.append(["The person will have high esteem.","The person will be witty."])
					
	if(sun==7):
		result.append(["The person will like exotic stuff."])
					
	if(mars==7 and good!=-1):
		good=1
		result.append(["The native will be submissive to women."])
					
	if(moon==10 and good!=-1):
		good=1
		result.append(["The native will be religious, intelligent and bold."])
					
	if(mars==10 and good!=-1):
		good=1
		result.append(["The native will be fond of praise","The native will take bold steps in governing."])
					
	if(mercury==10 and good!=-1):
		good=1
		result.append(["The native will be a straightforward person."])
					
	if(venus==10 and good!=-1):
		good=1
		result.append(["The person will be influential and friendly."])
					
	if(saturn==10 and good!=-1):
		good=1
		result.append(["The native will be dispassionate in nature.","The native will visit several holly rivers and shrines."])
		result.append(["The person will be brave."])	
					
	if(kethu==10 and good!=-1):
		good=1
		result.append(["The native will be strong, bold, well known and clever."])
			
	if(sun==9 and good!=-1):
		good=1
		result.append(["He will be ambitious and enterprising."])

	if(kethu==9 and good!=1):
		good=-1
		result.append(["He will be short tempered and arrogant."])
			
	if(saturn==3 and good!=1):
		good=-1
		result.append(["The native will be eccentric and cruel."])
					
	if(venus==9 and good!=-1):
		good=1
		result.append(["He will be sauve and polished in speechand diplomatic in actions."])
					
	if(mercury==6 and good!=1):
		good=-1
		result.append(["The native will be quarrelsome, showy, lazy but yet respected."])

	if(kethu==9 and good!=1):
		good=-1
		result.append(["He will be short tempered and arrogant."])
				
	if(mars==5 and good!=1):
		good=-1
		result.append(["The native will have disturbed thoughts and is weak-minded."])
				
	if(mercury==5 and good!=-1):
		good=1
		result.append(["The native will be learned,intelligent."])
				
	if(ragu==3 and good!=-1):
		good=1
		result.append(["The native will be brave."])
				
	if(saturn==3 and good!=-1):
		good=1
		result.append(["The native will be brave, courageous."])
				
	if(is_malefic(3) and good!=1):
		good=-1
		result.append(["The native will be violent."])
				
	if(jupiter==5 and good!=-1):
		good=1
		result.append(["The native will have decorous manners."])
				
	if(venus==5):
		result.append(["The native will be poetic."])
				
	if(sun==3 and good!=-1):
		good=1
		result.append(["The native will be courageous,resourceful and restive mind."])
				
	if(saturn==2 and good!=1):
		good=-1
		result.append(["The native will be unsocial","The native will have harsh speech."])
				
	if(kethu==6 and good!=-1):
		good=1
		result.append(["The native will be authoritative,foeless with a good intuitive power."])
				
	if(mars==8):
		result.append(["The native will control many people."])


	if(sun==2 and good!=1):
		good=-1
		result.append(["The native will be stubborn and peevish."])
				
	if(mars==2):
		result.append(["The native will make wrong friends."])
				
	if(mercury==2 and good!=-1):
		good=1
		result.append(["The native will be highly intelligent and clever."])
				
	if(mars==2):
		result.append(["The native will be a good conversationalist and unsympathetic."])
				
	if(kethu==3):
		result.append(["The native will be strong and adventuourous,funky but disturbed."])
				
	if(moon==5 and good!=-1):
		good=1
		result.append(["The native will be god-fearing,truthful with a clarity of mind."])
				
	if(ragu==8 and good!=1):
		good=-1
		result.append(["The native will be vicious and quarrelsome."])
				
	if(jupiter==6 and good!=1):
		good=-1
		result.append(["The native will be inactive but feared by enemies."])
				
	if(saturn==6 and good!=1):
		good=-1
		result.append(["The native will be a quarrelsome person,voracious eater and courageous."])


def wealth():

	wealth=0
	global result
	if(is_benefic(3) and is_benefic(6) and is_benefic(10) and is_benefic(11)):
		wealth= wealth + 5 
					
	if(( planet[6]==[] or is_benefic(6) )and ( planet[8]==[] or is_benefic(8) )):
		wealth = wealth + 5

	if(mercury==9):
		wealth=wealth + 1

	if(venus==11):
		wealth=wealth + 1
			
	if(is_benefic(3) and is_benefic(6) and is_benefic(10) and is_benefic(11)):
		wealth = wealth +5
				           	
	if(( planet[6]==[] or is_benefic(6) )and ( planet[8]==[] or is_benefic(8) )):
		wealth = wealth +5
				           	

					
	if(sun==10):
		wealth=wealth+1
					
	if(venus==10):
						#result.append(["The native will earn through houses and buildings."])
		wealth=wealth+1

	if(kethu==8):
		if(is_benefic(8)):
			wealth=wealth+1
				
	if(mercury==8):
		wealth=wealth+1
				
	if(saturn==3):
		wealth=wealth-1
				
	if(is_malefic(3)):
		wealth=wealth-1
				
	if(sun==5):
		wealth=wealth+1
				
	if(mercury==2):
		wealth=wealth+1
				
	if(venus==3):
		wealth=wealth-1
				
	if(sun==6):
		wealth=wealth+1
				
	if(ragu==6):
		wealth=wealth+1
				
	if(wealth>0):
		result.append(["The native will be wealthy."])
	else:
		result.append(["The person will be poor."])
				



def happiness():
			
	global result
	happy=0
				
	if(moon==4):
		happy=happy+1
				
	if(kethu==8):
		if(is_benefic(8)):
			happy=happy+3
				
	if(sun==5):
		happy=happy+1
				
	if(saturn==2):
		happy=happy-1
				
	if(mercury==5):
		happy=happy+1
				
	if(jupiter==8):
		happy=happy-1
					
	if(happy<0):
		result.append(["The native will have an unhappy life."])
	else:
		result.append(["The native will be happy in life."])
			

#end of hema
def career():

	global result

	if(len(setp)==7 and setp[0]=="1" and setp[6]=="7"):
		result.append(["The person will be a ruler or higher government official."])
	if(len(setp)==4 or length_of_planets==4):
        	result.append(["The native will be pursue agriculture."])
	if(length_of_planets==6):
		result.append(["The person will be a protector of cattle."])
	if(ragu==10):
      		result.append(["The native will be a skilled artist and have a flair for poetry and litrature."])
 	if(saturn==10):
		result.append(["The native will become a ruler or a minister and will work for downtrodden masses."])          
	if(venus==10):
		result.append(["The native will earn through houses and buildings.He will become a skilled trader."])
	if(jupiter==10):
    		result.append(["The native can become a high official in the government.He will make a good head of academic and research institutions."])
   	if(mars==10):
        	result.append(["The native will be a skilled scientist or technician."])
	if(mercury==9):
		result.append(["The native will have a scientific mind and will acquire higher standards in education."])
   	if(jupiter==9):
          	result.append(["He will be an exponent of law, philosophy, etc."])
	if(sun==11):
  		result.append(["The native will get royal and governmental favours and achieve success without much effort."])
	if(moon==11):
		 result.append(["He will earn profits in business."])
	if(mercury==11):
           	result.append(["The native will be learned in many sciences.The native will prosper in engineering venturesult."])
      	elif(saturn==11):
      		result.append(["The native will be involved in politics, commanding great respect."])
  	if(ragu==11):
          	result.append(["The native will become a ruler or a minister and will work for downtrodden masses."])
        elif(jupiter==2):
     		result.append(["The native will make good poet or great writer or astrologer or even a scientist."])                    
	if(sun==6):
       		result.append(["The native will make a good politician."])
       	elif(moon==6):
    		result.append(["The nativr will have success as a caterer."])


def skills():
	
	global result

	skillflag=0	
	if(mercury==sun or (length_of_planets==7 and setp[4]=="5" and setp[6]=="12") ):
		result.append(["The person will be highly intelligent and extremely skilful."])
		skillflag=1
	if((next_pos(moon,1)!=sun and prev_pos(moon,1)!=sun and planet[prev_pos(sun,1)]!=[] and planet[next_pos(sun,1)]!=[]) or mars==11):
    		result.append(["The native will be an eloquent speaker."])
	if(mercury==11 or kethu==10):
		result.append(["The native will be keen, possess sharp intellect and truthful."])
		skillflag=1
     	elif(jupiter==11 or moon==10 or ragu==10):
		result.append(["The native will be bold and intelligent."])
		skillflag=1
      	if(venus==1):
    		result.append(["The native will be interested in art,music,drama and singing."])
    	if(saturn==1):
    		result.append(["The native maybe lazy."])
    	if(kethu==1):
    		result.append(["The native will have psychic powers."])
  	if(venus==4):
  		result.append(["The native will be well versed in music."])                
  	if(ragu==4 and skillflag!=1):
  		result.append(["The native will be foolish."])
		skillflag=-1
	if(mercury==7):
		result.append(["The native will have profound knowledge in law and will be skilled in business tactics and trade." ])        
       	if(jupiter==7 and skillflag!=-1):
      		result.append(["The native will have a  good education."])
		skillflag=1
    	if(saturn==7):
           	result.append(["The person will be diplomatic and enterprising."])
   	if(sun==7):
        	result.append(["The native will be fond of music."])
        if(mars==10 and skillflag!=-1):
        	result.append(["The native will be a skilled scientist or technician."])
      	if(mercury==10 and skillflag!=-1):
           	result.append(["The person will be a scholar and engaged in accquiring more knowledge and fame."])        
       	if(venus==10 and skillflag!=-1):
         	result.append(["The native will have healing powers."])
        if(ragu==10):
            	result.append(["The native will be a skilled artist and have a flair for poetry and litrature."])
      	if(venus==2 and skillflag!=-1):
         	result.append(["The native will be skilful ."])
		skillflag=1
       	if(kethu==2 and skillflag!=1):
      		result.append(["The native will be a bad speaker."])
  	if(jupiter==5 and skillflag!=-1):
         	result.append(["The native will be learned in logic with a great discriminating power."])



def family():

	global result

	fam=0
	fre=0
	if(planet[1]!=[] and planet[4]!=[] and planet[7]!=[] and planet[10]!=[]):
      		result.append(["The native will have good children."])
       	if(jupiter==0  and moon==7 and sun==next_pos(moon,8)):
		result.append(["The native will have royal blood."])
    	elif(len(setp)==5 or length_of_planets==5):
         	result.append(["The native will always be surrounded by friends and relatives."])
		fre=1
		fam=1 
     	if(moon==4):
          	result.append(["The native will derive happiness from relatives."])
		fam=1
       	if(venus==4):
        	result.append(["The native will be deeply attachment to mother."])
   	if(saturn==4 and (fam!=1 and fre!=1)):
            	result.append(["The native will lead a secluded life."])                    
		fre=-1
		fam=-1
    	if(ragu==4 and fre!=1):
          	result.append(["The native will have few friends."])
		fre=-1
     	if(sun==7 and fre!=1):   
            	result.append(["The native will have few friends and difficulty in getting along with people."])                                
		fre=1
	if(venus==7 and fre!=-1):
  		result.append(["The native will have successful partnerships."])
		fre=1
	if((moon==3 or sun==3) and fam!=-1):
      		result.append(["The native will be attached to children."])
		fam=1
       	if(mars==6 and fam!=1):
            	result.append(["The native will experience worries from near relatives."])
		fam=-1
      	if(mars==8 and fam!=1):
           	result.append(["The native will have few children","The native will hate their relatives."])
		fam=-1
	if(venus==2 or moon==2):
     		result.append(["The native will have large family."])
      	if(venus==3 and fam!=1):
           	result.append(["The native will have troubling children."])	
		fam=-1
        if(sun==9 and fam!=1):
          	result.append(["The native will have issues with father and family."])
		fam=-1
   	elif(mercury==9 and fam!=-1):
      		result.append(["The native will have friendly realtion with father and family."])
		fam=1
     	if(moon==9 and fam!=-1):
         	result.append(["He will have many children."])
		fam=1
	elif(saturn==11 and fre!=1):
          	result.append(["The native will have few friends."])



def marriage():

	global result

	mflag=0
	if(is_malefic(1) and venus==1):
 		result.append(["The native will have an unhappy marital life."])
		mflag=-1
      	if(sun==7):
        	result.append(["The person will have a delayed marriage."])
   	if(moon==7 or jupiter==7):
        	result.append(["The native will have a good looking spouse."])
      	if(saturn==7):
       		result.append(["The native will be under wife's control."])        
		mflag=-1
 	if(kethu==7):
          	result.append(["The native will not have a satisfactory marriage."])
		mflag=-1
        if(sun==3):
		result.append(["The native will be subordinate to wife."])
		mflag=-1
     	if(ragu==9):
       		result.append(["The native will have a nagging and domineering wife."])
		mflag=-1
      	if(kethu==9 and mflag!=-1):   
           	result.append(["Hs is gifted with good wife and children."])
	


#hardcodechart()
def result_gen(planet,result):

	print(planet)
	print(result)

	initialize(planet,"capricorn")
	result=[]
	globals().update(locals())
	
	character()
	fame()
	beauty()
	happiness()

	wealth()
	life()
	career()
	skills()

	marriage()
	family()

	return result
	

