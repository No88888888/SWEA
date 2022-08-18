'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
 


 

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def dfs(v, N):
    top = -1
    visited[v] = 1
    while True:
        for w in adjList[v]:        # v위치에서 w가
            if visited[w] == 0:     # 방문하지 않았다면
                top += 1            # top 포인터 +1
                stack[top] = v      # stack 최상위에 v 저장
                v = w               # w로 v 변환
                visited[w] = 1      # 새 방문지 w도 1로 방문 표시
                break
            if w == N:              # 새 방문지가 N, 목적지라면
                return 1            # 1 반환
        else:                       # v에서 방문할 w가 없거나 다 방문 했다면
            if top != -1:           # top이 -1이 아니면
                v = stack[top]      # stack[top]을 이전 정점인 v로 돌리고
                top -=1             # top -=1
            else:                   # top이 -1이라면 출발지 돌아옴
                return 0            # 0 반환

for tc in range(int(input())):
    V, E = map(int, input().split())        # 정점, 간선
    N = V + 1                               # 인덱스 편하게 하기 위해
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int ,input().split())
        adjList[a].append(b)                # 간선 리스트 구축

    visited = [0]*N
    stack = [0]*N
    s, e = map(int, input().split())

    print(f'#{tc+1} {dfs(s, e)}')
