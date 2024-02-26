from collections import deque
from copy import deepcopy


def comb(idx, cnt):
    if cnt == 3:
        bfs()
        return

    if idx == len(walls):
        return

    r, c = walls[idx]
    maps[r][c] = 1
    comb(idx+1, cnt+1)
    maps[r][c] = 0
    comb(idx+1, cnt)


def bfs():
    global area
    map_tmp = deepcopy(maps)

    queue = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < M and not map_tmp[nr][nc]:
                map_tmp[nr][nc] = 2
                queue.append((nr, nc))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_tmp[i][j] == 0:
                cnt += 1
    if cnt > area:
        area = cnt


# 연구소 크기 N*M
N, M = map(int, input().split())
# 0: 빈칸, 1: 벽, 2: 바이러스
maps = [list(map(int, input().split())) for _ in range(N)]

# 바이러스는 상하좌우로 인접한 빈칸으로 퍼져나간다 -> delta
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 벽을 세울 수 있는 후보 다 찾기
walls = deque()
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            walls.append((i, j))

# 벽을 3개 세우고 bfs로 갈 수 있는 곳은 다 2로 바꾼다
# 남은 0의 개수를 센다
area = 0
comb(0, 0)

# 안전영역은 벽 세우고 바이러스 퍼지고 난 후 0의 개수
# 안전영역의 최대 크기 출력
print(area)
