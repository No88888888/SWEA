'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
 



같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 


입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''
for tc in range(int(input())):
    sdoku = [list(map(int, input().split())) for _ in range(9)] # tc 스도쿠 입력
    sep = [[] for _ in range(9)]        # 9개 박스용 빈 리스트
    result = 1                          # 결과 위한 초기값
    
    for i in range(9):
        for j in range(8):              # 0과 1~8까지 비교 1과 2~8까지 비교 방식 
            for k in range(j+1,9):
                if sdoku[i][j] == sdoku[i][k] or sdoku[j][i] == sdoku[k][i]: # 행,열 동시 비교 
                    result = 0          # 중복 있다면 result = 0
                    
    i = 0
    j = 0
    while 0 <= i < 3:                   # 작은 박스 내 비교 위한 박스 숫자들로 이루어진 리스트 sep 제작
        while 0 <= j < 3:
            sep[0].append(sdoku[i][j])
            j += 1
        while 3 <= j < 6:
            sep[1].append(sdoku[i][j])
            j += 1
        while 6 <= j < 9:
            sep[2].append(sdoku[i][j])
            j += 1
        j = 0
        i += 1
    while 3 <= i < 6:
        while 0 <= j < 3:
            sep[3].append(sdoku[i][j])
            j += 1
        while 3 <= j < 6:
            sep[4].append(sdoku[i][j])
            j += 1
        while 6 <= j < 9:
            sep[5].append(sdoku[i][j])
            j += 1
        j = 0
        i += 1
    while 6 <= i < 9:
        while 0 <= j < 3:
            sep[6].append(sdoku[i][j])
            j += 1
        while 3 <= j < 6:
            sep[7].append(sdoku[i][j])
            j += 1
        while 6 <= j < 9:
            sep[8].append(sdoku[i][j])
            j += 1
        j = 0
        i += 1
        
    for i in range(9):
        for j in range(8):
            for k in range(j+1,9):
                if sep[i][j] == sep[i][k]: # 행,열 비교방식과 같은 방법으로
                    result = 0             # 박스 내 숫자 중복 된다면 result = 0
                    
    print(f'#{tc+1} {result}')             # 중복 없었으면 초기값 1 출력