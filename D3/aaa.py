def sum(arr):
    s = 0
    for i in arr:
        s += i
    return s
def max_num(arr):
    maxnum = 0
    for i in range(len(arr)):
        if maxnum < arr[i]:
            maxnum = arr[i]
    return maxnum
 
for tc in range(int(input())):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    subset = [[]]
    for num in score:
        for i in range(len(subset)):
            subset.append(subset[i]+[num])
    
    a = []
    for i in subset:
        if len(i) == K:
            a += [sum(i)]
    print(f'#{tc+1} {max(a)}')