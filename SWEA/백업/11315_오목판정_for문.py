# N*N 크기의 판, 돌이 가로/세로/대각선 중 하나의 방향으로 다섯개 이상 연속한 부분이 있는지 판정

def solve():
    # 가로 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[i][j] == 'o':
                cnt += 1
            if data[i][j] == '.' or j == N - 1:
                if cnt >= 5:
                    return 'YES'
                cnt = 0

    # 세로 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[j][i] == 'o':
                cnt += 1
            if data[j][i] == '.' or j == N - 1:
                if cnt >= 5:
                    return 'YES'
                cnt = 0

    # 좌상-우하 방향 대각선 찾기
    cnt = 0
    for k in range(-N+5, N-4):
        for i in range(N):
            for j in range(N):
                if i-j == k:
                    if data[i][j] == 'o':
                        cnt += 1
                    if data[i][j] == '.' or j == N - 1:
                        if cnt >= 5:
                            return 'YES'
                        cnt = 0

    # 우상-좌하 방향 대각선 찾기
    cnt = 0
    for k in range(-N+5, N-4):
        for i in range(N):
            for j in range(N):
                if i + j == N-1+k:
                    if data[i][j] == 'o':
                        cnt += 1
                    if data[i][j] == '.' or i == N - 1:
                        if cnt >= 5:
                            return 'YES'
                        cnt = 0

    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(N)]

    print(f'#{tc} {solve()}')
