'''
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.


[제약 사항]

N은 2 이상 10,000,000 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

for tc in range(int(input())):
    num = int(input())
    
    a, b, c, d, e = 0, 0, 0, 0, 0
    
    while num%2 == 0:       # 2로 안 나눠질때까지
        if num%2 == 0:
            num = num//2    
            a += 1          # 나눌때마다 + 1
    while num%3 == 0:       # 위 while에서 나눈 몫에서 차레대로 3, 5, 7, 11 로 소인수분해 진행
        if num%3 == 0:
            num = num//3
            b += 1
    while num%5 == 0:
        if num%5 == 0:
            num = num//5
            c += 1
    while num%7 == 0:
        if num%7 == 0:
            num = num//7
            d += 1
    while num%11 == 0:
        if num%11 == 0:
            num = num//11
            e += 1
            
    print(f'#{tc+1} {a} {b} {c} {d} {e}')
