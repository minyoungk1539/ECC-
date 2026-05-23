def solution(routes):
    cars = len(routes)
    inouts = []
    for i in range (cars):
        inout = range(routes[i][0], routes[i][1] + 1)
        inouts.append(inout)
    #지나가는 곳에 카운트를 시켜버릴까?
    answer = 0
    return answer