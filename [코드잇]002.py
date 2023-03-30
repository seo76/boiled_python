
a, b= map(int,input().split())

arr = [[0]*b for _ in range (a)]

n = int(input())

for _ in range(n):
    l, d, x, y=map(int, input().split())
    x=x-1
    y=y-1
    if (d==1):#세로
        for i in range(l):
            arr[x+i][y]=1
    else:
        for j in range(l):
            arr[x][y+j]=1

for line in arr:
    print(*line)


"""
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

"""
