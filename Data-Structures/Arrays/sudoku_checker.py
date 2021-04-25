"""
Given a 9x9 grid of numbers, all of which are in the inclusive
range of 1 to 9, check if the grid satisfies the constraints of
a correct sudoku puzzle.

"""
def row(arr):
    for y in range(9):
        mp={x:1 for x in range(1,10)}
        for x in arr[y]:
            if mp[x]==0:
                return(False)
            else:
                mp[x]=0
    return(True)
def col(arr):
    for y in range(9):
        mp={x:1 for x in range(1,10)}
        for x in range(9):
            if mp[arr[x][y]]==0:
                return(False)
            else:
                mp[arr[x][y]]=0
    return(True)
def grid(arr):
    i,j=0,0
    while True:
        i=0
        while i<9:
            mp={x:1 for x in range(1,10)}
            for y in range(j,j+3):
                for x in range(i,i+3):
                    if mp[arr[y][x]]==0:
                        return(False)
                    else:
                        mp[arr[y][x]]=0
            i+=3

        j+=3
        if j>=9:
            break

    return(True)
        
            
arr=[]
for x in range(9):
    arr.append(list(map(int,input().split())))
if row(arr) and col(arr) and grid(arr):
    print("Yes")
else:
    print("No")