'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''

# def up_down(arr):
#     for _ in range(len(arr)):
#         for j in range(0, len(arr)-2, 2):
#             if arr[j] < arr[j+2]:
#                 arr[j], arr[j+2] = arr[j+2], arr[j]
#         for k in range(1,len(arr)-2, 2):
#             if arr[k] > arr[k+2]:
#                 arr[k], arr[k+2] = arr[k+2], arr[k]
#     return arr
                
                
            
# for tc in range(int(input())):
#     N = int(input())
#     num = list(map(int, input().split()))
    
# print(up_down(num))



# def up_down(arr):
#     s = [0]*len(arr)
#     for i in range(len(arr)):
#         for j in range(len(arr)-1-i):
#             if j%2 == 0:
#                 s[j] == arr[i]
#             elif j%2:
#                 s[j] == arr[len(arr)-1-i]
#     return s
# print(up_down([10,9,8,7,6,5,4,3,2,1]))

for tc in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))   # 의임의 숫자 리스트
    s= [0]*N                                # 같은 길이의 빈 리스트 구축
    
    for i in range(len(num)):               # 입력 받은 리스트를 내림차순 정렬
        for j in range(len(num)-1-i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    down_list = num                         # 리스트 이름을 down_list로 변경하여 가독성 높임
      
    big_index = []                          # down_list의 앞쪽 반
    for i in range(len(down_list)//2):      # big_list로 넣어줌
        big_index += [down_list[i]]

    small_index = []                        # down_list의 뒤쪽 반
    for i in range(len(down_list)//2,N):    # small_list로 넣어줌
        small_index += [down_list[i]]

    for i in range(len(big_index)):         # s의 짝수 인덱스에 big_list를 순서대로 넣어줌
        s[i*2] = big_index[i]

    for i in range(len(small_index)):       # s의 홀수 인덱스에 small_list를 역순으로 넣어줌
        s[i*2+1] = small_index[len(small_index)-1-i]
        
    print(f'#{tc+1}', end =' ')
    for i in range(10):
        print(s[i], end=' ')
    print(' ')                              # 없으면 프린트가 끊기지 않아 다음 테스트 케이스의 N까지 출력된다
