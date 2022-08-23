'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

'''

def cal(word, stack):
    for i in word:
        if not i in '+*':           # 피연산자
            stack.append(int(i))    # stack에 정수로 쌓는다
        else:                       # 연산자
            x = stack.pop()         # 위에서 2개 뽑아
            y = stack.pop()

            if i == '+':            
                stack.append(y + x) # 덧셈 후 stack에 다시 저장
            elif i == '*':
                stack.append(y * x) # 곱셈 후 stack에 다시 저장
    return stack[-1]                # 연산이 완료된 stack값 반환



for tc in range(10):
    N = int(input())
    sik = list(input())
    stack =[]
    result = ''

    for char in sik:
        if char in '+*':                    # 연산자
            if stack == []:                 # stack 비어있으면
                stack.append(char)          # 쌓는다
            elif char == '+':               # 비어있지않고 +면
                while stack:                # 문제조건 상 +보다 우선순위 낮은 연산자는 없기 때문에 stack 빌때까지 pop
                    result += stack.pop()
                stack.append(char)          # pop이 끝나고 해당 char는 stack에 추가
            elif char == '*':               # *면
                while stack[-1] == '*':     # *보다 낮지 않은 동안 즉 *들 모두 pop
                    result += stack.pop()
                    if stack == []:         # pop하다 stack이 비면
                        break               # break
                stack.append(char)          # 마찬가지로 pop이 끝나면 해당 char stack에 추가

        else:                               # 피연산자
            result += char                  # 바로 result에 추가
    while stack:                            # stack에 남은 연산자
        result += stack.pop()               # result에 추가

    print(f'#{tc+1} {cal(result, [])}')