def solution(routes):
    cars = len(routes)
    inouts = []
    for i in range (cars):
        inout = range(routes[i][0], routes[i][1] + 1)
        inouts.append(inout)
    #지나가는 곳에 카운트를 시켜버릴까?
    #2차원 배열을 만들어서 onehot encoding 마냥 해볼까
    #쭉 스캔해서 mix와 max를 찾고 min-max x len의 배열 생성 -> 지나가면 1로 변환 -> (합계 봐서 가장 높은 것 체크 -> 해당된 루트 지우기) -> 반복 
    answer = 0
    return answer