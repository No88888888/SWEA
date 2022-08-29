'''
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

양의 정수 N 개 A1, …, AN이 주어진다.

 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


[출력]

각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.

만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.
'''
# a.append()를 반복문 외부에 미리 a_app = a.append 선언해주고 사용하면 실행시간이 줄어든다
for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    danzo = []
    danzo_app = danzo.append
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            danzo_app(A[i]*A[j])            # 정수들의 곱을 리스트에 담는다

    result = []
    result_app = result.append
    for h in range(len(danzo)):
        x = danzo[h]
        while True:
            if x%10 < x//10%10:    # 해당 정수를 10으로 한번 나눈 나머지와 두번 나눈 나머지 비교
                break              # 단조 증가 수가 아니면 break
            elif x//10 == 0 and x%10 == 0:  # break하지 않고 끝까지 왔으면 단조 증가 수
                result_app(danzo[h])        # result에 담고 break
                break
            x = x//10
                
    if result == []:
        print(f'#{tc+1} {-1}')     # 단조 증가 수 없다면 -1
    else:
        print(f'#{tc+1} {max(result)}') # 있다면 최대값 도출
                        
#-----------------------------------------------------------
# 테스트케이스 50개 중 40개 맞음 시간초과 남
# 댓글에 str으로 받았다가 다시 int로 바꾸는게 시간이 오래 걸린다길래
# 위와 같이 바로 int로 받아서 &10, //10 이용하여 풀이

for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    danzo = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            danzo += [list(map(int, str(A[i]*A[j])))]
    result = []
    for h in range(len(danzo)):
        for k in range(len(danzo[h])-1):
            if danzo[h][k] > danzo[h][k+1]:
                break
            elif k == len(danzo[h])-2 and danzo[h][k] <= danzo[h][k+1]:
              
                result += [int(''.join(map(str, danzo[h])))]
                
            # for x in range(k+1, len(danzo[h])):
                # if danzo[h][k] > danzo[h][x]:
                    # break
                # elif k == len(danzo[h])-2 and x == k+1 and danzo[h][k] <= danzo[h][x]:
                    # res = int(''.join(map(str, danzo[h])))
                    # result += [res]
    if result == []:
        print(f'#{tc+1} {-1}')
    else:
        print(f'#{tc+1} {max(result)}')           
            
