
# 과제
# 강사님 코드
# 1번 : 별표 출력
"""
for i in range(5) : # 0, 1, 2, 3, 4로 증가(i)
    for j in range(i+1) : # 1, 2, 3, 4, 5 (j)
        print("*", end='') # 줄바꿈 없이 * 붙여줌
    print() # 줄바꿈
# ---
for i in range(5) : # 0, 1, 2, 3, 4로 증가(i)
    for j in range(4-i) : # (4, 1), (3, 2), (2, 3), (1, 4) => 4, 3, 2, 1, 0
        print(" ", end="")
    for k in range(i+1) : # 1, 2, 3, 4, 5
        print("*", end="")
    print()
# --- 위 코드 또다른 방법
for i in range(5) : # 0, 1, 2, 3, 4
    for j in range(5) : # 0, 1, 2, 3, 4 (i값에 따라 달라짐)
        if i + j < 4 : # 4, 3, 2, 1, 0
            print(" ", end = "")
        else :
            print("*", end = "")
        print()
# ---
for i in range(5) : # 0, 1, 2, 3, 4
    for j in range(5-i) : # 5, 4, 3, 2, 1
        print("*", end = "")
    print()
# ---
for i in range(5) : # 0, 1, 2, 3, 4
    for j in range(i) : # (0, 5), (1, 4), (2, 3), (3, 2), (4, 1)
        print(" ", end = "")
    for k in range(5-i) : # 공백 채워주기, j + k = 5
        print("*", end = "")
    print()
# ---
for i in range(5) : # 0, 1, 2, 3, 4
    for j in range(4-i) : # 4, 3, 2, 1, 0 # i + j = 4
        print(" ", end="")

    for k in range(2*i+1) : # 1, 3, 5, 7, 9
        print("*", end="")

    print()
# --- 위 코드 또다른 방법
for i in range(5) : # 0, 1, 2, 3, 4
    for j in range(4-i) : # = 5-i-1 # 5, 4, 3, 2, 1
        print(" ", end="")
    
    for k in range(2*i+1) : # 1, 3, 5, 7, 9
        print("*", end="")
    
    print()

# 2번 : reversed

menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]
menu2 = list(reversed(menu))
menu.reverse()

print(menu)
print(menu2)
# ---

menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]
for i in range(len(menu)) :
    print("%s, " %(menu[6-i]))

print()
# 또는
menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]
for i in range(len(menu)-1, -1, -1) :
    print("%s, " %(menu[i]))

print()
# 또는
menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]
menu2 = []
for i in range(len(menu)) :
    menu2.append(menu[len(menu)-1-i])

print(menu2)


# 3번 : 5x5 배열(1~25)
a = []

for i in range(5) : # 0~4
    b = []
    for j in range(5) : # 0~4
        b.append(5*i+j+1)
    a.append(b)

for i in a :
    print(i)



# 이전 코드 복습
s = "Hello World"

print(s.replace("o", "a")) # o부분을 a로
print(s.replace("o", "")) # o부분 생략

st = list(s)
print(st)

for i in st :
    if(i=="o") :
        continue
    print(i, end="")
print()

print(st[0:4] + st[5:7] + st[8:])

s = ""
for i in st[0:4] + st[5:7] + st[8:] :
    s += i

print(s)

s = ""
for i in st :
    if i == 'o' :
        continue
    s += i
print(s)

st2 = []
start = 0

for i in range(len(st)+1) :
    if st[i] == 'o' or i == len(st) :
        st2 += st[start:i]
        start = i+1

print(st2)

if st[len(st) - 1] != 'o' :
    st2 += st[len(st) - 1]

print(st2)
# 슬라이싱


#딜리트
s = "Hello World"

print(s.replace("o", "a")) # o부분을 a로
print(s.replace("o", "")) # o부분 생략

st = list(s)
start = 0

for j in range(len(st)):
    for i in range(start, len(st)) :
        if st[i] == 'o' :
            del st[i]
            start = i
            break
    
del st[4]
print(st)


st = list('Helloooo Woooooorloooood')
i = 0

while True:
    if i == len(st) :
        break

    if st[i] == 'o' :
        del st[i]
    else :
        i += 1

print(st)


# reverse 함수 구현
menu = ["김밥", "떡볶이", "아메리카노", "카레", "순대", "파스타", "피자"]

s1 = "김밥"
s2 = "떡볶이"

temp = s1
s1 = s2
s2 = temp

print(s1)
print(s2)

start, end = 0, len(menu)-1

for i in range(len(menu)//2) : # 혹은 while start < end : 
    temp = menu[start]
    menu[start] = menu[end]
    menu[end] = temp # menu[start], menu[end] = menu[end], menu[start]
    start += 1 # start는 앞에서부터 접근
    end -= 1 # end는 뒤에서부터 접근

print(menu)


# Chapter 06 | 튜플과 딕셔너리
# 하나의 자료구조(리스트)

# 리스트의 대괄호([]) 대신 소괄호(()) 사용
# 요소의 추가와 수정이 불가하다.

# 기존 리스트 예시 code
print(menu)
print(menu[0])
print(menu[2])
print(menu[0:3])

# 튜플 병합과 길이 구하기
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange", "melon", "strawberry")
tuple3 = tuple1 + tuple2

print(tuple3)

print(len(tuple3))

for x in tuple1 :
    print(x)

del tuple1

# 튜플로 구구단표 제작
dans = (2, 3, 4, 5, 6, 7, 8, 9)
print('구구단표')
print('-' * 30)
for dan in dans :
    for i in range(1, 10) :
        print('%d x %d = %d' %(dan, i, dan*i))
    print('-' * 30)

# 튜플로 관리자 정보 처리
admin_info = ('admin', '12345', 'rubato@naver.com')
id = input('관리자 아이디를 입력하시오. : ')
password = input('관리자 비밀번호를 입력하시오. : ')

if id == admin_info[0] and password == admin_info[1] :
    print('관리자입니다.')
else :
    print('아이디 또는 비밀번호가 잘못 입력되었습니다.')


# 딕셔너리란?
    # 키(Key)와 값(Valur)으로 구성

# 기본 구조
members = {'name' : '전예원', 'age' : 30, 'email' : 'one505@naver.com'}

print(members)
print(members['name'])
print(members['age'])

print('길이 : %d' %len(members))

name = '전예원'
scores = {'kor' : 98, 'eng' = 78, 'math' : 90, 'science' : 80}


# for문에서 딕셔너리 사용
phones = {'갤럭시 노트8' : 2017, '갤럭시 S9' : 2018, '갤럭시 노트 10' : 2019}


words = {'책상' : 'desk', '핸드폰' : 1234, 123:[1,2,3]}

for k in words :
    print(words[k])


# student = {"name":name, "age":age, "phone":phone} - 한 명에 대한 정보

# 여러명의 정보를 입력해주고 싶을 때
# 하나씩 삽입하는 방법
list = []

while True :
    name = input('이름 : ')
    age = int(input('나이 : '))
    phone = input('연락처 : ')

    if age <= 0 :
        break

    student = {"name":name, "age":age, "phone":phone}
    list.append(student)

print(list)


dic = {'kor':80, 'eng':86, 'math':97, 'com':100}

print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

for key in dic.keys() :
    print(key)

for value in dic.values() :
    print(value)

for key, value in dic.items():
    print(key, value)

for item in dic.items() :
    print(item)


# 학생 성적 조회
students = {"Kim":85, "Bob":90, "Choi":70, "Park":80}

# 조회할 학생의 이름을 입력하시오. : 
# " "학생의 점수는 몇 점이다. 또는 해당하는 학생을 찾을 수 없습니다.
# exit을 입력하면 프로그램 종료

while True :
    name = input("조회할 학생의 이름을 입력하세요.(종료하려면 exit를 입력하시오.) : ")

    if name == 'exit' : 
        print('프로그램을 종료합니다.')
        break

    check = 1

    for student in students :
        if name == student :
            print('%s학생의 점수는 %d점이다.' %(student, students[student]))
            check = 0
            break

    if check : # check = True = 1
        print('해당하는 학생을 찾을 수 없습니다.')


# 또다른 방법
students = {"Kim":85, "Bob":90, "Choi":70, "Park":80}


while True :
    name = input("조회할 학생의 이름을 입력하세요.(종료하려면 exit를 입력하시오.) : ")

    if name == 'exit' : 
        print('프로그램을 종료합니다.')
        break

    if student in students.keys :
        print('%s학생의 점수는 %d점이다.' &(student, students[student]))
    else :
        print('해당하는 학생을 찾을 수 없습니다.')


# Chapter 07 | 함수

# 기본 함수 정의와 호출

def hello() :
    print("안녕하세요.")

hello()

# 안녕하세요.


# 파이썬의 내장 함수

1. print() : 화면에 데이터 출력
2. input() : 키보드를 통해 데이터를 입력받음
3. range() : 정수의 범위 설정
4. list() : 리스트 생성
5. abs() : 숫자의 절댓값 변환
6. len() : 문자열, 리스트, 튜플, 딕셔너리 등의 길이 추출
7. round() : 소수점 이하 반올림 값을 구함
8. int() : 문자열이나 실수형 숫자를 정수형 숫자로 변환
9. float() : 문자열이나 정수형 숫자를 실수형 숫자로 변환




# 매개 변수란?

def 함수명(매개변수1, 매개변수2, ... ) :
    문장1
    문장2
    ... => 함수 정의
함수명(입력값1, 입력값2, ...) => 함수 호출



# 매개 변수가 1개인 경우
def even_odd(num) :
    if num % 2 == 0 :
        print('%d은(는) 짝수이다.' %num)
    else :
        print('%d은(는) 홀수이다.' %num)

even_odd(7)
even_odd(16)

# 매개 변수가 여러개인 경우 
def favorate_color(name, color, amount) :
    if (amount == 1) :
        print("%s님은 %s을 좋아하지 않습니다." %(name, color))
    elif (amount == 2) :
        print("%s님은 %s을  조금 좋아합니다." %(name, color))
    else :
        print("%s님은 %s을 매우 좋아합니다." %(name, color))
    
favorate_color('김지영', '빨강', 1)
favorate_color('홍채영', '노랑', 2)
favorate_color('진소진', '파랑', 3)

# 매개 변수 *args
def average(*scores) : # 앞에 *를 붙이면, score가 범위형임을 의미
    sum = 0
    for i in range(len(scores)) :
        sum += scores[i]
    avg = sum/len(scores)
    print('%d과목의 평균 : %.2f' %(len(scores), avg))

average(80, 90, 100)
average(75, 80, 94, 78)
average(87, 60, 77, 95, 76)



# 함수 예시

# 전역변수(전 지역에서 활동하는 변수)
num = 3
num2 = num

for i in range(5) :
    num2 += 1

# 파라미터 = 지역변수(특정 지역에서만 활동하는 변수)
# 이름만 같은 것(= 전역변수와 지역변수의 이름이 동일할 수 있다.)
# 하지만 이름이 같은 경우, 지역변수가 우선이다.
def func(num) :
    num = 100
    print(num)

func(num)

print(num)


def circle_area(r) :
    area = r * r * 3.14
    return area

radius = int(input('원의 반지름을 입력하시오. : '))
result = circle_area(radius)
print('반지름 : %d, 원의 면적 : %.2f' %(radius, result))

radius = int(input('원의 반지름을 입력하시오. : '))
result = circle_area(radius)
print('반지름 : %d, 원의 면적 : %.2f' %(radius, result))


def sum(start, end) :
    total = 0
    for i in range(start, end+1) :
        total += i
    print('%d~%d의 정수 합계 : %d' %(start, end, total))

sum(10, 100)
sum(100, 1000)
sum(1000, 10000)


# 함수로 배수 합계 구하기
def sum_besu(n1, n2, num) :
    sum = 0
    for i in range(n1, n2+1) :
        if i % num == 0 :
            sum += i
    return sum

start = int(input('시작 수를 입력하세요. : '))
end = int(input('끝 수를 입력하세요. : '))
besu = int(input('합계를 구할 배수를 입력하세요. : '))

result = sum_besu(start, end, besu)

print('%d~%d의 정수 중 %d의 배수의 합 : %d' %(start, end, besu, result))

# 최대공약수
def computeMaxGong(x, y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            result = i 
    return result

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

max_gong = computeMaxGong(num1, num2)

print('%d과(와) %d의 최대공약수 : %d' % (num1, num2, max_gong))


# 람다 함수
x = lambda a : a**2

print(x(5))


# 람다 함수 사용 예시
f = lambda x, y, z : x + y + z
print(f(10, 20, 30))

def mul(n) :
    return lambda x : x * n

g = mul(3)
h = mul(5)

print(g(10))
print(h(10))

# 지역 변수와 전역 변수

1) 지역 변수(Local Variable)
  : 호출된 함수 내에서만 유효
2) 전역 변수(Global Variavle)
  : 하위의 모든 함수에서 유효



# 전역 변수의 사용 예시
def func() :
    print(x)
    print(id(x))

x = 10
print(x)
print(id(x))
func()

# 전역 변수의 값의 변경
def func() :
    x = 100
    print(x)
    print(id(x))

x = 10
print(x)
print(id(x))
func()

print(x)
print(id(x))

# 키워드 global
def func() :
    global x
    x = 100
    print(x)
    print(id(x))

x = 10
print(x)
func()
print(x)
print(id(x))
"""

# 05.02. 과제
"""
1) list 함수의 원리를 구현해보자, 숫자 123456을 list 형식으로
  ex)
   s = 12345

   list = []

   print(lst) # ['1', '2', '3', '4', '5', '6']
"""

# 2) 2차원 리스트
a = []

for i in range(5) : 
    b = []
    for j in range(5) :
        b.append(0)
    a.append(b)

for i in range(len(a)) : #[[0,0,0,0,0], [0,0,0,0,0,] ...]
    for j in range(len(a[i])) :
        a[i][j] = 5*i*j+1

for i in a :
    print(i)

# 1 6 11 16 21
# 2 7 12 17 22
# ...

# 3) 
# 1 2 3 4 5
# 10 9 8 7 6
# ...

# 4)
# 1 10 11 20 21
# 2 9 12 19 22
# ...

# 마지막 : pdf, 책 나오는 코드 작성해보기

