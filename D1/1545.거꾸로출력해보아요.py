'''
주어진 숫자부터 0까지 순서대로 찍어보세요

아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

N  N-1  N-2  0
'''

N = int(input())

for i in range(N+1):
    print(N-i, '', end = '')