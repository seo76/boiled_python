"""
변수
배열 arr 배열 크기 a
질의 개수 q
x1 y1 x2 y2
"""
"""
a, q = map(int, input("배열 크기와 질의 개수를 공백으로 구분해 입력하시오.").split())

arr=[]
arr2=[[0 for l in range(a+1)]for m in range(a)]

print("배열 입력")
for i in range(a):
    #arr.append(0)
    temp=0
    arr.append(list(map(int,input().split())))
    for k in range(a):
        temp += arr[i][k]
        #print(temp)
        arr2[i][k+1]=temp
        #arr2.append(temp)

#print(arr2)



answer=[]
print("구간 입력")
for j in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans=0
    for n in range(x2-x1+1):
        an=arr2[x1-1+n][y2]-arr2[x1-1+n][y1-1]
        ans +=an
    answer.append(ans)

print(*answer,sep="\n")
"""

"""

        print("n",n,"a:",answer)
    if (x1 == x2):
        print(answer2/2)
    else:
        print(answer2)

    



if (x1 == x2):
        print(answer/2)
    else:
        print(answer)

    answer=(arr2[x1-1][y2]-arr2[x1-1][y1-1])
    answer=(arr2[x2-1][y2]-arr2[x2-1][y1-1])
print(arr2)

print(x1, y1, x2, y2)
print(arr)
print(arr[1][1])
"""


"""
변수
배열 arr 배열 크기 a
질의 개수 q
x1 y1 x2 y2
"""

a, q = map(int, input("배열 크기와 질의 개수를 공백으로 구분해 입력하시오.").split())

arr=[] #입력받을 배열
arr2=[[0 for l in range(a+1)]for m in range(a)] #합배열 크기선언(0으로 채움)

print("배열 입력")
for i in range(a):
    temp=0 #행 늘어날 때 마다 temp값 초기화
    arr.append(list(map(int,input().split())))
    for k in range(a):
        temp += arr[i][k]
        arr2[i][k+1]=temp #행별 수열 합 입력



answer=[]
print("구간 입력")
for j in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans=0
    for n in range(x2-x1+1):
        an=arr2[x1-1+n][y2]-arr2[x1-1+n][y1-1] #행 별 구간합
        ans +=an #행 별 구간합의 합
    answer.append(ans)

print(*answer,sep="\n")
