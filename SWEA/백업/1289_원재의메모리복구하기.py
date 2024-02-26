T = int(input())
for tc in range(1, T+1):
    word = list(map(int, input()))  # 메모리의 원래 값
    N = len(word)
    reset = [0] * N     # 초기화된 상태
    cnt = 0     # 수정횟수

    for i in range(N):
        # 메모리의 원래 값이랑 초기화된 상태의 값이 다르면
        if word[i] != reset[i]:
            # i번부터 마지막까지 메모리의 원래 값으로 바꿔주기
            for j in range(i, N):
                if word[i] == 1:
                    reset[j] = 1
                elif word[i] == 0:
                    reset[j] = 0
            cnt += 1    # 변경횟수 1 증가

    print(f'#{tc} {cnt}')
