'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def llen(arr):          # len함수
    count = 0
    for _ in arr:
        count += 1
    return count

def max_num(arr):       # 최대값 찾기 함수
    maxnum = 0
    for i in range(llen(arr)):
        if maxnum < arr[i]:
            maxnum = arr[i]
    return maxnum

for tc in range(int(input())):
    str1 = input()      
    str2 = input()
    set_str1 = ""       
    dict = {}
    
    for i in str1:
        if i not in set_str1:
            set_str1 += i       # str1에서 중복문자 제거 ->set_str1
    
    for i in set_str1:
        count = 0
        for j in str2:
            if i == j:          # set_str1과 str2 비교
                count +=1       # 문자 같으면 해당 문자 count + 1
                dict[i] = count # 딕셔너리로 저장
    
    arr = list(dict.values())   # 딕셔너리의 값만 리스트 변환 후
    result = max_num(arr)       # 최대값 찾기 함수 돌림

    print(f'#{tc+1} {result}')
 

        
                

    # for i in str1:
    #     for j in str2:
    #         if i == j:
    #             dict[i] = dict[i] + 1

