'''
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

아래의 예시에서는 도달 가능하다.
 

  

아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.


[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
# '''
# q와 stack 이용 풀이

for tc in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    stack = []
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:     # 시작 좌표 찾기
                si, sj = i, j
           
    maze[si][sj] = 1                # 시작점 포함 방문한 좌표는 모두 1로 변환
    i, j = si, sj
    out =False
    result = 0
    q= []
    q.append((si, sj))              # 시작점 인큐
    while q:
        i, j = q.pop()        
        if out == True:
            break
        s= 0
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = i + di
            nj = j + dj
            s += maze[ni][nj]
            if maze[ni][nj] == 3:   # 좌표값이 3이면 도착
                result = 1          # 1 반환 후 탈출
                out = True
                break
            elif maze[ni][nj] == 0: # i,j에서 사방 탐색 후 0이면
                maze[i][j] = 1      # i,j 1로 변환 후
                q.append((ni,nj))   # 해당 ni,nj q에 쌓는다
                

        if s < 3:                   # 사방 탐색 후 주변 합이 3 미만이면
            stack.append((i,j))     # 갈림길이기 때문에 stack에 저장
        elif s == 4:                # 사방 합이 4라면 막다른길
            if i == si and j == sj: # 만약 이때 i,j가 시작점이라면 
                out = True          # 경로 없는것이기 때문에 탈출
                break

            elif stack == []:       # 만약 더이상 앞에 돌아갈 갈림길이 없다면
                i, j = si, sj       # 시작점으로 돌아감
            else:                   # 돌아갈 갈림길이 있다면
                i, j = stack.pop()  # 제일 최근 갈림길로 돌아감

    print(f'#{tc+1} {result}')
        

    