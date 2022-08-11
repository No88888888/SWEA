'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 k가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 


[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

 

[입력]
 

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''

T = int(input()) # test케이스

for tc in (range(T)):
    full, N, M = map(int, input().split())
    stop= [0]* (N+1)
    ch = list(map(int, input().split()))
    
    for i in range(N+1):                                                                      
        for j in range(len(ch)):    
            if i == ch[j]:
                stop[i] = full      # 충전소가 표시된 총 정류장 stop 표현 [0,3,0,3,0,3...]
                
    for h in range(len(stop)):
        for m in range(len(ch)):
            full = full - 1
            if stop[h] != 0:
                if full > ch[m+1] 
    
    
    for b in range(1, len(ch)):
        if ch[0] - 0 > full or ch[b] - ch[b-1] > full or N - ch[-1] > full or full*M < N: # 충전소 간의 거리가 full보다 크거나 
            print(0)                                                                          # 총 충전소 개수가 전체 거리를 갈수 없는 
                                                                                              # 개수라면 0을 프린트
    
    count = 0
    for h in range(N+1):
        full = full - h           # 버스 출발 후 정류장 마다 -1
        
        
        if h > 1 and stop[h] != 0:    
            full = stop[h]
            count += 1
        if 
    print(f'#{tc} {count}')
        