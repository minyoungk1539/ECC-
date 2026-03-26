import collections

N = int(input())
ls = list(map(int, input().split()))  #풍선 속 쪽지
q = collections.deque([]) #input으로 받은 요소 저장
p = collections.deque([]) #결과용 덱

for num in range (0, N) :
    bal = (num+1, ls[num])
    q.append(bal) #풍선번호와 쪽지를 짝지어 저장


while q:
    if len(q) == 0 : break
    else :
        K = q.popleft() #왼쪽에 있는 요소 pop
        p.append(K[0])  #터트린 풍선 번호 삽입
        if K[1] > 0:
            q.rotate(-(K[1] - 1))  #양수라면 더 회전
        else:
            q.rotate(-K[1])  #음수라면 그냥
        
     
print(*p)  #터트린 풍선순으로 번호 출력