"""10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.


[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)"""


"""t = int(input())

for test in range(1, t+1):
    a = map(int, input().split())
    oddsum = 0
    for i in a:
        if i%2 != 0:
            oddsum += i
    print('#', test, ' ', oddsum)"""

"""t = int(input())
 
for test_case in range(1,t+1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        if i%2!=0:
            answer += i
    print("#"+str(test_case),str(answer))"""

T = int(input())

for test in range(1, T+1):
    a = list(map(int, input().split()))
    oddsum = 0
    for i in a:
        if i%2 != 0:
            oddsum += i
    print('#'+str(test), oddsum)






"""t = int(input())

for i in range(1, t+1):
    a = map(int, input().split())
    oddsum = 0
    for i in a:
        if i%2 !=0:
            oddsum += i
    print('#'+str(i), ' ', oddsum)"""
            


    
