"""
Implement RLE for a string, encoding and decoding part.
input:
String, number
number:0/1
0 for encoding
1 for decoding

Output:
encoded/decoded string

Ex:
Input:aaaabcccaa 0
Output: 4a1b3c2a

Input: 3e4f2e 1
Output: eeeffffee
"""


def enc(s):
    cnt=0
    p=s[0]
    ans=[]
    for x in range(len(s)):
        if x==len(s)-1:
            if s[x]==p:
                cnt+=1
                ans.append(str(cnt))
                ans.append(p)
            else:
                ans.append(str(cnt))
                ans.append(p)
                cnt=1
                ans.append(str(cnt))
                ans.append(s[-1])
        else:
            if s[x]==p:
                cnt+=1
            else:
                ans.append(str(cnt))
                ans.append(p)
                p=s[x]
                cnt=1
    print("".join(ans))
        
def dec(s):
    ans=[]
    d=0
    for x in range(0,len(s)-1,2):
        for y in range(int(s[x])):
            ans.append(s[x+1])
    print("".join(ans))
        

a,b=input().split()
if b=="1":
    dec(a)
else:
    enc(a)