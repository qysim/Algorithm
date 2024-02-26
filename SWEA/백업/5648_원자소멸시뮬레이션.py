# 이동방향은 상(0) 하(1) 좌(2) 우(3)
# 행렬과 (x,y)좌표는 방향이 다른가?
delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 원자들의 수
    # 행마다 원자 x위치, y위치, 이동방향, 보유에너지 K 가 주어진다
    data = [list(map(int, input().split())) for _ in range(N)]

    # 두개 이상의 원자가 충돌할 경우 각자 보유한 에너지를 모두 방출하고 소멸
    total = 0

    # n초 이후의 위치는?
    n = 0
    tmp = set()

    # max_time = 0
    # for i in range(N):
    #     if max_time < max(abs(data[i][0]), abs(data[i][1])):
    #         max_time = max(abs(data[i][0]), abs(data[i][1]))
    # print(max_time)

    while n <= 1000:
        if len(tmp) == len(data)-1:
            break

        n += 1

        for i in range(N):
            if i not in tmp:
                d = data[i][2]
                data[i][0] += delta[d][0]
                data[i][1] += delta[d][1]

        for x in range(N-1):
            if x not in tmp:
                for y in range(x+1, N):
                    if y not in tmp:
                        if data[x][0] == data[y][0] and data[x][1] == data[y][1]:
                            tmp.add(x)
                            tmp.add(y)

    for t in tmp:
        total += data[t][3]

    # 방출되는 에너지의 총합
    print(f'#{tc} {total}')

'''
[[-1000, 0, 3, 5], [1000, 0, 2, 3], [0, 1000, 1, 7], [0, -1000, 0, 9]]
[[-1, 1, 3, 3], [0, 1, 1, 1], [0, 0, 2, 2], [-1, 0, 0, 9]]
'''