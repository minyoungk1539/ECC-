import collections

N, K = map(int, input().split())
q = collections.deque([])
p = collections.deque([])    
for i in range(1, N+1) : 
    q.append(i)  #q에 1~N 삽입


for l in range (1, N+1):
    q.rotate(-K)
    a = q.pop()
    p.append(a)

result = "<" + ", ".join(map(str, p)) + ">"
print(result)
    


        


