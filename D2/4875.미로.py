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

for tc in range(int(input())):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    for i in range(len(miro)):
        miro[i] = list(map(int, miro[i]))

    for i in range(N):
        miro[i] = [1] + miro[i] + [1]
    miro = [[1] * (N+2)] + miro + [[1] * (N+2)]

    di = [0, -1, 0, 1] # 좌상우하
    dj = [-1, 0, 1, 0]
    stack = []
    ans = 0

    for i in range(N+2):
        for j in range(N+2):
            if miro[i][j] == 2:
                sx = i
                sy = j
                break
    sx, sy = x, y
   
    while miro[x][y] != 3:
        sum = 0
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            sum += miro[nx][ny]
            nx, ny = 0, 0
        if sum == 4:
            if stack:
                x = stack[-1][0]
                y = stack[-1][1]
                stack.pop()
                continue
            else:
                x = sx
                y = sy
                for i in range(4):
                    nx = x + di[i]
                    ny = y + dj[i]
                    sum += miro[nx][ny]
                    nx, ny = 0, 0
                    if sum == 4:
                        ans = 0
                        out = True
                    else:
                        

        elif sum == 3:
            for i in range(4):
                nx = x + di[i]
                ny = y + dj[i]
                if miro[nx][ny] == 0:
                    x = nx
                    y = ny
        elif sum == 2 or sum == 1:
            stack.append([x, y])
            for i in range(4):
                nx = x + di[i]
                ny = y + dj[i]
                if miro[nx][ny] == 0:
                    x = nx
                    y = ny
        if miro[x][y] == 3:
            ans = 1
            break

        

        # if miro[nx][ny] == 0 and visited[nx][ny] == 0:
        #     visited[x][y] = 1
        #     x = nx
        #     y = ny
        # if miro[nx][ny] == 3:
        #     ans = 1
        #     break

