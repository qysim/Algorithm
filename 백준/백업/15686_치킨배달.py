# 크기가 N*N인 도시, 각 칸은 빈 칸, 치킨집, 집 중 하나이다
# 칸은 (r, c) 형태로 나타내고, 1부터 시작한다
# 치킨거리는 집과 가장 가까운 치킨집 사이의 거리이다
# 치킨거리는 집을 기준으로 정해지며, 각각의 집은 치킨거리를 가지고 있다
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다
# 두 칸의 거리는 abs(r1-r2)+abs(c1-c2)
# 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다
# 치킨 집 중에서 최대 M개를 고르고 나머지는 폐업시킨다
# 집은 적어도 하나 존재하고, M <= 치킨집의 개수 <= 13
# 도시의 치킨 거리의 최소값을 구하라

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]



print()
