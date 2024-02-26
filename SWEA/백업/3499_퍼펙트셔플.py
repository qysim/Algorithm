T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()

    result = []
    if N % 2 == 0:
        for i in range(0, N // 2):
            result.append(cards[i])
            result.append(cards[N // 2 + i])
    else:
        for i in range(0, N // 2 + 1):
            result.append(cards[i])
            if N//2+1+i < N:
                result.append(cards[N // 2 + 1 + i])

    print(f'#{tc}', *result)
