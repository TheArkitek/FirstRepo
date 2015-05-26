
class Game(object):
	def __init__(self, roadMap):
		self.roadMap = roadMap
	def play(self):
		currentRoom = self.roadMap.StartRoom()
		victoryRoom = self.roadMap.Victory()
		deathRoom = self.roadMap.Death()
		
		while currentRoom != victoryRoom or deathRoom:
			nextRoomName = currentRoom.start()
			currentRoom = self.roadMap.nextRoom(nextRoomName)
		currentRoom.start()

class Room(object):
	def start(self):
		print "Not a room"
		exit(1)


	
