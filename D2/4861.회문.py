'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
 

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
 



[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다
'''

for tc in range(int(input())):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]
    out = False                 # 회문 찾을 시 코드 종료하기 위한 기본값
    result = []
    row = []
    col = []
    for i in range(N):          # 전체 행 순회
        if out:
            break
        for j in range(N-M+1):  # 한 열에서 전체 길이 - 패턴길이 까지 순회
            if out:
                break
                
            for k in range(M+j-1, j-1, -1): # 역으로 순회하며 
                
                row += code[i][k]   # 열 값 저장
                col += code[k][i]   # 행 값 저장
            
            if row == row[::-1]:    # 열이 회문이라면
                result = row[::-1]  # 결과에 열 회문 저장
                out = True          
            elif col == col[::-1]:  # 행이 회문이라면 
                result = col[::-1]  # 결과에 행 회문 저장
                out =True
            else:
                row = []
                col = []

    ans = ''.join(result)
    print(f'#{tc+1} {ans}')
