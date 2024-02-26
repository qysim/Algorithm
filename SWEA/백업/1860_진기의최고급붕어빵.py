T = int(input())
for tc in range(1, T+1):
    # N: 사람수, M초마다 K개씩 생산
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))

    # 손님 시간순으로 정렬하기
    time.sort()

    # 손님이 도착했을 때 붕어빵이 있는지 판단하기
    ans = 'Possible'
    for i in range(N):
        bbang = time[i]//M*K
        # bbang = K*time[i]//M # 실패

        # 손님 순번은 1번부터 시작 -> 실제 순번은 i+1
        if i+1 > bbang:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')
