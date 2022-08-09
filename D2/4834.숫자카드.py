'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

'''

def max_num(arr):
    maxnum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxnum:
            maxnum = arr[i]
    return maxnum


for T in range(int(input())):
    N = int(input())
    num = input()
    list_a = [] # 숫자카드 리스트
    list_b = [] # 각 숫자들의 개수 리스트
    list_c = [] # 가장 많이 나온 개수의 숫자카드 리스트
    
    for char in num:
        list_a += [int(char)]    # 숫자카드의 숫자를 리스트 저장
    for i in range(10):
        list_b[i] += [list_a.count(i)]  # 각 숫자들의 개수를 list_b에 저장
    for j in range(10):
        if list_b[j] == max_num(list_b): # 가장 많이 나온 숫자의 인덱스 값을 list_c에 저장
            list_c += [j]
        if j == 9:
            print(f'#{T+1} {max_num(list_c)} {max_num(list_b)}') # list_c의 최대값(가장 많이 나온 숫자가 동일하다면 더 큰값)
                                                                # 과 가장 많이 나온 개수을 출력
            # if list_b.count(max(list_b)) == 1:
            #     print(f'#{T+1} {j} {max(list_b)}')
            # elif list_b.count(max(list_b)) > 1:
            #     list_c += [j]
            #     if j == 9:
            #         print(f'#{T+1} {max(list_c)} {max(list_b)}')
            # print(f'#{T+1} {max(list_c)} {max(list_b)}')
                
        
        




# from collections import Counter

# for T in range(int(input())):
#     N = int(input())
#     num = input()
#     dict_a = {}
#     dict_b = {}
#     list_a = []
   
#     for char in num:
#         list_a += [int(char)]
#     for i in range(10):
#         dict_a[i] = list_a.count(i)
#     for j in range(10):
#         dict_b[j] = list(dict_a.values()).count(j)
#         max_num = max(dict_b.values())
#     for k in range(10):
#         if dict_b[k] == max_num:
#             print(f'#{T+1} {k} {dict_b[k]}')
            
    # dict_b count(dict_a[i])
    #     max_num = max(dict_a.values())
        
        
            
    # for j in range(10):
    #     if dict_a[j] == max_num:
    #         print(f'#{T+1} {j} {dict_a[j]}')
    #         print('f{T} {dict_a.key(i)} {dict_a.values(i)}')
    # print(dict_a.items())
    # print(max(dict_a.values()))
    
    # print(Counter(list_a))
        
        