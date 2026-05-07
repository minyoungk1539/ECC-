def solution(brown, yellow):
    pairs = []

    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            pairs.append((i, yellow // i))
    n = len(pairs)
    z = 0
    for l in range(n) :
        w = pairs[l][0]
        h = pairs[l][1]
        if brown == ( w + h ) * 2 + 4 :
            if w < h : #가로가 더 길게
                z = h
                h = w
                w = z
            answer = w + 2, h + 2
    return answer