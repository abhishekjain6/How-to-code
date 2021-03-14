"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example
q=[1,2,3,5,4,6,7,8]

If person 5 bribes person 4, the queue will look like this:1,2,3,5,4,6,7,8 . Only 1 bribe is required. Print 1.

q=[4,1,2,3]
Person 4 had to bribe 2 people to get to the current position. Print Too chaotic.


https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    flag=1
    for y in range(n):
        if l[y]-y-1>2:
            print("Too chaotic")
            flag=0
            break
        for j in range(max(l[y]-2,0),y):
            if l[j]>l[y]-1:
                c+=1
    if flag:
        print(c)