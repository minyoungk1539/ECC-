def find_fake_coin(coins):
    """
    coins: 동전 무게 리스트
           정상 동전은 모두 같은 무게
           위조 동전은 하나이며 정상보다 무겁거나 가벼움
    """

    def weigh(left, right):
        left_sum = sum(coins[i] for i in left)
        right_sum = sum(coins[i] for i in right)

        if left_sum > right_sum:
            return "left"
        elif left_sum < right_sum:
            return "right"
        else:
            return "equal"

    # 1차: 4개씩 나누기
    A = [0, 1, 2, 3]
    B = [4, 5, 6, 7]
    C = [8, 9, 10, 11]

    result1 = weigh(A, B)

    candidates = []

    if result1 == "equal":
        # 위조 동전은 C에 있음
        # A, B는 정상 동전
        normal = 0

        # 2차: C 중 3개와 정상 동전 3개 비교
        result2 = weigh([8, 9, 10], [normal, normal, normal])

        if result2 == "equal":
            # 12번 동전이 위조
            fake = 11
            result3 = weigh([fake], [normal])
            if result3 == "left":
                return fake + 1, "heavy"
            else:
                return fake + 1, "light"

        elif result2 == "left":
            # 9,10,11 중 하나가 무거움
            result3 = weigh([8], [9])
            if result3 == "left":
                return 9, "heavy"
            elif result3 == "right":
                return 10, "heavy"
            else:
                return 11, "heavy"

        else:
            # 9,10,11 중 하나가 가벼움
            result3 = weigh([8], [9])
            if result3 == "left":
                return 10, "light"
            elif result3 == "right":
                return 9, "light"
            else:
                return 11, "light"

    else:
        # A가 무겁거나 B가 무거운 경우
        # 보기 편하게 heavy_group, light_group으로 정리
        if result1 == "left":
            heavy_group = A
            light_group = B
        else:
            heavy_group = B
            light_group = A

        normal = 8  # C 그룹은 정상 동전

        # 2차
        result2 = weigh(
            [heavy_group[0], heavy_group[1], light_group[0]],
            [heavy_group[2], heavy_group[3], light_group[1]]
        )

        if result2 == "equal":
            # 남은 light_group[2], light_group[3] 중 하나가 가벼움
            result3 = weigh([light_group[2]], [light_group[3]])

            if result3 == "left":
                return light_group[3] + 1, "light"
            else:
                return light_group[2] + 1, "light"

        elif result2 == "left":
            # heavy_group[0], heavy_group[1] 중 하나가 무겁거나
            # light_group[1]이 가벼움
            result3 = weigh([heavy_group[0]], [heavy_group[1]])

            if result3 == "left":
                return heavy_group[0] + 1, "heavy"
            elif result3 == "right":
                return heavy_group[1] + 1, "heavy"
            else:
                return light_group[1] + 1, "light"

        else:
            # heavy_group[2], heavy_group[3] 중 하나가 무겁거나
            # light_group[0]이 가벼움
            result3 = weigh([heavy_group[2]], [heavy_group[3]])

            if result3 == "left":
                return heavy_group[2] + 1, "heavy"
            elif result3 == "right":
                return heavy_group[3] + 1, "heavy"
            else:
                return light_group[0] + 1, "light"


# 예시: 7번 동전이 무거운 경우
coins = [10] * 12
coins[6] = 11

fake_coin, state = find_fake_coin(coins)

print("위조 동전:", fake_coin)
print("상태:", state)