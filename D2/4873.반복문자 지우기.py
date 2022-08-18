'''
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
 

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
# '''

for tc in range(int(input())):
    s = list(input())
    i = 0

    while i < len(s)-1:
        if s[i] != s[i+1]:
            i = i + 1
            continue
        else:
            s.pop(i)
            s.pop(i)
            if i == 0:
                continue
            else:
                i = i - 1
                
    print(f'#{tc+1} {len(s)}')






# def push(item, size):
#     global top
#     stack = []
#     top += 1
#     if top == size:
#         return 'overflow'
#     else:
#         stack.append(item)

# def pop():
#     global top
#     if top <= size:
#         return 'underflow'
#     else:
#         top -= 1
        

# top = -1
# size = len(s)
# s = list[input()]
# for i in range(len(s)):
#     if s[i] != s[i+1]:
#         push(s[i], size)
#     else:
#         pop()





# for tc in range(int(input())):
#     s = list(input())
#     stack = [0]*len(s)
#     top = 0
#     for i in range(1,s):
#         stack[0] = s[0]
#         top += 1
#         if stack[i-1] != stack[i]:
#             stack[top] = s[i]
#             top += 1
#         else:
#             top -= 1

#     while top == len(s)-1:


            

    
#     while True:
#         if s[i] == s[i+1]:
#             s = s - [s[i]]
#             s = s - [s[i+1]]
#             if i == 0:
#                 pass
#             else:
#                 i = i - 1
#         else:
#             i = i + 1
# print(s)
