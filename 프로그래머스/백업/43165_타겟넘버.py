def dfs(idx, result, numbers, target):

    if idx == len(numbers):
        if result == target:
            return 1
        return 0

    plus = dfs(idx + 1, result + numbers[idx], numbers, target)
    minus = dfs(idx + 1, result - numbers[idx], numbers, target)
    print(plus, minus)
    return plus + minus


def solution(numbers, target):

    answer = dfs(0, 0, numbers, target)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
