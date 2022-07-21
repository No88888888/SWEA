for tc in range(int(input())):
    N = int(input())
    result = ''
    for i in range(N):
        alphabet, cnt = input().split()
        result += alphabet*(int(cnt))
    print("#{}".format(tc+1))
    if len(result) <= 10:
        print(result, end="")
    else:
        for j in range(len(result)//10+1):
            print(result[10*j:10*j+10])