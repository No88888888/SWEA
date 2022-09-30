# SWEA 1795.인수의 생일 파티 D6
'''
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''
from collections import deque
def dijkstra(s):
    U = deque([s])
    D[s] = 0
    while U:
        t = U.popleft()          # N개의 정점 중 출발을 제외한 정점 선택
        for w, v in adj[t]:      # 정점 t의 인접 정보 중
            if D[v] > D[t] + w:  # 시간이 앞 루트보다 짧다면
                D[v] = D[t] + w  # 해당 시간을 업데이트
                U.append(v)      # 해당 정점 추가

for tc in range(int(input())):
    N,M,X = map(int, input().split())   # N개의 집, M개의 간선의 수, 인수의 집 X
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split()) # 정점 x에서 y까지 걸리는 시간 c
        adj[x].append([c, y])              # 인접리스트

    res = [0]*(N+1)
    for i in range(1,N+1):
        D = [100000]*(N+1)    # 출발지에서 각 집까지 걸리는 최단시간 배열
        dijkstra(i)  # 출발지에서 각 집까지 걸리는 최단시간 구하기
        if i != X:
            res[i] += D[X]  # 각 잡에서 인수집까지 걸리는 최단시간을 res에 저장
        else:
            for j in range(len(D)): # 인수집에서 각 집까지 걸리는 최단시간을 
                res[j] += D[j]      # 인수집까지 오는 시간에 플러스

    print(f'#{tc+1} {max(res[1:])}')

# def dijkstra(N, s, adj, d):
#     for i in range(N+1):
#         d[i] = adj[s][i]
#     U = [s]
#     for _ in range(N-1):        # N개의 정점 중 출발을 제외한 정점 선택
#         w = 0
#         for i in range(1, N+1):
#             if (i not in U) and d[i] < d[w]: # 남은 노드 중 비용이 최소인 w
#                 w = i
#         U.append(w)
#         for v in range(1, N+1):     # 정점 i가
#             if 0<adj[w][v]<1000000:  # w에 인접이면
#                 d[v] = min(d[v], d[w] + adj[w][v])
        
# def dijkstra2(N, s, adj, d, X):

#     visited = [0]*(N+1)
#     visited[s] = 1
#     minV = 1000000
#     q = [s]
#     for i in range(N+1):
#         d[i] = adj[s][i]
#     while q:
#         w = q.pop(0)
#         for i in range(N+1):
#             if visited[i] == 0 and 0< adj[w][i]< 1000000:
#                 if i == X:
#                     d[i] = min(d[i], d[w] + adj[w][i])
#                     if d[i] < minV:
#                         minV = d[i]
#                 else:
#                     q.append(i)
#                     visited[i] = 1
#                     d[i] = min(d[i], d[w] + adj[w][i])
#     return minV



# for tc in range(int(input())):
#     N,M,X = map(int, input().split())   # N개의 집, M개의 간선의 수, 인수의 집 X
#     adj1 =[[1000000]*(N+1) for _ in range(N+1)] # 해당 정점까지 걸리는 시간 최수값 구하기 위한 기본값(무한)
#     for i in range(N+1):
#         adj1[i][i] = 0      # 자기 자신까지 가는 시간은 0
#     for _ in range(M):
#         x, y, c = map(int, input().split()) # 정점 x에서 y까지 걸리는 시간 c
#         adj1[x][y] = c
#     D = [0]*(N+1)    # 인수집에서 돌아가는 시간 배열

#     dijkstra(N,X, adj1, D)
#     tmpD = D[:]
#     for i in range(1,N+1):  # 각자집에서 인수집까지 가는 최소 시간 구하기
#         if i != X:
#             tmpD[i] += dijkstra2(N,i, adj1, D, X)  # 각집-> 인수집 + 인수집 -> 각집 시간
#     print(f'#{tc+1} {max(tmpD[1:])}')
    # U = [s]
    # for _ in range(N-1):        # N개의 정점 중 출발을 제외한 정점 선택
    #     w = 0
    #     for i in range(1, N+1):
    #         if (i not in U) and d[i] < d[w]: # 남은 노드 중 비용이 최소인 w
    #             if i == X:
                    
    #             w = i
    #     U.append(w)
    #     for v in range(1, N+1):     # 정점 i가
    #         if 0<adj[w][v]<1000000:  # w에 인접이면
    #             d[v] = min(d[v], d[w] + adj[w][v])
            
    # print(f'#{tc+1} {max(tmpD[1:])}')   # 그 중 최대값 출력
    