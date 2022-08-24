'''
민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.

민석이는 처음으로 과제를 내었다.

그리고 제출한 사람의 목록을 받았다.

수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.
'''
# 버블정렬 함수 사용해도 되고 안해도 되고
# def up(arr):
    # for i in range(len(arr)):
        # for j in range(len(arr)-1-i):
            # if arr[j] < arr[j+1]:
                # arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr

for tc in range(int(input())):
    N, K = map(int, input().split())
    submit = list(map(int, input().split())) # 제출한 학생 번호
    no_submit= []                           
    for i in range(1,N+1):
        if not i in submit:
            no_submit += [i]                 # 미제출자 번호를 담는자
    # up(no_submit)
    print(f'#{tc+1}', end= ' ')              # 자동으로 오름차순으로 쌓임
    print(*no_submit)
        