def solution(triangle):
    # 두 번째 줄부터 시작
    for i in range(1, len(triangle)):
        for k in range(len(triangle[i])):

            # 왼쪽 끝: 바로 위 값만 올 수 있음
            if k == 0:
                triangle[i][k] += triangle[i - 1][k]

            # 오른쪽 끝: 왼쪽 위 값만 올 수 있음
            elif k == i:
                triangle[i][k] += triangle[i - 1][k - 1]

            # 가운데: 왼쪽 위와 바로 위 중 큰 값 선택
            else:
                triangle[i][k] += max(
                    triangle[i - 1][k - 1],
                    triangle[i - 1][k]
                )

    return max(triangle[-1])