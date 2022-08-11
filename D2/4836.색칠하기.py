'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
 

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

for tc in range(int(input())):
    N = int(input())                                        # 칠할 횟수
    chart = [([0]*10) for _ in range(10)]                   # 빈 10x10 차트
    count = 0                                               # 보라색 칸의 수
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())   # 시작, 끝 좌표, 칠할 색
        for i in range(r2-r1+1):        
            for j in range(c2-c1+1):
                chart[i+r1][j+c1] += color                  # 해당 구간에 해당 색 칠
                                                            # 레드 +1 블루 +2
    for i in range(len(chart)):                             
        for j in range(len(chart)):
            if chart[i][j] == 3:                            # 칠해진 차트에서 겹친 부분(보라색)은 3
                count += 1                                  # 카운트
    print(f'#{tc+1} {count}')
    
    # for i in range(color[2]-color[0]):
    #     chart[color]
    #     for j in range(color[3]-color[1]):
    #         chart[i][j] = color[4]
    # print(chart)
            
            
            
            
    #color = [list(map(int, input().split())) for _ in range(N)]    # 색칠할 영역
            # color[i][0], color[i][2]+1
            # color[i][1], color[i][3]+1