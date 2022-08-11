'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
 

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
 

v

1

2

3

4

5

 

v

1

2

3

4

5


이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
 

v

1

2

3

4

5


이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
 

답은 12와 6의 차인 6을 출력한다.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M < N )


다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

def bubble(B, n):
    for i in range(n):
        for j in range(n-1-i):
            if B[j] > B[j+1]:
                B[j], B[j+1] = B[j+1], B[j]
    return B


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
     
    B = []
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum = sum + A[i+j]
        B += [sum]
    bubble(B, len(B))
   
    print(f'#{tc+1} {B[-1] - B[0]}')
# def max_min(list):
#     max = min = 0
#     for i in range(1, len(list)-1):
#         max = min = list[0] + list[1] + list[2]
        
#         if max <=  list[i-1] + list[i] + list[i+1]:
#             max = list[i-1] + list[i] + list[i+1]
#         if min >= list[i-1] + list[i] + list[i+1]:
#             min = list[i-1] + list[i] + list[i+1]
#     return max - min

    
