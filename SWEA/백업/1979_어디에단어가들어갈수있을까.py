# N*N 크기 퍼즐, 특정길이 K를 갖는 단어가 들어갈 수 있는 자리 수 출력

T = int(input())
for tc in range(1, T+1):
    # N: 단어퍼즐크기, K: 단어의길이
    N, K = map(int, input().split())
    # 퍼즐의 흰색 부분은 1, 검은색 부분은 0
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 가로 찾기 (행 순회)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:   # 흰칸이면 cnt 1 증가
                cnt += 1
            # 검은칸을 만나거나 마지막 칸에 왔을 때
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:    # 흰칸 개수와 단어길이랑 같으면
                    ans += 1    # 자리수 1 증가
                cnt = 0         # 카운트 초기화

    # 세로 찾기 (열 순회)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:   # 흰칸이면 cnt 1 증가
                cnt += 1
            # 검은칸을 만나거나 마지막 칸에 왔을 때
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:    # 흰칸 개수와 단어길이랑 같으면
                    ans += 1    # 자리수 1 증가
                cnt = 0         # 카운트 초기화

    print(f'#{tc} {ans}')
