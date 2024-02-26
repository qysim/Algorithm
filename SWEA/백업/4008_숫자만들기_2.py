from collections import deque


def comb(i, tmp):
    if tmp in tmp_set:
        return
    tmp_set.add(tmp)
    if i == N-1:
        checked.add(tmp)
        return
    for j in range(N-1):
        if not visited[j]:
            visited[j] = 1
            comb(i+1, tmp + operators[j])
            visited[j] = 0


def operate(txt):
    # 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
    idx = 0
    op = nums[idx]
    for i in range(N-1):
        idx += 1
        if txt[i] == '+':
            op += nums[idx]
        elif txt[i] == '-':
            op -= nums[idx]
        elif txt[i] == '*':
            op *= nums[idx]
        else:
            op = int(op/nums[idx])

    result.add(op)


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자의 개수
    op_nums = list(map(int, input().strip().split()))
    nums = list(map(int, input().strip().split()))

    # 연산자 개수만큼 배열에 넣어주기
    operators = deque()
    for i in range(op_nums[0]):
        operators.append('+')
    for i in range(op_nums[1]):
        operators.append('-')
    for i in range(op_nums[2]):
        operators.append('*')
    for i in range(op_nums[3]):
        operators.append('/')

    # 연산자 조합하고 연산하기
    visited = [0] * (N-1)
    checked = set()
    result = set()
    tmp_set = set()
    comb(0, '')
    for i in checked:
        operate(i)
    max_v = max(result)
    min_v = min(result)


    # 연산의 최대값과 최소값의 차이를 출력
    ans = max_v - min_v
    print(f'#{tc} {ans}')

