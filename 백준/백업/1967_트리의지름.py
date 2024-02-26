# 트리는 사이클이 없는 무방향 그래프이다.
# 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재한다.
# 트리의 지름은 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하기
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())    # 노드의 개수
graph = defaultdict(list)
for i in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
# print(graph)

max_v = 0
visited = [0] * (n+1)


def dfs(start, sum_v):
    global max_v

    if sum_v > max_v:
        max_v = sum_v

    for c, w in graph[start]:
        if not visited[c]:
            visited[c] = 1
            dfs(c, sum_v + w)
            visited[c] = 0


for k in graph.keys():
    visited[k] = 1
    dfs(k, 0)
    visited[k] = 0

print(max_v)
