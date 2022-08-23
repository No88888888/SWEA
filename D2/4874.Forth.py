'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
 

3 4 + .
 

Forth에서는 동작은 다음과 같다.
 

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

 

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
 

다음은 Forth 연산의 예이다.
 

코드
4 2 / .
4 3 - .

출력
2
1


[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
# '''

for tc in range(int(input())):
    sik = list(input().split())
    stack = []
    cnt1, cnt2 = 0, 0
    
    for i in sik:
        if i in '+-*/.':
            cnt1 += 1           # 연산자 + '.'의 갯수
        else:
            cnt2 += 1           # 숫자의 갯수
    if cnt1 != cnt2:            # 두 숫자가 같지 않다면 
        print(f'#{tc+1} error') # error
        continue

    for char in sik:
        if char == '.':                         # .이면 stack에서 숫자 꺼내 출력
            print(f'#{tc+1} {int(stack[-1])}')

        elif not char in '+-/*':                # 피연산자
            stack.append(char)                  # stack에 쌓는다

        else:                                   # 연산자
            x = int(stack.pop())                # 위에서 두개씩 꺼내
            y = int(stack.pop())                # '-'와 '/' 연산 순서에 유의하며 계산 후
            if char == '+':                     # stack에 다시 쌓는다
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*': 
                stack.append(y * x)
            elif char == '/': 
                stack.append(y / x)