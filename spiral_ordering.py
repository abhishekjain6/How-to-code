"""
Given a square n*n matrix, print the elements as per
spiral ordering of the elements.
Input:
space separated integers n and m
n lines, with m space separated numbers

Output:
n*n integers
"""
from math import pi
arr=[]
n,m=map(int,input().split())
for x in range(n):
    arr.append(list(map(int,input().split())))
moves={1:[0,1],2:[1,0],3:[0,-1],4:[-1,0]}
cm=1
t,b,l,r=0,n-1,0,n-1
points_travelled=0
x,y=0,0
while(points_travelled<n*m):
    print(arr[y][x],end=" ")
    arr[y][x]=pi
    n_y=y+moves[cm][0]
    n_x=x+moves[cm][1]
    if n_x>=m or n_x<0 or n_y>=n or n_y<0 or arr[n_y][n_x]==pi:
        cm=(cm%4)+1
        n_y=y+moves[cm][0]
        n_x=x+moves[cm][1]
    x,y=n_x,n_y
    
    points_travelled+=1