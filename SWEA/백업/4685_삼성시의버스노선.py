T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N: 주어진 버스노선의 개수
    cnt = [0] * 5001    # 버스정류장은 1번부터 5000번까지

    for _ in range(N):
        A, B = map(int, input().split())
        # i번 버스 정류장에 다니는 버스 노선 카운트
        for i in range(A, B+1):
            cnt[i] += 1

    P = int(input())
    # result = []
    result = [0] * P
    # C번 버스 정류장에 다니는 노선의 개수 result에 넣어주기
    for i in range(P):
        C = int(input())
        # result.append(cnt[C])
        result[i] = cnt[C]

    # C번 버스정류장을 지나는 버스 노선의 개수
    print(f'#{tc}', *result)
