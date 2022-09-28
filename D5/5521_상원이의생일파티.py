
# dfs 풀이
def dfs(i, N, c):
    if c == 3:
        return
    else:
        visited[i] = 1
        friend[i] = 1
        for j in range(1,N+1):
            if adjM[i][j] and visited[j] == 0:
                dfs(j, N, c+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    visited = [0]*(N+1)
    friend = [0]*(N+1)
    dfs(1,N,0)
    print(f'#{tc} {sum(friend)-1}')


#------------------------------------
#------------------------------------

# bfs 풀이

def bfs(N):
    q = [1]             # 큐 생성 + 시작점 인튜
    visited = [0]*(N+1) # visited 생성
    visited[1] = 1      # 시작점 방문표시
    while q:            # 큐가 비어있지 않으면
        t = q.pop(0)
        if visited[t] > 3:
            break
        for i in range(1, N+1):
            if adj[t][i]==1 and visited[i]==0:
                q.append(i)
                visited[i] = visited[t] + 1
    cnt = 0
    for i in range(1, N+1):
        if 1<visited[i]<4:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    ans = bfs(N)
    print(f'#{tc} {ans}')
    
#---------------------------------------
def bfs(N):
    q = [1]             # 큐 생성 + 시작점 인튜
    visited = [0]*(N+1) # visited 생성
    visited[1] = 1      # 시작점 방문표시
    cnt = 0
    while q:            # 큐가 비어있지 않으면
        t = q.pop(0)
        cnt +=1
        if visited[t] <= 2:
            for i in range(1, N+1):
                if adj[t][i]==1 and visited[i]==0:
                    q.append(i)
                    visited[i] = visited[t] + 1
    return cnt-1

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    ans = bfs(N)
    print(f'#{tc} {ans}')