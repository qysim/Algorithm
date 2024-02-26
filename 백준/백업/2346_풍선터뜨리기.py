from collections import deque
# 1번 부터 N번까지 N개의 풍선이 원형으로 놓임
# N번 다음 1번으로 이어짐
# 풍선 안 종이에는 -N <= 정수 <= N, 0은 없음
# 처음은 1번 풍선 터트림
# 풍선 안 종이에 적힌 숫자만큼 이동하여 풍선 터트림
# 양수 오른쪽, 음수 왼쪽
# 이미 터진 풍선은 빼고 이동

N = int(input())
ballon = list(map(int, input().split()))

idx = 0
while ballon:
    # 터트린 풍선 출력
    tmp = ballon[idx]
    print(idx+1, end=' ')
    # 이동할 거리
    if tmp > 0:
        idx = (tmp-1) % N
    else:
        idx = (N - tmp + 1) % N