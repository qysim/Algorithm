# 부녀회장 - 강사님, 현제, 수빈
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k)]

# 0으로 가득찬 아파트 만들기  OK
# 0채우기 OK
    for i in range(1,n):
        apt[0][i] = i
    # 1부터 K층 까지 채우기
    print(apt)
# 1층은 어떻게 채울까?  0층 이용해야지요...
# 내 앞집 값 + 아래층 내 라인 값
# for i in range(1,n):
#     apt[1][i] = apt[1][i-1] + apt[0][i]
#
# for i in range(1,n):
#     apt[2][i] = apt[2][i-1] + apt[1][i]
#
#
    for i in range(1, k):
        for j in range(1, n):
            apt[i][j] = apt[i][j - 1] + apt[i-1][j]

    print(apt)

# ---------------------------------------------------

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k)]

    # 0으로 가득찬 아파트 만들기  OK
    # 0채우기 OK
    for i in range(1,n):
        apt[0][i] = i
    # 1부터 K층 까지 채우기
    print(apt)
    # 1층은 어떻게 채울까?  0층 이용해야지요...
    # 내 앞집 값 + 아래층 내 라인 값
    # for i in range(1,n):
    #     apt[1][i] = apt[1][i-1] + apt[0][i]
    #
    # for i in range(1,n):
    #     apt[2][i] = apt[2][i-1] + apt[1][i]
    #
    #
    # for i in range(1, k):
    #     for j in range(1, n):
    #         apt[i][j] = apt[i][j - 1] + apt[i-1][j]

    for i in range(1,k):
        for j in range(1,n):
            # apt[k][n]
            # 아래층에 1호부터 j호 까지 합구하기
            for s in range(1,j+1):
                apt[i][j] += apt[i-1][s]
    print(apt)

# ---------------------------------------------------

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k)]
    # 0으로 가득찬 아파트 만들기  OK
    # 0채우기 OK
    for i in range(1,n):
        apt[0][i] = i
    # 1부터 K층 까지 채우기
    print(apt)
    # 1층은 어떻게 채울까?  0층 이용해야지요...
    # 내 앞집 값 + 아래층 내 라인 값
    # for i in range(1,n):
    #     apt[1][i] = apt[1][i-1] + apt[0][i]
    #
    # for i in range(1,n):
    #     apt[2][i] = apt[2][i-1] + apt[1][i]
    #
    #
    # for i in range(1, k):
    #     for j in range(1, n):
    #         apt[i][j] = apt[i][j - 1] + apt[i-1][j]

    for i in range(1,k):
        for j in range(1,n):
            # apt[k][n]
            # 아래층에 1호부터 j호 까지 합구하기
            for s in range(1,j+1):
                apt[i][j] += apt[i-1][s]
    print(apt)

# ---------------------------------------------------

T = int(input())
for test_case in range(1, T + 1):
    k = int(input())
    n = int(input())
    apt = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, n+1):
        apt[0][i] = i
        for j in range(1, k+1):
            apt[j][i] = apt[j][i - 1] + apt[j - 1][i]
    print(apt)
    print(apt[k][n])