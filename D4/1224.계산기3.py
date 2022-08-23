'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
# '''

def cal(word, stack):
    for i in word:
        if not i in '+*':               # 피연산자
            stack += i                  # stack에 추가
        else:                           # 연산자
            x = int(stack.pop())        # stack 상위 두개 뽑아서
            y = int(stack.pop())

            if i == '+':                # 덧셈이면 더하고
                stack.append(y + x) 
            elif i == '*':              # 곱셈이면 곱해서 stack에 다시 쌓아줌
                stack.append(y * x)
    return stack[-1]                    # 최종 연산값 반환


for tc in range(10):
    N = int(input())
    sik = list(input())
    stack = []
    result = ''
    for char in sik:
        if char in '+*()':                  # 연산자
            if stack == []:                 # stack 비어있으면 바로 쌓는다
                stack.append(char)
            elif char == '(':               # 여는 괄호면 바로 쌓는다
                stack.append(char)
            elif char == '*':               # *라면 *보다 낮은 연산자 나올떄까지 pop
                while stack[-1] == '*':
                    result += stack.pop()
                stack.append(char)          # 해당 char 추가
            elif char == '+':               # +라면 +보다 낮은 연산자 나올때까지 pop
                while stack[-1] != '(':     # ()는 들어올땐 우선순위 3이지만 들어오면 0이다
                    result += stack.pop()
                stack.append(char)
            elif char == ')':               # )라면
                while stack[-1] != '(':     # (나올때까지 pop
                    result += stack.pop()
                stack.pop()                 # 그 후 (도 pop
        else:                               # 피연산자
            result += char                  # 바로 추가

    while stack:                            # 남은 연산자
        result += stack.pop()               # result에 추가

    print(f'#{tc+1} {cal(result, [])}')


