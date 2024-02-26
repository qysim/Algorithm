for tc in range(1, 11):
    N = int(input())
    # 1은 N극 성질(아래로 떨어짐), 2는 S극 성질(위로 올라감)
    data = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    for i in range(N):
        tmp = []
        for j in range(N):
            if data[j][i] != 0:
                tmp.append(data[j][i])

        for k in range(len(tmp)-1):
            if tmp[k] == 1 and tmp[k+1] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')