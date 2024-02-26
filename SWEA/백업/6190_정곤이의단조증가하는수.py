def solve():
    max_v = -1

    for i in range(N-1):
        for j in range(i+1, N):
            is_danjo = True
            tmp = num[i] * num[j]
            if tmp <= max_v:
                continue
            lst = []
            while tmp != 0:
                lst.append(tmp % 10)
                tmp = tmp // 10

            if len(lst) > 1:
                for k in range(len(lst)-1):
                    if lst[k] < lst[k+1]:
                        is_danjo = False

            if is_danjo and num[i]*num[j] > max_v:
                max_v = num[i]*num[j]

    return max_v


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    print(f'#{tc} {solve()}')