import collections

N, M = map(int, input().split())  #N개의 원소 중 M개 뽑기
ls = list(map(int, input().split()))  #뽑기를 원하는 원소의 위치
count = 0
q = collections.deque(range(1, N+1)) #사실상 첫 위치 = 요소



for i in ls :
    mid = len(q)//2   #가운뎃값 위치(10개가 있을 경우 5)
    idx = q.index(i)  #i가 속해있는 위치(맨 앞에 있으면 0)
    if len(q) == 0 :  #비어있으면 break
        break
    if i == q[0] : #왼쪽 끝
        q.popleft()
        continue
        
    if idx > mid :  #중앙보다 인덱스가 클 경우 시계회전
        while i != q[0] :
            q.rotate(1)
            count += 1 #카운트 증가

        q.popleft()
    else :  #중앙보다 작을 경우 반시계회전
        while i != q[0] : 
            q.rotate(-1)
            count += 1 #카운트 증가
        q.popleft()

print(count)