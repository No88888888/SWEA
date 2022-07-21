for tc in range(int(input())):
    s = input()
    result = 0
    if s == s[::-1]:
        result = 1
    print("#{} {}".format(tc+1, result))