from abc import *
class vehicle(ABC):
	@abstractmethod
	def start(self):
		pass
class car(vehicle):
    def start(self):
      print("car starts with a key")
v=car()
v.start()      		