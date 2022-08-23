'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5+6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+5+6+7+"

변환된 식을 계산하면 25를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
# '''

def cal(word, stack):                   # 후위표기식 계산 식
    
    for i in word:                      
        if not i == '+':                # 피연산자
            stack.append(int(i))        # 정수로 변환 후 stack에 추가
        else:                           # 연산자를 만나면
            x = stack.pop()             # stack 위에서 부터 x, y로 꺼내와서
            y = stack.pop()

            stack.append(y + x)         # 역순으로 연산 후 stack에 다시 넣어준다 - , / 주의해야할 사항
    return stack[-1]                    # 최종 연산이 완료된 stack[-1]값을 리턴


for tc in range(10):
    N = int(input())                    # 식의 길이
    sik = list(input())                 # 중위 표기식
    stack = []
    result = ''
    for char in sik:
        if char == '+':                 # '+'라면
            if stack == []:             # stack이 비어있다면 
                stack.append(char)      # stack에 추가
            elif stack != []:           # stack이 비어있지않다면
                result += stack.pop()   # '+'보다 낮은 우선순위의 연산자 나올때까지 pop해야함
                stack.append(char)      # 어차피 '+'에 없기 때문에 stack에 2개 이상 쌓일 일 없다
        else:                           # 피연산자
            result += char              # 바로 result에 추가

    while stack:                        # stack에 남은 연산자를
        result += stack.pop()           # result에 추가
    
    print(f'#{tc+1} {cal(result, [])}')

