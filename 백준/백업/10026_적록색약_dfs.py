# 적록색약은 빨간색과 초록색의 차이를 느끼지 못한다
# N*N 칸에 R, G, B 중 하나가 있다
# 같은 색상이 상하좌우로 인접해 있는 경우 두 글자는 같은 구역에 속한다
# 적록색약이 아닌 사람은 (R, G, B), 적록색약인 사람은 (R+G, B)
# 1. 입력받고 적록색약인 사람 배열을 R -> G or G -> R로 바꾸기
# 2. 함수 내 조건문에서 R이면 G와 같은 값으로 판별하기

# 기저조건 설정을 못해서 런타임에러(RecursionError) 뜨길래 넣어줌
import sys
sys.setrecursionlimit(1000000)


def dfs(r, c, color):
    # # 출발점 방문표시 # 여기보다는 아래에 적는게 좀 더 낫다
    # visited[r][c] = 1

    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        # 범위 안이고 방문하지 않았고 내가 찾는 값이면 방문
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and data[nr][nc] == color:
            # 출발점 방문표시
            visited[r][c] = 1
            dfs(nr, nc, color)


N = int(input())
data = [list(input()) for _ in range(N)]

# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0] * N for _ in range(N)]
cnt1 = 0    # 적록색약이 아닌 사람
cnt2 = 0    # 적록색약인 사람

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, data[i][j])
            cnt1 += 1

# 적록색약인 사람 배열을 R -> G or G -> R로 바꾸기
# visited 초기화
for i in range(N):
    for j in range(N):
        visited[i][j] = 0
        if data[i][j] == 'G':
            data[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, data[i][j])
            cnt2 += 1

# 적록색약 아닌 사람의 구역 개수, 적록색약인 사람의 구역 개수 출력
print(cnt1, cnt2)
