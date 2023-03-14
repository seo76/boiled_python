#최대값을 기준으로 평균 구하기 (백준 1546)

"""
점수 a1+a2+...aN더해서/최댓값M*100/점수개수N

과목 개수 n개..
리스트로 받아야겠네


"""



sum = 0

n=int(input("과목의 개수를 입력하시오"))


p=list(map(int, input("띄어쓰기로 구분하여 점수를 입력하시오\n").split()))
 
for i in range (n):
    sum=sum+p[i]


avg=sum/max(p)*100/n

print(avg)
"""

s=[]
s=list(input("@입력고").split("@",1))

for i in range (3):
    print(s[i])

"""
