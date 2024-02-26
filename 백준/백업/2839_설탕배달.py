# N 킬로그램 배달, 설탕봉지는 3킬로그램과 5킬로그램 두 종류
# 최대한 적은 개수의 봉지를 들고 가려고 함

N = int(input())

# N 번까지 구해야해서 N+1개 만들어줌
# 정확하게 만들수 없다면 -1 출력
dp = [-1] * (N+1)

sugar = 0

for a in range(N):
    for b in range(N):
        if (5 * a + 3 * b) == N:
            sugar = a + b
            dp[N] = sugar

        # 배달하는 봉지의 최소 개수 출력
        if sugar < dp[N]:
            dp[N] = sugar

print(dp[N])
