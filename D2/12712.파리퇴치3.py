'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.

아래는 N=5 의 예이다.

파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.



한 번에 잡을 수 있는 최대 파리수를 출력하라.

 

[제약 사항]

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
'''
di1 = [0, 1, 0, -1]      # + 모양
dj1 = [1, 0, -1, 0]
di2 = [1, 1, -1, -1]    # x 모양
dj2 = [1, -1, -1, 1]

for tc in range(int(input())):
    N,M = map(int, input().split())
    F = [list(map(int, input().split())) for _ in range(N)]
    
    maxV = 0
    for i in range(N):
        for j in range(N):
            cnt1 = F[i][j]         # i, j를 중심으로 + 모양
            for k in range(4):
                for z in range(1,M):
                    ni, nj = i+di1[k]*z, j+dj1[k]*z
                    if 0<=ni<N and 0<=nj<N:
                        cnt1 += F[ni][nj]
            if maxV < cnt1:
                maxV = cnt1
                
            cnt2 = F[i][j]         # i, j를 중심으로 x 모양
            for di, dj in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for z in range(1,M):
                    ni, nj = i+di*z, j+dj*z
                    if 0<=ni<N and 0<=nj<N:
                        cnt2 += F[ni][nj]
            if maxV < cnt2:
                maxV = cnt2
    print(f'#{tc+1} {maxV}')