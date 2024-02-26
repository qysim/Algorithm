T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 201 # 복도는 1번부터 200번까지
    for _ in range(N):
        A, B = map(int, input().split())
        # 반드시 A보다 B가 크다는 말이 없기 때문에
        # 둘 중에 큰 수, 작은 수를 판별해야함
        # start = min(A, B)
        # end = max(A, B)
        if A < B:
            start = (A+1)//2
            end = (B+1)//2
        else:
            start = (B+1)//2
            end = (A+1)//2
        # 방번호로 범위를 잡으면 중복되는 경우가 생김
        # 그래서 최소 복도번호부터 최대 복도번호까지 카운트 1 증가시키기
        for i in range(start, end+1):
            cnt[i] += 1

    # 최대값 찾기
    # max(cnt)
    max_v = 0
    for i in range(1, 201):
        if cnt[i] > max_v:
            max_v = cnt[i]

    print(f'#{tc} {max_v}')
