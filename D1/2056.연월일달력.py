"""
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
 



해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

[그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
 


※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

T = int(input())

for i in range(1, T+1):
        
    year = input()
    list = [str(j) for j in year]  #입력한 연도를 str형태 list로 만들기
    list.insert(4, '/')
    list.insert(7, '/')            # 연월일 구분 자리에 '/' 삽입
     
    MM = int(str(list[5])+str(list[6])) #월자리 요소를 합하고 정수로 변환
    DD = int(str(list[8])+str(list[9])) #일자리 요소를 합하고 정수로 변환
                                        # ex) '1', '2', -> 12(정수)
    if not 1<= MM <= 12:
        print(f'#{i} -1')
    elif MM%2 and not 1 <= DD <= 31:    # 홀수월이고 1 <= 일 <= 31 아니라면
        print(f'#{i} -1')
    elif MM == 2 and not 1 <= DD <= 28: #2월이고 1 <= 일 <= 28 아니라면
        print(f'#{i} -1')
    elif MM>3 and MM%2 == 0 and not 1<= DD <= 30: #월 3보다 크면서 짝수월이고 1<= 일 <= 30 아니라면
            print(-1)
    else:
        print(f'#{i}', ''.join(list))
            
"""if str(MM) == str(2).zfill(2) and DD != 28:
            
            print(-1)
        if str(MM) != str(2).zfill(2) and MM%2 == 0 and DD != 30:
            print(-1)
            
    print(MM)"""
            
"""
MM = int(str(list[5])+str(list[6]))
    DD = int(str(list[8])+str(list[9]))
    if not 1<= MM <= 12:
        print(-1)
    if list[5] != 0 and list[5] != 1:
        print(-1)
    elif list[5] == 1 and list[6] != 0 and list[6] != 1 and list[6] != 2:
        print(-1)
        if 
        """          
            
            
        
    #if 
    #if list[6]
    
    
    
    
    
    
    #''.join(list)
    
