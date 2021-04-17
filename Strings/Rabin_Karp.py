"""
Find the first occurence of a substring in a given substring of alphabets, 
Input:
string
substring
Output:
index of starting position
"""
n=input()
m=input()
ln=len(n)
lm=len(m)
h={chr(x):x-96 for x in range(97,97+26)}
check=0
for x in range(lm):
    check+=h[m[x]]*26**(lm-1-x)
for x in range(0,ln-lm+1):
    to_check=0
    p=0
    for y in range(x,x+lm):
        to_check+=h[n[y]]*26**(lm-1-p)

        p+=1
    if to_check==check:
        if n[x:x+lm]==m:
            print(x+1)
            break


