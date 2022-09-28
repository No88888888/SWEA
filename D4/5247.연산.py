'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# def bfs():
#     global visited
#     stack = [2]
#     top = 0
    
#     while stack:
#         v = stack[top]
        
#         stack.append(v + 1)
#         visited[top+1] = visited[top] + 1
#         if v + 1 == M:
#             res = visited[top+1]
#             break
#         stack.append(v - 1)
#         visited[top+2] = visited[top] + 1
#         if v - 1 == M:
#             res = visited[top+2]
#             break
#         stack.append(v * 2)
#         visited[top+3] = visited[top] + 1
#         if v * 2 == M:
#             res = visited[top+3]
#             break
#         stack.append(v - 10)
#         visited[top+4] = visited[top] + 1
#         if v - 10 == M:
#             res = visited[top+4]
#             break
#         top += 1
#     return res


# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     cnt = 0
#     visited = [0]*100
#     visited[0] = 1
#     print(bfs())
    
    

def bfs():
    
    visited = [0] * 1000001
    visited[N] = 1
    q = [0] * 1000001
    front, rear = -1, -1
    rear += 1
    q[rear] = N
    
    while q:
        front += 1
        v = q[front]
        for i in [v+1, v-1, v*2, v-10]:
            if 1> i or i > 1000000 or visited[i]:
                continue
            rear += 1
            q[rear] = i
            visited[i] = visited[v] + 1
            print(visited)
            if i == M:
                return visited[i] - 1
    
    
for tc in range(int(input())):
    N, M = map(int, input().split())
    
    print(f'#{tc+1} {bfs()}')
        
        
        
        
            
            # if i == 0:
            #     t = v+1
            #     q.append(t)
            #     visited.append(visited[top] + 1)
            # elif i == 1:
            #     t = v-1
            #     q.append(t)
            #     visited.append(visited[top] + 1)
            # elif i == 2:
            #     t = v*2
            #     q.append(t)
            #     visited.append(visited[top] + 1)
            # elif i == 3:
            #     t = v-10
            #     q.append(t)
            #     visited.append(visited[top] + 1)