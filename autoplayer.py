#I'm tired of staying in the same place. I will move foward. I won't blame my parents. I won't blame my enviroment. I will manage my 
#emotions. I can't stay here anymore. I'm sick with being stuck. Why can't I keep moving? I must make something

dialspace = '**********************************************'
class CreateCharacter(object):
	def _init_(self, side, gender, cclass, cname):
		self.side = side
		self.gender = gender
		self.cclass = cclass
		self.cname = cname	
		
def userside(y):
	if y == 1:
		print (dialspace)
		print ('You need to choose a side. There is a war in Joes World. Politics are sensitive and everyone will ask what side'
		   	' you are on. I know sucks right? You can choose the 1. Arathi Kingdom or 2. the Warsong Clan.')
		factions = {1: 'Arathi Kingdom', 2: 'Warsong Clan'}
		print (' ')
		theside =  factions[int(input('Please choose a side by entering either 1 or 2 please: '))]
		return theside
def usergender(z):
	if z == 1:
		print (dialspace)
		print ('Next step, are you a 1. male or 2. female ? ')
		thegenders = {1: 'male',2: 'female'}
		print (' ')
		gender = thegenders[int(input('Pick a gender with either 1 or 2: '))]
		return gender
def usercclass(xx):
	if xx == 1:
		print (dialspace)
		print ('Almost there, this is an important decision. This is how your experience with Joes World will be affected. There'
		  	' are four choices. 1. Warrior 2. Sellsword 3. Wizard and 4. Priest')
		classes = {1: 'Warrior', 2: 'Sellsword', 3: 'Wizard', 4: 'Priest',}
		print (' ')
		theclass = classes[int(input('Pick a class with either 1, 2, 3, or 4: '))]
		return theclass
def usercname(yy):
	if yy == 1:
		print (dialspace)
		print ('Great this is the last part. Thanks again for joining Joes World. I would just like to know your name now please.')
		print (' ')
		thename = input('My name is: ')
		return thename


mySide = userside(1)
myGender = usergender(1)
myClass = usercclass(1)
myName = usercname(1)

'''myCharacter = CreateCharacter(mySide, myGender, myClass, myName)'''

def JoesWorldShortStory(zzz):
	if zzz == 1:
		print (dialspace)
		print ('The world was at peace. Seasons and festivals passed in harmony. Then the Dredgers came from the shadows of '
			'society. They executed as many leaders as was possible and plunged the; religious, political, economical, and culteral '
			'worlds into dismay.')
		print (dialspace)
		continuu = input('Press enter to continue:')
		print (dialspace)
		print ('Society must repair itself again. Right now it is torn in two. There is the Arathi Kingdom and the Warsong Clan')
		print (' ')
		print ('The Arathi Kingdom is a society bound by traditions and order. It is mostly religious and ruled by rules. It was formed'
			' by Prime Minister Jakhob Vandervort')
		print (' ')
		print ('The Warsong Clan came out of brute strength and admiration for strength. While the Warsong Clan seems more primal'
			' in its ways, it holds Honor in high regard. It is tied by clans, groups, and etc. It is all banded together by the'
			' Warchief Alexander Thenn')
		print (dialspace)
		continuu = input('Press enter to continue:')
		print (dialspace)
		print ('You have chosen The ' + str(mySide) + ' as a ' + str(myGender) + ' ' + str(myClass) + '.' + ' Your name is ' + str(myName) + '.') 
	
myIntro = JoesWorldShortStory(1)
		
