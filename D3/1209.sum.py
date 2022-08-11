'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.



[제약 사항]

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''

       

def up(arr):    # 오름차순 정렬
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
           
for tc in range(1, 11):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(100)]
    sum_list = [] # 행, 열, 대각선의 합들의 리스트
    
    # 열의 합
    for i in range(100):
        s1 = 0
        for j in range(100):
            s1 += chart[i][j]
        sum_list.append(s1)
        
    # 행의 합    
    for j in range(100):
        s2= 0
        for i in range(100):
            s2 += chart[i][j]
        sum_list.append(s2)
        
    # 우하향 대각선 합
    s3= 0
    for i in range(100):
        s3 += chart[i][i]
    sum_list.append(s3)

    # 역 대각선 합
    s4 = 0
    for i in range(100):
        s4 += chart[i][100-1-i]
    sum_list.append(s4)
    
    result = up(sum_list)[-1]
    print(f'#{tc} {result}')
    

    
def up(arr):                    # 오름차순 정렬 함수
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
           
for tc in range(1, 11):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []               # 행, 열, 대각선의 합들의 리스트
    
    s3 = 0                      # 우하향 대각선의 합
    s4 = 0                      # 역방향 대각선의 합
    for i in range(100):
        s1 = 0                  # 열의 합
        s2 = 0                  # 행의 합
        s3 += chart[i][i]
        s4 += chart[i][100-1-i]
        for j in range(100):
            s1 += chart[i][j]
            s2 += chart[j][i]
        sum_list.append(s1)
        sum_list.append(s2)
        sum_list.append(s3)
        sum_list.append(s4)    # 합 리스트에 추가
    result = up(sum_list)[-1]  # 오름차순 정렬 후 최대값 도출
    print(f'#{tc} {result}')