'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.
 

다음은 5x5 미로의 예이다.
 

13101

10101

10101

10101

10021

 

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
 

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
# 백트래킹 이용 풀이
for tc in range(int(input())):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):                      # 패딩 작업
        miro[i] = [1] + miro[i] + [1]
    miro = [[1] * (N+2)] + miro + [[1] * (N+2)]
    

    di = [0, -1, 0, 1]                      # 좌상우하
    dj = [-1, 0, 1, 0]
    stack = []                              # 갈림길 좌표
    visited = [[] for _ in range(N+2)]      # 방문한 좌표
    ans, direction = 0, 0                   # 답, 방향
    for i in range(N+2):                    
        for j in range(N+2):
            if miro[i][j] == 1:             # miro의 1인 값을 visited에도 넣어줌
                visited[i] += [1]
            else:
                visited[i] += [0]
            if miro[i][j] == 2:             # 시작지점 좌표 구함
                sx = i
                sy = j
                

    x, y = sx, sy
    while True:
        visited[x][y] = 1        # 방문한 곳은 1 넣어줌
        if visited[x-1][y] and visited[x+1][y] and visited[x][y-1] and visited[x][y+1] and x == sx and y == sy: # 주변이 다 방문했고 시작지점이면
            ans = 0              # 탈출할 수 없기때문에 0
            break
        if visited[x-1][y] and visited[x+1][y] and visited[x][y-1] and visited[x][y+1]: # 주변이 다 방문했고
            if stack:            # stack에 뭔가 있다면
                x = stack[-1][0] # 최근 갈림길로 돌아간다
                y = stack[-1][1]
                stack.pop()
            else:                # stack에 아무것도 없다면
                x, y = sx, sy    # 시작지점으로 돌아간다
                
        if visited[x-1][y] + visited[x+1][y] + visited[x][y-1] + visited[x][y+1] < 3: # 주변 합이 3 이하라면
            stack.append([x,y]) # 갈림길이기 때문에 stack에 저장

        # --- 이동 ---    
        x += di[direction]
        y += dj[direction]
        if miro[x][y] == 3:     # 이동한 곳이 3이라면 탈출
            ans = 1             
            break
        
        if miro[x][y] == 1 or visited[x][y] == 1:  # 이동한곳 값이 1이거나 방문한 곳이라면
            x -= di[direction]                     # 다시 되돌아오고
            y -= dj[direction]                     
            direction += 1                         # 방향을 튼다
            if direction == 4:
                direction = 0
    print(f'#{tc+1} {ans}')
            
    # ==========================================================================
    
    # bfs 이용 풀이
    def bfs(i, j, N):
        visited = [[0]*N for _ in range(N)]
        q = []
        q.append((i, j))
        visited[i][j] = 1
        while q:
            i, j = q.pop(0)
            if maze[i][j] == 3:     # 3번인지 확인
                return 1
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni, nj = i+di, j+dj
                if 0<ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj] ==0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
        return 0
             
    for tc in range(int(input())):
        N = int(input())
        maze = [list(map(int, input())) for _ in range(N)]
        sti = -1
        stj = -1
        for i in range(N):
            for j in range(N):
                if miro[i][j] == 2:             # 시작지점 좌표 구함
                    sti, stj = i, j
                    break
            if sti != -1:
                break
                
        print(f'#{tc} {bfs(sti, stj, N)}')