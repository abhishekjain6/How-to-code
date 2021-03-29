"""
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
"""
def goodness(s,n):
    st=[x for x in s]
    score=0
    for i in range(0,n//2):
        if st[i]!=st[-i-1]:
            score+=1
    return(score)
            
for t in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    k1=goodness(s,n)
    print("Case #"+ str(t+1)+": "+str(abs(k-k1)))