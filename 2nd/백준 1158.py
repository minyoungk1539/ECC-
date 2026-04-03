import collections

N, K = map(int, input().split())  #N명의 사람, K씩 띄우면서 제거
q = collections.deque([])  #기존 사람들
p = collections.deque([])   #제거된 사람들
for i in range(1, N+1) : 
    q.append(i)  #q에 1~N 삽입


for l in range (1, N+1):
    q.rotate(-K)  #K씩 반시계방향 회전
    a = q.pop()  #해당 사람 제거
    p.append(a)  #새로운 덱인 p에 삽입

result = "<" + ", ".join(map(str, p)) + ">"
print(result)
    


        


