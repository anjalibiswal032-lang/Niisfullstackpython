class voterError(BaseException):
	def __init__(self):
		super().__init__()
print("enter a age")
age=int(input())
if age>=18:
   print("eligbal")
else:
   raise voterError("age not allow")
print("main end")      		