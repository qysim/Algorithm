def bfs(start):
    global ans

    # 가로 또는 세로 방향으로 연결 -> 델타
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    visited = [[0] * N for _ in range(N)]
    queue = [start]
    r, c = start
    visited[r][c] = 1
    flag = True

    while queue:
        r, c = queue.pop(0)

        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 높은 지형에서 낮은 지형으로 -> 현재값보다 이동한값이 작아야함
                if visited[nr][nc] < visited[r][c]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                # 딱 한 곳을 정해서 **최대** K 깊이만큼 지형을 깎을 수 있다
                # 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.
                else:
                    if flag:
                        maps[nr][nc] -= K


    for i in range(N):
        for j in range(N):
            ans = max(ans, visited[i][j])


T = int(input())
for tc in range(1, T+1):
    # N: 지도 한 변의 길이, K: 최대 공사 가능 깊이
    N, K = map(int, input().split())
    # 배열 안의 숫자는 지형의 높이
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 등산로는 가장 높은 봉우리에서 시작 -> 배열 탐색해서 가장 높은 값 찾기
    max_v = 0
    for i in range(N):
        for j in range(N):
            max_v = max(maps[i][j], max_v)

    ans = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_v:
                bfs((i, j))

    # 가장 긴 등산로의 길이 출력
    print(f'#{tc} {ans}')
