"""
for i in range(1, 6) :
    for j in range(1, i+1) :
        print('*', end = '')
    print()
"""

"""
for i in range(5, 0, -1) :
    for j in range(1, i) :
        print(' ', end ='')
    for k in range(5, i, -1) :
        print('*', end='')
    print()
"""

""" 
for i in range(5, 0, -1) :
    for j in range(i) :
        print('*', end ='')
    print()
"""

"""
for i in range(5, 0, -1) :
    print(' ' * (5-i) + '*' * i)
"""

"""
for i in range(5, 0, -1) :
    print(' ' * (5-i) + '*' * (2*i-1))
"""

"""
menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]
menu2 = list(reversed(menu))
menu.reverse()

print(menu)
print(menu2)
"""

"""
# reverse 또다른 예시
a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = ['g', 'h', 'i']

a.reverse()
print(a)

b2 = list(reversed(b))
print(b2)

for c2 in reversed(c) :
    print(c2)
"""

"""
# 3. 5x5 배열 1~25까지 채워넣기
count = [] # 빈 리스트 생성
for i in range(1, 26) : # 1부터 25까지의 숫자를 count 리스트에 추가
    count.append(i)

for i in range(0, len(count), 5) : # 5*5 배열 생성
    print(*count[i:i+5]) # i~i+5 결과를 출력
"""

