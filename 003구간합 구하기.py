
"""
리스트 l, m
l=배열
l2=합 배열
"""
"""



l2=[]
temp=[]

n, m=map(int, input("수의 개수와 질의 개수를 공백으로 구분해 입력하시오(1<=n<=100,000)").split())
l=list(map(int,input("공백으로 구분해 수를 입력하시오").split()))
l2.append(l[0])
for h in range(1, n):
    l2.append(l2[h-1]+l[h])
    print(l2)

for k in range(m):
    i, j=map(int, input("구간합을 구할 i번째부터 j번째 수를 공백을 두고 입력하시오").split())
    if (i-2<0):
        l2[i-2]=[0]

    temp.append(l2[j-1]-l2[i-2])

for o in range(m):
    print(temp[o])



"""
#구간 합 구하기
"""
수의 개수 N개, 질의 개수 M개
주어진 수의 배열의 i번째 수 부터 j번째 수 까지의 구간 합 구하기
"""

"""
l2=[]
temp=0
ans=[]

n, m=map(int, input("수의 개수와 질의 개수를 공백으로 구분해 입력하시오(1<=n<=100,000)").split())
l=list(map(int,input("공백으로 구분해 수를 입력하시오").split()))


l2.append(temp) #값을 제대로 받기 위해 0 추가

for t in range(n):
    temp += l[t] #리스트 l의 1부터 n번까지 수열의 합 구하기 
    l2.append(temp) #고대로 리스트 l2에 입력

print("구간합을 구할 i번째부터 j번째 수를 공백을 두고 입력하시오")

for q in range(m):
    i, j=map(int, input().split())
    ans.append(l2[j]-l2[i-1]) #구간 합 공식 사용
    
print(*ans,sep='\n') #*을 인 앞에 붙여 언패킹, sep을 통해 엔터로 분리

"""
"""

#구간 합 구하기 2

a, q=map(int, input("배열의 크기와 질의 개수를 공백으로 구분해 입력하시오").split())

arr=[]

print("배열을 입력하시오")

for i in range(a):
    arr,append(list(map(int,input().split())))

print(arr)


"""
import sys
input = sys.stdin.readline

l2=[]
temp=0
ans=[]

n, m=map(int, input().split())
l=list(map(int,input().split()))


l2.append(temp)

for t in range(n):
    temp += l[t]
    l2.append(temp)

for q in range(m):
    i, j=map(int, input().split())
    ans.append(l2[j]-l2[i-1])

print(*ans,sep='\n')









