def solve(i,j,flag,cnt): # i,j는 움직일애들 
    # flag가 True면 K값 아직 안뺀거 False면 K값 빼준거
    # cnt는 등산로 길이   
    global result
    for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<N:
            if case[ni][nj] < case[i][j] and visit[ni][nj] == 0:
                visit[ni][nj] = 1
                solve(ni,nj,flag,cnt+1)
                visit[ni][nj] = 0
            elif flag == True and case[ni][nj]-K < case[i][j] and visit[ni][nj] == 0:
                visit[ni][nj] = 1
                save = case[ni][nj] # 임시변수 경우의 수 끝내면 다시 원래로 바꿔야하기에
                case[ni][nj] = case[i][j] -1 # K값 뺼 수 있으면 원값에서 -1 해주는게 가장 효율적
                solve(ni,nj,False,cnt+1)
                visit[ni][nj] = 0
                case[ni][nj] = save # 원래로 바꾸는 코드
    if result < cnt:
        result = cnt
        return


T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    case = [list(map(int,input().split())) for _ in range(N)]
    maxy = 0
    for i in range(N):
        for j in range(N):
            if case[i][j] > maxy:
                maxy = case[i][j]
    visit = [[0]*N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if case[i][j] == maxy:
                visit[i][j] = 1
                solve(i,j,True,1)
                visit[i][j] = 0

    print(f'#{t+1}',result)