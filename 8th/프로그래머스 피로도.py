from itertools import permutations

def solution(k, dungeons):
    or_k = k
    n = len(dungeons)
    maxi = 0

    for case in permutations(dungeons):  # 가능한 모든 경로
        for i in range(n):
            if k < case[i][0]:  # 현재피로도 < 최소피로도
                break

            k = k - case[i][1]
            count = i + 1

            if maxi < count:
                maxi = count

        k = or_k

    answer = maxi
    return answerp