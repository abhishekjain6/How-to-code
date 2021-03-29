"""
https://www.codechef.com/MARCH21B/problems/PAPARAZI
"""

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==2:
        print(1)
    else:
        
        arr1=[]
        for i in range(n):
            arr1.append([i+1,arr[i]])
        arr2=[arr1[0],arr1[1]]
        ans=1
        l=len(arr2)
        for i in range(2,n):
            while len(arr2)>=2:
                s1=(arr2[l-1][1]-arr2[l-2][1])/(arr2[l-1][0]-arr2[l-2][0])
                s2=(arr1[i][1]-arr2[l-1][1])/(arr1[i][0]-arr2[l-1][0])
                if s1<=s2:
                    arr2.pop(-1)
                    l-=1
                else:
                    break
            arr2.append(arr1[i])
            l+=1
            ans=max(ans,arr2[l-1][0]-arr2[l-2][0])
        print(ans)



    