"""
    문제
    
    주어진 텍스트를 그대로 출력하세요.
    
    출력
    #++++
    +#+++
    ++#++
    +++#+
    ++++#
"""

for i in range(1, 6):
    for j in range(1, 6):
        if i != j:
            print('+', end = '')
        else:
            print('#', end = '')
    print()
    
# 스터디그룹의 김수형님 답안
s = ['+'] * 5
 
for i in range(5):
    s[i] = '#'
    print(''.join(s))
    s[i] = '+'