'''
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
 

 

위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.

예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[제약사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다. 
 


[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
'''
def llen(arr):          # len함수
    count = 0
    for _ in arr:
        count += 1
    return count

def max_num(arr):       # 최대값 찾기 함수
    maxnum = 0
    for i in range(llen(arr)):
        if maxnum < arr[i]:
            maxnum = arr[i]
    return maxnum

for tc in range(10):
    N = int(input())
    chart = [list(input()) for _ in range(100)]
    result = []
    ans = 1                                     # 회문 최대길이가 문자 하나일 때 위한 기본값 

    arr2 = [[0]*100 for _ in range(100)]        # 열을 90도 회전시킨 arr2 구축
    for i in range(100):
        for j in range(100):
            arr2[i][j] = chart[j][i]
 

    for i in range(100):
        for j in range(99):
            for k in range(j+1,100):

                if chart[i][j] != chart[i][k]:                      # 회문은 첫 문자와 끝문자가 다르면 안됨
                    pass                                            # 다르다면 pass
                elif chart[i][j] == chart[i][k]:                    # 첫, 끝 문자 같으면
                    if chart[i][j:k+1] == chart[i][j:k+1][::-1]:    # 회문인지 확인
                        result += [llen(chart[i][j:k+1])]           # 해당 회문 길이를 result에 저장

                if arr2[i][j] != arr2[i][k]:                        # 열방향을 행으로 돌린 arr2에 대해서도 동일하게 적용
                    pass
                elif arr2[i][j] == arr2[i][k]:
                    if arr2[i][j:k+1] == arr2[i][j:k+1][::-1]:
                        result += [llen(arr2[i][j:k+1])]
                       
    if result == []:                # result가 빈 리스트라면
        print(f'#{tc+1} {ans}')     # 1 출력

    else:
        ans = max_num(result)       # 아니라면 result의 최대값을 찾아 출력
        print(f'#{tc+1} {ans}')
                

 