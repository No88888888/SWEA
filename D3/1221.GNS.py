'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.'''





def up(arr):                                # 오름차순 정렬
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

str_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
int_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_dic = {}
for i in range(10):
    num_dic[i] = str_num[i]

for tc in range(int(input())):
    T, case = map(str, input().split())  # 테스트케이스 넘버와 케이스 수 입역
    N = int(case)                        # 케이스 수를 정수로 변환
    num = list(input().split())          # 케이스 입력
    result = []                          

    for i in range(N):
        for j in range(10):
            if num[i] == str_num[j]:    # 입력받은 케이스의 문자와 str_num을 비교하여 일치하면
                num[i] = j              # 해당 문자를 str_num의 인덱스로 변환
    up(num)                             # 정수로 변환한 num을 오름차순 정렬

    for i in range(len(num)):           # 정수로 변환한 num을
        result += [num_dic[num[i]]]     # 문자와 정수가 매칭되어있는 딕셔너리를 참조하여 다시 문자로 변환
    print(T)
    print(' '.join(result))
