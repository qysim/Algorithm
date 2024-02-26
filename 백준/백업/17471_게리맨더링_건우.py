def subset(i):
    if i == N:
        temp_sum = 0
        for el in temp:
            temp_sum += el
        ans.append((abs(abs(sum_voters - temp_sum) - temp_sum), temp[:]))
        ans.sort()
        return
    else:
        subset(i+1)
        temp[i] = voters[i]
        subset(i+1)
        temp[i] = 0


N = int(input())
voters = list(map(int, input().split()))
sum_voters = 0
real_ans = -1
for el in voters:
    sum_voters += el
temp = [0] * N
ans = []
edges = [[0] * (N) for _ in range(N)]
for i in range(N):
    in_lst = list(map(int, input().split()))
    for j in range(1, len(in_lst)):
        edges[i][in_lst[j]-1] = 1

subset(0)
for el in ans:
    s1, s2 = -1, -1
    visited = [0] * N
    for i in range(len(el[1])):
        if el[1][i] == 0:
            s1 = i
        else:
            s2 = i
    if s1 == -1 or s2 == -1:
        continue

    stack = [s1]
    visited[s1] = 1
    while stack:
        now = stack[-1]
        for j in range(len(edges[now])):
            if edges[now][j] == 1 and visited[j] == 0 and el[1][j] == 0:
                stack.append(j)
                visited[j] = 1
                break
        else:
            stack.pop()


    stack = [s2]
    visited[s2] = 1
    while stack:
        now = stack[-1]
        for j in range(len(edges[now])):
            if edges[now][j] == 1 and visited[j] == 0 and el[1][j] != 0:
                stack.append(j)
                visited[j] = 1
                break
        else:
            stack.pop()
    if 0 not in visited:
        real_ans = el[0]
        break

print(real_ans)