"""
Given the decimal number for a particular mask, check if the ith bit is set, set and unset the ith and jth bit.
"""
def checkbit(mask,i):
    return(mask&(1<<i))
def setbit(mask,i):
    return(mask|(1<<i))
def rembit(mask,i):
    return(mask&~(1<<i))
i=0
j=1
mask=38
print(bin(mask).lstrip("0b"))
newbit=checkbit(mask,i)
if newbit:
    print("The bit number "+str(i)+" is set")
else:
    print("The bit number "+str(i)+" is not set")
newbit=setbit(mask,i)
print("After setting the bit number "+str(i)+": "+bin(newbit).lstrip("0b"))
newbit1=rembit(newbit,j)
print("After unsetiing the bit  number "+ str(j)+": "+bin(newbit1).lstrip("0b"))