def solution(n, lost, reserve):
    both = []
    for i in range (1, n+1) :
        if i in reserve :  #여분있는 학생
            if i in lost :  #여분있는 학생이 도난 당함
                lost.remove(i)
                reserve.remove(i)
    for i in range(1, n+1) :   #lost와 reserve에 모두 있는 학생을 전부 lost와 reserve에서 모두 뺌
        if i in reserve : 
            if i not in lost :  #그 학생은 도난 x
                if i+1 in lost and i-1 in lost :  #앞뒤 학생 모두 도난
                    both.append(i)
                elif i+1 in lost : #뒷번호가 도난
                    lost.remove(i+1)
                    reserve.remove(i)
                elif i-1 in lost :  #앞번호가 도난
                    lost.remove(i-1)
                    reserve.remove(i)
                else : #앞 뒤 학생 모두 체육복있음
                    reserve.remove(i)
            


    for i in both :
        if i in reserve:
            if i-1 in lost :
                lost.remove(i-1)
                reserve.remove(i)

            elif i+1 in lost:
                lost.remove(i+1)
                reserve.remove(i)

            else:
                reserve.remove(i)
    lost_num = len(lost)
    answer = n - lost_num
    return answer
      

