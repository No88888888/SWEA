'''
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약 사항]

N 은 5 이상 50 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

def select_sort(arr):                   # 선택정렬 함수
    for i in range(len(arr)-1):
        min_idx = i                     # 최솟값 인덱스를 리스트 i 인덱스로 지정
        for j in range(i+1, len(arr)):  # i의 값과 다음 인덱스들의 값 비교하여   
            if arr[min_idx] > arr[j]:   # 보다 작은 값의 인덱스를
                min_idx = j             # 최소값  인덱스로 바꿈
        arr[min_idx], arr[i] = arr[i], arr[min_idx] # 리스트 전체 순회 후 찾은 최소값 인덱스의 값과 i의 값의 자리를 바꿔줌
    return arr
               
               
for tc in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    result = ' '.join(map(str, select_sort(num)))
    print(f'#{tc+1} {result}')
