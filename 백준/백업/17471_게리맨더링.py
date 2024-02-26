


def divide():
    # 구역을 두개의 선거구로 나누고 각 구역은 들 중 하나에 포함
    # 선거구는 구역을 적어도 하나 포함

    min_v = 0
    for i in range(1, 1 << N):
        area1 = []
        area2 = []
        sum1 = 0
        sum2 = 0

        for j in range(N):
            if i & (1<<j):
                area1.append(population[j])
                sum1 += population[j]
            else:
                area2.append(population[j])
                sum2 += population[j]


    # 한 선거구에 포함되어 있는 구역은 모두 연결되어야함

    # 두 선거구에 포함된 인구 차이의 최솟값 출력
    # 두 선거구로 나눌 수 없는 경우 -1 출력
    pass



# 구역의 개수
N = int(input())    
# 1번 ~ N번 구역의 인구
population = list(map(int, input().split()))
# 각 행의 첫번째 수는 인접한 구역의 수, 나머지는 인접한 구역의 번호
# temp = [list(map(int, input().split())) for _ in range(N)]
adj = {}
for i in range(N):
    temp = list(map(int, input().split()))
    adj[i+1] = temp[1:temp[0]+1]
# print(adj)


