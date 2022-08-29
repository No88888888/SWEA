'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def min(arr):                       # min함수
    minnum = arr[0]
    for i in range(1, len(arr)):
        if minnum > arr[i]:
            minnum = arr[i]
    return minnum

def bfs(i, j, N):                   # bfs 함수
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] = 1
    root = []
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:                                     # 도착 시
             root += [visited[i][j] - visited[sti][stj] - 1]    # 지나온 거리를 저장
        for di, dj in [[0,-1],[-1,0],[0,1],[1,0]]:
            ni = i+ di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    if root==[]:            # root 비어있으면 도착 가능 경로 X
        return 0
    else:
        return min(root)    # 지나온 거리들 중 최소값 반환

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:     # 출발 좌표 찾기
                sti, stj = i, j
                break
        if sti != -1:
            break
   
    print(f'#{tc+1} {bfs(sti, stj, N)}')
    
    ##### bfs 사용하면 어차피 처음 도착했을떄가 최단 거리기 때문에 따로 도착하면 해당 루트 거리 바로 출력하면 됨