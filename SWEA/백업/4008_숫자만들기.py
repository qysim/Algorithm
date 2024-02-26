from collections import deque


def comb(i):
    if i == N - 1:
    # if i == N-1 and tmp not in checked:
    #     checked.append(tmp[:])
        operate(tmp)
        # print(tmp)
        # print(checked)
        return

    for j in range(N-1):
        if not visited[j]:
            tmp[i] = operators[j]
            visited[j] = 1
            comb(i+1)
            visited[j] = 0


def operate(arr):
    global max_v, min_v

    # 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
    idx = 0
    op = nums[idx]
    for i in range(N-1):
        idx += 1
        if arr[i] == '+':
            op += nums[idx]
        elif arr[i] == '-':
            op -= nums[idx]
        elif arr[i] == '*':
            op *= nums[idx]
        else:
            op = int(op/nums[idx])

    result.append(op)
    # print(result)
    # 연산 결과랑 최대값 최소값 비교
    # max_v = max(result, max_v)
    # min_v = min(result, min_v)


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자의 개수
    op_nums = list(map(int, input().strip().split()))
    nums = list(map(int, input().strip().split()))

    # max_v = -100000000
    # min_v = 100000000

    # 연산자 개수만큼 배열에 넣어주기
    operators = deque()
    for i in range(op_nums[0]):
        operators.append('+')
    for i in range(op_nums[1]):
        operators.append('-')
    for i in range(op_nums[2]):
        operators.append('*')
    for i in range(op_nums[3]):
        operators.append('//')
    # print(operators)

    # 연산자 조합하고 연산하기
    visited = [0] * (N - 1)
    tmp = [None] * (N - 1)
    checked = deque()
    result = deque()
    comb(0)
    # for i in range(len(checked)):
    #     operate(checked[i])
    max_v = max(result)
    min_v = min(result)

    # print(max_v, min_v)
    ans = max_v - min_v
    # 연산의 최대값과 최소값의 차이를 출력
    print(f'#{tc} {ans}')
