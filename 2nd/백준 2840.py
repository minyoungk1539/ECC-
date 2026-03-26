import collections


N, K = map(int, input().split())
q = collections.deque([]) #입력 저장용 덱
p = collections.deque(range(1, N+1)) #바퀴 일단 숫자로 채움


for i in range (1, K+1) :
    items = input().split()  #입력값
    number = int(items[0])   #화살표가 가리키는 글자 변화 수
    Text = str(items[1])   #회전 이후 가리키는 글자
    set = (number, Text)  #입력 세트
    q.append(set)


for l in range (0, K) : #K세트
    S = q.popleft()    #pop
    p.rotate(S[0])   #글자 변화수(number)만큼 회전
    if p[0] != S[1] and type(p[0]) != int :  #숫자도 아니고 같은 알파벳도 아님
        p.clear()   #덱 비우기
        print('!')  #! 출력
        break
    if p[0] != S[1] and S[1] in p:
        p.clear()
        print('!')
        break
    else : 
        p.popleft()  #기존에 있던 숫자 빼고
        p.appendleft(S[1])   #알파벳 넣기
        
for k in range(1, N+1) :  #바퀴의 칸 개수
    if len(p) == 0 :   #덱에 아무것도 없으면 ! 상태
        break
    p.rotate(1)  #한 칸 회전
    if type(p[0]) == str :  #알파벳이 있다면 넘어가기
        continue  
    else : 
        p.popleft()   #알파벳이 없다면 숫자가 있으니 pop
        p.appendleft('?')   #그 자리에 ? 채우기

if len(p) == 0 :
    pass 
else : print(''.join(p))
#회전->해당자리 비었는지 검사->비었으면 삽입->안비었으면 return ! -> 최종 빈자리 ?