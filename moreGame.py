from sys import exit
from myGame import *

class StartRoom(Room):
	def start(self):
		print "Hello you worthless maggot. Welcome to the training simulator!"
		print
		print "We shall begin by moving into the room. What would you like to do?"
		print
		print "1. Enter the Room"
		print "2. Run away. Quit Training"
		print 
		action = raw_input("> ")
		
		if action == '1':
			print "Onward we go! GET MOVING MAGGOT"
			return 'robot'
		else:
			print "MAGGOT! GET BACK HERE AND FINISH YOUR TRAINING"
			exit(0)

class RobotRoom(Room):
	def start(self):
		print "Alright Maggot, for your first part of training you have to get past this robot."
		print "Use whatever means you need to, but you need to advance to the next room."
		print
		print "What will you do?"
		print
		print "1. Attack the robot"
		print "2. Try to sneak past"
		print "3. Scream loudly"
		action = raw_input("> ")
		
		if action == '1':
			roll = randint(1, 10)
			
			if roll < 5:
				print "You attack the robot, but I don't think this is going to work"
				return 'death'
			else:
				print "Good work maggot! You destroyed the robot. You ain't half bad at this"
				return 'boss'
		elif action == '2':
			roll = randint(1, 10)
			
			if roll < 5:
				print "You lazily try sneaking past the robot"
				return 'death'
			else:
				print "That was pretty sneaky, maggot! I'm not even sure I would have noticed you!"
				return 'boss'
		else:
			print "You start yelling uncontrollably"
			return 'death'
	
class BossRoom():
	def start(self):
		print "Alright Maggot, you got past the robot, bu let's see how you do against the boss. This guy is tough"
		print "Again use whatever means necessary. Just get to the next room"
		print
		print
		print "What will you do?"
		print
		print "1. Attack the boss!"
		print "2. Sneak around the boss"
		print "3. Run away."
	
		action = raw_input("> ")
	
		if action == '1':
			roll = randint(1, 10)
			
			if roll < 5:
				print "You attack the boss, but I don't think this is going to work"
				return 'death'
			else:
				print "Good work maggot! You defeated the boss! You ain't half bad at this"
				return 'victory'
		elif action == '2':
			roll = randint(1, 10)
			
			if roll < 5:
				print "You lazily try sneaking past the boss"
				return 'death'
			else:
				print "That was pretty sneaky, maggot! I'm not even sure I would have noticed you!"
				return 'victory'
		else:
			print "You start yelling uncontrollably"
			return 'death'
	
class Death(Room):
	def start(self):
		print "You're dead maggot! And you got blood all over the place! God damn it, it took weeks to clean up the last recruits mess!"
		exit(0)
		
class Victory(Room):
	def start(self):
		print "Great work maggot! You're still alive! That's more than i can say for most people who go through."
		print "Come on up, we'll go have a beer. You've earned it."
		exit(0)

class Map(object):
	
	rooms = {
		'start': StartRoom(),
		'robot': RobotRoom(),
		'boss': BossRoom(),
		'death': Death(),
		'victory': Victory()
	}
	
	def __init__(self, beginRoom):
		self.beginRoom = beginRoom
	def nextRoom(self, roomName):
		roomType = Map.rooms.get(roomName)
		return roomType
	def startRoom(self):
		return self.nextRoom(self.beginRoom)

		
aRoad = Map('start')
aGame = Game(aRoad)
aGame.play()
	
