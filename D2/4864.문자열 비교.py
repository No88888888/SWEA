'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
 

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
 

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
for tc in range(int(input())):

    def pre_process(P):             # lps 만드는 함수
        
        lps = [0] * len(P)          # 패턴 길이만큼 빈 리스트 생성
        j = 0                       # prefix index
        
        for i in range(1, len(P)):
            if P[i] == P[j]:        # 패턴 순회하며 같다면
                lps[i] = j + 1      # 해당 인덱스의 lps를 j+1로 변환
                j = j + 1           
                
            else:                   # 같지 않다면
                j = 0               # j 초기화
                if P[i] == P[j]:    # 그자리에서 다시 비교 
                    lps[i] = j + 1
                    j = j + 1
            
        return lps

    def KMP(T, P):
        lps = pre_process(P)
        i, j = 0, 0
        N = len(T)
        M = len(P)
        result = 0
        
        while i < N and j < M:
            if T[i] == P[j]:        # 타겟,패턴 동시 순회하며 같다면
                i = i + 1           # 둘다 +1 전진
                j = j + 1
            else:                   # 같지 않고
                if j != 0:          # j =0이 아니라면
                    j = lps[j-1]    # i는 유지 j만 이동하여 재비교
                else:               # j = 0이라면
                    i += 1          # 처음부터 비교하듯 i+1 이동하여 비교
            if j == M:              # j = M라면 패턴이 끝까지 순회한 것
                result += 1
        return result

    pattern = input()
    target = input()
    

    print(f'#{tc+1} {KMP(target, pattern)}')




