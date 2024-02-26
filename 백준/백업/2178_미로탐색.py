# N*M 크기 배열, 1은 이동가능, 0은 이동불가능
# (1,1)에서 출발, (N,M)으로 이동할 때 지나야하는 최소의 칸수 출력
# 서로 인접한 칸으로만 이동가능, 시작점,도착점도 칸수에 포함

from collections import deque


def dfs(r, c, cnt):
    global min_cnt

    if r == N-1 and c == M-1:
        min_cnt = min(min_cnt, cnt)
        return

    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and maze[nr][nc]:
            visited.append((nr, nc))
            # dfs(nr, nc, cnt+1, visited)
            dfs(nr, nc, cnt + 1)


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
min_cnt = 0xffffffff

visited = deque()
visited.append((0, 0))
# dfs(0, 0, 1, visited)
dfs(0, 0, 1)

print(min_cnt)

# deque([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (1, 1), (0, 1), (2, 2),
# (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 5)])
