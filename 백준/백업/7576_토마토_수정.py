# 누적해서 더하지 말고 tomato[nr][nc] = 1로 하고 cnt를 인자로 넣어주기, (i,j) 대신 r, c로 적기, 수빈이처럼 덜익은 토마토를 변수로 설정

# queue를 그냥 리스트로 하면 시간초과 나서 deque 씀
from collections import deque


def bfs():
    queue = deque()

    # 시작지점 전부 queue에 넣기
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i, j, 0))

    while queue:
        r, c, cnt = queue.popleft()

        # 상 하 좌 우 확인
        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < M and not tomato[nr][nc]:
                queue.append((nr, nc, cnt+1))
                # 날짜 구하려면 누적해서 더해주기
                tomato[nr][nc] = 1

    # 모든 방문이 끝난 후
    max_v = 0
    for i in range(N):
        for j in range(M):
            # 토마토가 모두 익지는 못하는 상황이면 -1 출력
            if tomato[i][j] == 0:
                return -1

            if tomato[i][j] > max_v:
                max_v = tomato[i][j]

    # 만약 저장될때부터 모든 토마토가 익어있는 상태면 0 출력
    # 시작지점을 1로 시작했기 때문에 날짜를 구하려면 -1 해줘야함
    return max_v - 1


# M : 상자의 가로 칸 수, N : 상자의 세로 칸 수
M, N = map(int, input().split())
# 1 : 익은 토마토, 0 : 익지않은 토마토, -1 : 토마토 없음
tomato = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토의 왼쪽, 오른쪽, 앞, 뒤의 토마토는 하루가 지나면 익음
# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 토마토가 모두 익을 때까지의 최소 날짜 출력
ans = bfs()
print(ans)


''' 수빈 코드 (덜익은 토마토 변수로 설정 -> 이중for문 안돌려도됨)
from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs():
    global cnt
    queue = deque(ripe_tomatoes)

    minimum_date = 0
    while queue:
        cr, cc = queue.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            # 범위 안에 있고, 익지 않았으며, 과일이 있는 경우만...
            if 0 <= nr < N and 0 <= nc < M and boxes[nr][nc] != -1 and not ripened[nr][nc]:
                # 큐에 삽엡
                queue.append((nr, nc))
                # 방문 표시
                ripened[nr][nc] += ripened[cr][cc] + 1
                # 덜 익은 사과 익혔으니 덜 익은 사과 개수 cnt 빼기
                cnt -= 1
                # 최소 날짜 세기
                if minimum_date < ripened[nr][nc]:
                    minimum_date = ripened[nr][nc]

    return minimum_date


# 가로 칸 수 M, 세로 칸 수 N
M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]
# 안 익은 토마토 세는 변수
cnt = 0
# 익은 토마토 위치 기억하는 리스트
ripe_tomatoes = []
# 익었는지 판단하는 리스트 (1 익음, 0 안익음 혹은 토마토 없음)
ripened = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 0:
            cnt += 1
        elif boxes[i][j] == 1:
            ripe_tomatoes.append((i, j))
            ripened[i][j] = 1
# 이미 모든 토마토가 익은 경우면 익힐 필요가 없음
if cnt == 0:
    print(0)
# 익지 않은 토마토가 있다면 bfs 돌리기
else:
    result = bfs()
    if cnt != 0:
        print(-1)
    else:
        print(result - 1)
        '''