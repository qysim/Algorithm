# 맨 처음엔 A로만 이루어져 있음, 세글자인 경우 AAA, 네글자인 경우 AAAA


def solution(name):
    answer = 0

    n = len(name)   # 문자열 길이

    for i in range(n):
        # 알파벳 만들기
        if ord(name[i]) <= 78:
            answer += (ord(name[i])-ord('A'))
        else:
            answer += 26 - (ord(name[i])-ord('A'))

    idx = 0  # 현재 커서 위치
    length = 0
    while True:
        right = 0
        left = 0

        # 오른쪽으로 이동
        for i in range(idx, n):
            if name[i] == 'A':
                break
            else:
                right += 1

        # 왼쪽으로 이동
        for i in range(n-1, 0, -1):
            if name[i] == 'A':
                break
            else:
                left += 1

        length += min(left, right)

    answer += length
    print(answer)
    return answer


# print(ord('A'))  # 65
# print(ord('N'))  # 78
# print(ord('Z'))  # 90

solution("BBBBAAAABA")
