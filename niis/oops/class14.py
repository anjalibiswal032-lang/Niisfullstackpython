class person:
	def display_person(self):
		print("class person")

class student(person):
	def display_student(self):
		print("class student")

class Engineering(student):
    def display_Engineering(self):
    	print("class Engineering")
e=Engineering()
e.display_person()
e.display_student()
e.display_Engineering()    	


