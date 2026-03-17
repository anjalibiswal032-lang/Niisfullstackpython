print("main start")

try:
	raise IndexError("hi")
except IndexError as e:
    print(e)
print("main end")    	