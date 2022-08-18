'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
 



N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


[제약 사항]

파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.

삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
# 메모이제이션 활용
# 실행시간 154ms
def pascal(N):
    if N <= 2:
        return memo[N]
    
    pascal(N-1)                         # 재귀호출
    
    for i in range(1, N-1):             # 첫항과 끝항은 1로 고정이기 때문에
        memo[N][i] = memo[N-1][i-1] + memo[N-1][i] # 수학적으로 전 줄 i-1과 i의 합
    return memo

for tc in range(int(input())):
    N = int(input())
    memo = [[] for _ in range(N+1)]     # 인덱스 편리 위해 N+1
    for i in range(1,N+1):              # 인덱스 편리 위해 1, N+1
        memo[i] += [1]*i                # 메모이제이션 사용
        
    pascal(N)
    
    print(f'#{tc+1}')
    for i in range(1,N+1):
        print(*memo[i])
        
# 재귀활용
# 실행시간 1357ms
def tri(N):                     
    
    arr = [1]*N
    if N == 1:
        return [1]              # N이 1일땐 [1] 반환
    if N == 2:
        return [1, 1]           # N이 2일땐 [1, 1] 반환
    else:
        for i in range(1, N-1):                     # 양끝은 1이기 때문에
            arr[i] = tri(N-1)[i-1] + tri(N-1)[i]    # i번째는 전 줄의 i-1과 i의 합
        return arr


for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(1, N+1):
        print(' '.join(map(str, tri(i))))
            

        