"""
Implement a function to evaluate (a^b)%c
"""
def mod(a,b):
    return(((a%b)+b)%b)
def mul(a,b,c):
    return(mod(mod(a,c)*mod(b,c),c))

def power(a,b,c):
    ret=1
    if b==0:
        return(ret)
    elif b==1:
        return(mod(a,c))
    else:
        while(b):
            if b%2!=0:
                ret=mul(ret,a,c)
            a=mul(a,a,c)
            b//=2
        return(ret)


a,b,c=map(int,input().split())

print(power(a,b,c))