T = int(input())
for tc in range(1, T+1):
    # N: 서쪽 사이트 개수, M: 동쪽 사이트 개수, 0 < N <= M < 30
    N, M = map(int, input().split())

    # 한 사이트에는 한 개의 다리만 연결 가능
    # N개만큼 다리를 짓는다
    # 다리끼리는 서로 겹쳐질수 없다 -> 순서 상관없음 -> 조합
    # 다리를 지을 수 있는 경우의 수를 구하라

    # '경우의 수'가 몇번인지 결과만 구하면 됨
    # 실제 몇번과 몇번 다리가 연결되는지는 상관없음
    # 그래서 재귀, 비트마스킹 등으로 풀면 시간초과됨

    # M개 중에서 순서 상관없이 N개를 뽑는 경우의 수?
    # nCr = n! // (n-r)! * r!
    # n!의 결과를 DP 배열에 저장해봅시다
    DP = [1] * (M+1) # 0!부터 M! 까지, 0! & 1!은 1이니까 초기값을 1로
    for i in range(2, M+1): # 2!부터 M!까지 구해봅시다
        # i의 팩토리얼을 구해서 DP[i]에 할당
        DP[i] = i * DP[i-1]

    ans = DP[M] // (DP[M-N] * DP[N])

    print(ans)