import collections

N = map(int, input())
q = collections.deque([])
    
for i in range(1, N+1) : 
    q.append(i)  #q에 1~N 삽입


for l in range (1, N+1):
    K = q.pop()
    q.rotate(K)

result = "<" + ", ".join(map(str, p)) + ">"
print(result)5
    