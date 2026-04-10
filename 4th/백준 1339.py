import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

weight = {}

# 각 알파벳의 자리수 가중치 계산
for word in words:
    length = len(word)
    for i in range(length):
        ch = word[i]
        weight[ch] = weight.get(ch, 0) + 10 ** (length - i - 1)

# 가중치 기준으로 내림차순 정렬
sorted_weights = sorted(weight.values(), reverse=True)

digit = 9
result = 0

# 큰 가중치부터 큰 숫자 배정
for w in sorted_weights:
    result += w * digit
    digit -= 1

print(result)