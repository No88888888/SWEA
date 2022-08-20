'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# for tc in range(int(input())):
#     N, K = map(int, input().split())
#     for i in range(1<<N):
#         for j in range(N):
#             if 
# arr = list(map(int, input().split()))

# n = len(arr)

# for i in range(1<<n):
# 	for j in range(n):
# 		if i & (1<<j):
# 			print(arr[j], end=", ")
# 	print()
# print()

for t in range(1, int(input())+1):                  # 테스트케이스 입력
    N, K = map(int, input().split())                # N, K 값 입력

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    ans = 0                                         # 조건 충족하는 부분집합 개수

    for i in range(1 << n):                         # 부분집합의 개수
        # ls = []
        total = 0                                   # 원소들의 총합
        count = 0                                   # 원소의 개수
        for j in range(n):                          # 원소 수 만큼 비트 비교
            if i & (1 << j):                        # i의 j번 비트가 1인 경우
                # ls.append(arr[j])                 # 빈 리스트 ls에 넣어서 확인해봄 -> 부분집합들 출력됨
                total += arr[j]                     # 각 부분집합의 원소들의 합
                count += 1                          # 각 부분집합의 원소의 개수
        if count == N and total == K:               # N개의 원소를 갖고, 원소들의 합이 K라면,
            ans += 1                                # 조건 충족하는 부분집합 개수 증가
            
    print(f'#{t} {ans}')