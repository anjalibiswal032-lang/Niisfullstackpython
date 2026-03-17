#try except finally

print("main start")
L=[10,20,30]
try:
	print(L[2]//2)
except:
    print("handling all exception")
finally:
    print("must execute")
print("main end")        	