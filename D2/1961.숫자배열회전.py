'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


[제약 사항]

N은 3 이상 7 이하이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

다음 N 줄에는 N x N 행렬이 주어진다.

[출력]

출력의 첫 줄은 '#t'로 시작하고,

다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''

for tc in range(int(input())):
    N = int(input())
    ori = [list(map(int, input().split())) for _ in range(N)]   # 오리지널 숫자 입력 배열
    gusip = [[0]*N for _ in range(N)]                           # 90도 돌릴 배열
    baekparsip = [[0]*N for _ in range(N)]                      # 180도 돌릴 배열
    ibaekchiilsip = [[0]*N for _ in range(N)]                   # 270도 돌릴 배열
    for i in range(N):
        for j in range(N):
            gusip[i][j] = ori[N-1-j][i]                         # 각 각도 별 전환 배열 저장
            baekparsip[i][j] = ori[N-1-i][N-1-j]
            ibaekchiilsip[i][j] = ori[j][N-1-i]                 
            
    result = [[0]*N for _ in range(N)]                          # 답 출력을 위한 빈 배열
    for i in range(N):
        result[i][0] = ''.join(map(str, gusip[i]))              # 0행에 90도 배열 요소
        result[i][1] = ''.join(map(str, baekparsip[i]))         # 1행에 180도 배열 요소
        result[i][2] = ''.join(map(str, ibaekchiilsip[i]))      # 2행에 270도 배열 요소
        
    print(f'#{tc+1}')    
    for i in range(N):                                          # N열만큼
        for j in range(3):                                      # 0: 90도 1: 180도 2: 270도
            print(result[i][j], end=' ')
        print()
    
    # for i in range(N):
    #     for j in range(N):
    #         empty[i][j] = ori[N-1-i][N-1-j]
    
    # for i in range(N):
    #     for j in range(N):
    #         empty[i][j] = ori[j][N-1-i]
    # print(empty)