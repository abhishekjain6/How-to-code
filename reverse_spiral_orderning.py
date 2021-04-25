"""
Given n*m integers, create a n*m matrix considering them to be of spiral 
ordering.
Input:
Integer n and m
n*m space separated integers
Output:
n*m matrix

"""
from math import pi
n,m=map(int,input().split())
arr=list(map(int,input().split()))
mat=[[pi for x in range (m)] for y in range(n)]
moves={1:[0,1],2:[1,0],3:[0,-1],4:[-1,0]}
cm=1
l=0
points_travelled=0
x,y=0,0
while(points_travelled<n*m):
    mat[y][x]=arr[l]
    n_y=y+moves[cm][0]
    n_x=x+moves[cm][1]
    if n_x>=m or n_x<0 or n_y>=n or n_y<0 or mat[n_y][n_x]!=pi:
        cm=(cm%4)+1
        n_y=y+moves[cm][0]
        n_x=x+moves[cm][1]
    x,y=n_x,n_y
    
    points_travelled+=1
    l+=1
for x in mat:
    print(x)