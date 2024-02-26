# 오목판정_델타버전

# 우, 우하, 하, 좌하
# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     check = 0   # 오목인지 아닌지 판별하는 변수
#
#     # 오목판 전체를 순회하면서
#     for i in range(N):
#         for j in range(N):
#             # 돌이 있으면
#             if arr[i][j] == 'o':
#                 # 우, 우하, 하, 좌하 방향을 탐색
#                 for k in range(4):
#                     cnt = 1
#                     ni = i + di[k]
#                     nj = j + dj[k]
#                     # 다음 돌이 놓여있고 오목판 범위 안이면 계속 탐색
#                     while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
#                         cnt += 1
#                         ni += di[k]
#                         nj += dj[k]
#                     # if cnt == 5:  # 이 조건으로 돌려도 pass함
#                     if cnt >= 5:    # 돌이 5개 이상이면
#                         check = 1   # 오목임
#     if check == 1:
#         print(f'#{tc}', 'YES')
#     else:
#         print(f'#{tc}', 'NO')

#####################################################################################
# 오목판정_델타버전_함수이용
def solve():
    # 오목판 전체를 순회하면서
    for i in range(N):
        for j in range(N):
            # 돌이 있으면
            if arr[i][j] == 'o':
                # 우, 우하, 하, 좌하 방향을 탐색
                for k in range(4):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 다음 돌이 놓여있고 오목판 범위 안이면 계속 탐색
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                    if cnt >= 5:  # 돌이 5개 이상이면
                        return 'YES'  # 오목임
    return 'NO'


# 우, 우하, 하, 좌하
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc} {solve()}')
