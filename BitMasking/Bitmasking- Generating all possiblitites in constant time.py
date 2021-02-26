"""
Given a set of numbers til N ([1,2,3,4.......N-1,N]), use BitMasking to generate all possible subsets.
Write functions to show all subsets, with O(1) memory complexity.

"""
def show(n):
    a=1
    for x in (bin(n).lstrip("0b"))[::-1]:
        if x=="1":
            print(a,end=" ")
        a+=1
    print("")
N=17 ## array =[1,2,3....16,17], change if you wish

#For N, we will need a binary number of max length l=N

a=int("1"*N,2)#This number a contains all possible subsets
for y in range(a+1):
    show(y)


