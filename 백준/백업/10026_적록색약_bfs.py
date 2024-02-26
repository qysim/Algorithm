# 적록색약은 빨간색과 초록색의 차이를 느끼지 못한다
# N*N 칸에 R, G, B 중 하나가 있다
# 같은 색상이 상하좌우로 인접해 있는 경우 두 글자는 같은 구역에 속한다
# 적록색약이 아닌 사람은 (R, G, B), 적록색약인 사람은 (R+G, B)
# 1. 입력받고 적록색약인 사람 배열을 R -> G or G -> R로 바꾸기
# 2. 함수 내 조건문에서 R이면 G와 같은 값으로 판별하기


def bfs(r, c, arr, flag):
    # 상 하 좌 우
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # queue 초기화
    queue = []

    # 출발점 방문표시
    arr[r][c] = 1
    queue.append((r, c))
    color = data[r][c]

    # 큐가 비어있지 않으면 반복
    while queue:
        r, c = queue.pop(0)

        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            # 범위 안이고 방문하지 않았고 내가 찾는 값이면 방문
            if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
                if data[nr][nc] == color:
                    arr[nr][nc] = 1
                    queue.append((nr, nc))
                elif flag == 2 and color != 'B' and data[nr][nc] != 'B':
                    arr[nr][nc] = 1
                    queue.append((nr, nc))


N = int(input())
data = [input() for _ in range(N)]

# 적록색약이 아닌 사람
visited1 = [[0] * N for _ in range(N)]
cnt1 = 0
# 적록색약인 사람
visited2 = [[0] * N for _ in range(N)]
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i, j, visited1, 1)
            cnt1 += 1
        if not visited2[i][j]:
            bfs(i, j, visited2, 2)
            cnt2 += 1

# 적록색약 아닌 사람의 구역 개수, 적록색약인 사람의 구역 개수 출력
print(cnt1, cnt2)
