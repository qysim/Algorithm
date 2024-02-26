# 세로 R칸, 가로 C칸 보드, 보드 각 칸에는 대문자 알파벳이 하나씩 적혀있다
# 좌측 상단 (1행 1열)에 말이 놓여 있다
# 말은 상하좌우 인접한 네 칸 중 한 칸으로 이동 가능
# 새로 이동한 칸에 적혀있는 알파벳은 지금까지 지나온 모든 칸에 적힌 알파벳과 달라야한다
# 즉, 같은 알파벳이 적힌 칸을 두번 지날 수 없다
# 말이 최대한 몇 칸 지날 수 있는지 구하라, 좌측 상단칸 포함

from collections import deque
import sys

input = sys.stdin.readline


def dfs(r, c, used, cnt):
    global max_v

    if cnt > max_v:
        max_v = cnt

    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        if 0 <= nr < R and 0 <= nc < C and alphabets[nr][nc] not in used:
            used.append(alphabets[nr][nc])
            dfs(nr, nc, used, cnt+1)
            used.pop()


R, C = map(int, input().split())
alphabets = [input().strip() for _ in range(R)]

max_v = 0
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

used = deque()

used.append(alphabets[0][0])
dfs(0, 0, used, 1)

print(max_v)
