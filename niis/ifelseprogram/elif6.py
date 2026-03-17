print("Enter two number:")
no1=int(input("first number:"))
no2=int(input("second number:"))
print("\nEnter an operator(+,-,*,//):")
op=int("operator:")
if op=="+":
	print("Result=",no1+no2)
elif op=="-":
	print("Result=",no1-no2)
elif op=="*":
	print("Result=",no1*no2)
elif op=="//":
	if no2!=0:
		print("Result=",no1//no2)
	else:
		print("Division by zero is not allowed.")
else:
	print("invalid operator")                   