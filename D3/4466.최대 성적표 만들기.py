'''
당신은 N개의 과목에 대한 시험을 쳤다. 각 과목의 점수는 정수이고 만점은 100점이다.

성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다. 당신은 기왕이면 성적표에 나타나는 총점이 가장 크도록 성적표를 만들고 싶다.

최대로 만들 수 있는 총점은 몇점인지 구하여라.


 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 N,K(1≤K≤N≤100)이 공백 하나로 구분되어 주어진다.

두 번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다. 각 정수는 0 이상 100이하이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 성적표에 표시될 총점의 최댓값을 출력한다.
'''

def sum(arr):
    s = 0
    for i in arr:
        s += i
    return s
def max_num(arr):
    maxnum = 0
    for i in range(len(arr)):
        if maxnum < arr[i]:
            maxnum = arr[i]
    return maxnum
 
for tc in range(int(input())):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
   
    subset = [[]]
    for num in score:
        for i in range(len(subset)):
            subset.append(subset[i]+[num])
    print(subset)
    print()
            
    # result = []
    # for i in range(1<<n):
        # subset = []
        # for j in range(n):
            # if i & (1<<j):
                # subset.append(score[j])
        # result.append(subset)
    
    a = []
    for i in subset:
        if len(i) == K:
            print(i)
            a += [sum(i)]
    print()
    print(a)
    print(f'#{tc+1} {max_num(a)}')

