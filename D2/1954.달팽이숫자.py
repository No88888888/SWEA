'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,
 



N이 4일 경우,
 


[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

for tc in range(int(input())):              
    N = int(input())
    snail = [[0]*N for _ in range(N)]       # 빈 차트 생성

    di = [0, 1, 0, -1]                      # 우하좌상
    dj = [1, 0, -1, 0]
    num, direction, x, y = 0, 0, 0, 0
    
    while num < N**2:
        if 0 <= x < N and 0 <= y < N and snail[x][y] == 0:  # 이동 가능한 칸이면
            num += 1
            snail[x][y] = num
            x = x + di[direction]
            y = y + dj[direction]           # 숫자 찍고 같은 방향이동
        else:
            x = x - di[direction]           # 이동 불가능한 칸이면 원래  칸으로 돌아온 후
            y = y - dj[direction]
            direction += 1                  # 방향 전환
            if direction > 3:               
                direction = 0               # 방향 '상'이었으면 다시 '우'로
                x = x + di[direction]       
                y = y + dj[direction]
                num += 1
                snail[x][y] = num           # 돌아온 자리에서 바꾼 방향으로 전진 후 숫자찍고
                x = x + di[direction]
                y = y + dj[direction]       # 한칸 더 이동
            else:        
                x = x + di[direction]       # '우''하''좌'면
                y = y + dj[direction]       # 똑같이 원래 자리 돌아온후
                num += 1
                snail[x][y] = num           # 바꾼 반향 이동 후 숫자 찍고
                x = x + di[direction]
                y = y + dj[direction]       # 한칸 더 전진
    print(f'#{tc+1}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end = ' ')
        print()
            
    #     if 0 <= x < N and 0 <= y < N and snail[x][y] == 0:
    #         num += 1
    #         snail[x][y] = num
    #         x = x + di[direction]
    #         y = y + dj[direction]
    #     else:
    #         direction +=1
    #         x = x - di[direction]
    #         y = y - dj[direction]
            
        
    
    # for i in range(1):
    #     for j in range(N):
    #         num += 1
    #         if snail[i][j+dj[i]] != 0:
                
    #         snail[i][j+dj[i]] = num
            
            
    #         for k in range(4):
    #             ni = i + di[k+i]
    #             nj = j + dj[k+i]
    #             if 0<=ni<N and 0<=nj<N:
    #                 num += 1
    #                 snail[i][j] = num
    #                 break
                    

            
           
            
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# arr = [[1,2,3,4], [4,5,6,8]]
# for i in range(N):
#     for j in range(M):
#         for d in range(1,3):
#             for k in range(4):
#                 ni = i + dj[k] * d
#                 nj = j + dj[k] * d
#                 if 0<=ni<N and 0<=nj<M:
#                     print(ni, nj)