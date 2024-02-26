def pinball(start, d):
    global max_v

    cnt = 0  # 점수
    r, c = start

    while True:
        r, c = r + delta[d][0], c + delta[d][1]

        if 0 <= r < N and 0 <= c < N:
            # 핀볼이 출발위치로 돌아오거나, 블랙홀에 빠질 때 끝남
            if (r, c) == start or board[r][c] == -1:
                if cnt > max_v:
                    max_v = cnt
                return

            # 점수는 벽이나 블록에 부딪힌 횟수 (웜홀 제외)
            if 1 <= board[r][c] <= 5:
                cnt += 1
                d = direc[board[r][c]][d]

            # 웜홀에 빠지면 같은 번호를 가진 웜홀로 빠져나오고 진행방향 유지
            elif 6 <= board[r][c] <= 10:
                for k in range(len(wormhole)):
                    if board[r][c] == wormhole[k][0] and (r, c) != (wormhole[k][1], wormhole[k][2]):
                        r = wormhole[k][1]
                        c = wormhole[k][2]
                        break
                        # break가 필요한 이유 : r, c 재할당 받고 나서 남은 for문이 돌아가면 
                        # (r,c) != ~ 이 부분에 해당되는 경우가 생김 그래서 무한루프에 빠짐
                        # 그래서 내가 찾아야할 r, c를 찾고 break로 for문을 끝내줘야함

        else:   # 벽을 만나면 반대방향으로 돌아온다
            cnt += 1
            d = direc[5][d]


# 상하좌우 델타
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 블록을 만난 후 진행하는 방향의 델타 배열 인덱스
direc = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 게임판 크기, 5 <= N <= 100
    # 블록은 1~5, 웜홀은 6~10, 블랙홀은 -1
    board = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    
    # 웜홀을 리스트로 구현했는데 딕셔너리로 구현하면 더 편할 것 같음!
    wormhole = []
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                wormhole.append([board[i][j], i, j])
    # print(wormhole)
    # [[7, 0, 8], [6, 4, 8], [7, 7, 6], [6, 9, 2]]

    for i in range(N):
        for j in range(N):
            if not board[i][j]:  # 출발점은 0인 곳만 가능
                for d in range(4):  # 핀볼은 상하좌우 중 한방향으로 움직임
                    start = (i, j)
                    pinball(start, d)

    print(f'#{tc} {max_v}')
