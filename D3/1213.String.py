'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.

한 문장에서는 하나의 문자열만 검색한다. 

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
# '''


for tc in range(1,11):
    T = int(input())
    pattern = input()
    target = input()
    N = len(target)
    M = len(pattern)
    i = 0
    j = 0
    ans = 0

    while i < N and j < M:
        if target[i] != pattern[j]: # 같지 않다면
            i = i - j               
            j = -1
        i = i + 1                   # 같기 시작했던 다음 인덱스로 돌아감
        j = j + 1                   # j를 0으로 되돌림
        
    
        if j == M:                  # j가 M이라면(M-1까지 동일했다면)
            ans += 1                # 패턴이 나온것으로 ans += 1
            j = 0                   # 재탐색 위해 j 초기화
    print(f'#{tc} {ans}')