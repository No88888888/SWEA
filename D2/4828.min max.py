'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# 내장함수 사용 버전
import sys
input = sys.stdin.readline

for T in range(int(input())):
    list_a = []
    N = int(input())
    list_a = list(map(int,input().split()))
    result = max(list_a) - min(list_a)
    print(f'#{T+1} {result}')


# 내장함수 사용x 버전
import sys
input = sys.stdin.readline

for T in range(int(input())):
    list_a = []
    N = int(input())
    list_a = list(map(int,input().split()))
    maxnum = list_a[0]
    minnum = list_a[0]
    for i in range(N):
        if list_a[i] >= maxnum:
            maxnum = list_a[i]
    for j in range(N):
        if list_a[i] <= minnum:
            minnum = list_a[i]
    result = maxnum - minnum
    print(f'#{T+1} {result}')
