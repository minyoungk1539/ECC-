def solution(people, limit):
    people.sort()  #몸무게 적은 순으로 정렬
    count = 0

    left = 0
    right = len(people) - 1  #가장 몸무게가 큰 사람의 인덱스

    while left <= right:
        org_limit = limit

        org_limit -= people[right]
        right -= 1

        if left <= right and people[left] <= org_limit:
            org_limit -= people[left]
            left += 1

        count += 1

    return count