def sical():
    print("enter principle")
    p=float(input())
    print("enter rate of interest")
    r=float(input())
    print("enter time")
    t=float(input())
    si=p*t*r/100
    return si
res=sical()
print("simple interest=",res)