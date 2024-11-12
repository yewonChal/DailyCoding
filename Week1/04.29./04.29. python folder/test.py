# 10:17 컴퓨터에 관한 설명
# 컴퓨터는 1과 0, 덧셈밖에 사용하지 못한다.(이진법)
# 최초의 컴퓨터 (애니악) -> 전구 켜지면(1), 꺼지면(0)

# 연산속도가 굉장히 빠르다는 장점이 있다.

# ABCD, ㄱㄴㄷㄹ -> 아스키 코드(ASCII CODE)(a : 97 등)

# 언어 -> 고급언어(Python, JAVA 등) -> 어셈블리어 -> 기계어
# 컴파일러(통역사) -> 컴파일(번역)

# (#) : 주석 (컴퓨터가 읽지 못하는 메모(사람만 읽을 수 있는))

# 변수 : 컴퓨터에 데이터가 저장되는 메모리 공간의 위치

a = 20
b = 30
c = a + b
print(c)

# 변수명 규칙 : 영문 대소문자, 밑줄(_), 숫자를 조합하여 사용
    # 특수문자나 공백은 변수명에 사용할 수 없다.
    # 변수명은 숫자로 시작하면 안된다.
    # 영문에서 대문자와 소문자는 서로 다르다.

# 자주 쓰이는 데이터 유형
    # 숫자 : 20, 49, 9 0 -12
    # 문자열 : 'a', 'ㄱ'
    # bool(불) : True, False
    # 리스트 : ['홍길동', 32]
    # 튜플 : ('짜장면', '짬뽕')
    # 딕셔너리 : {'red':'빨간색'}

# 숫자 타입
    # 정수형(Integer) : 음수, 0, 양수로 구성된 숫자
    # 실수형(Float) : 소수 
print(type(c)) # c의 자료형을 파악하는 코드

x = 2.0
print(x)
print(type(x)) # x의 자료형을 파악하는 코드

# 문자열(String)
    # 하나 또는 여러 개의 문자로 구성
q = 'x'
w = 'Hello'
e = '안녕하세요.'

print(q) 
print(w)
print(e)

# 20과 '20'의 차이
r = 20
print(r)
print(type(r))

t = '20'
print(t)
print(type(t))

# 문자열의 인덱스  
    # 인덱스는 문자열 요소의 위치를 가르킨다.
    # 인덱스는 0부터 시작한다.
u = 'I am happy!'

print(u)
print(u[0])
print(u[0:3])
print(u[5:])
print(u[-1])
print(u[-3:])
print(u[-4:-2])

# 불 데이터형
s = True
d = False
print(a)
print(b)

f = 10 > 20
print(f)

print(type(s))

# 산술 연산자
    # + : 덧셈
    # - : 뺄셈
    # * : 곱셈
    # / : 나눗셈
    # % : 나머지 연산
    # // : 소수점 이하 절삭(몫)
    # ** : 거듭제곱

# 사칙 연산자
g = 10
h = 20 
j = g + h * 10 - 5 / 5
print(j)

k = 10 % 3
print(k)

l = 7//3
print(l)

print(2**3)

# 할당 연산자 : +=, *= 등
# = : 대입 연산자(우항(오른쪽) 값을 좌항(왼쪽)에 대입)
m = 10
m += 20 # 20만큼 더해준다.
m *= 10 # 10만큼 곱해준다.
print(m) # 출력하면 m의 기본값(10)에 20이 더해진 후 10이 곱해진 결과를 출력한다.

n = 20
v = 4

n = v % n
print(n)

v -= n*2
print(n, v)

# 문자열 반복 : *
hello = '안녕' * 5
print(hello)

# 문자열 길이 : len()
A = '쥐 구멍에 볕 들 날 있다.'
B = len(A)
print(B)

# 문자열 연결 : +
name = '홍길동'
greet = name+'님 안녕하세요.'
print(greet)

# 정수 -> 문자열 : str()
eng = 80
result = '영어점수 : ' + str(eng) + '점'
print(result)

# 문자열 포맷팅 : %s
C = '나는 %s입니다.' % name
print(C)

# 문자열 포맷팅 : %d
age = 23
D = '나이는 %d살 입니다.' % age
print(D)

# 문자열 포맷팅 : %2d
year = 2002
month = 12
day = 15

# 문자열 포맷팅 : %02d
E = '%d-%02d-%02d' % (year, month, day) # %02 (두 칸으로 작성, 남는 칸은 '0'으로 작성)
print(E)

# 문자열 포맷팅 : %.2f
height = 165.3
F = '키는 %.2f입니다.' % height # .2 (소수점 둘째자리까지 표시)
print(F)

# Format()을 이용한 문자열 포맷팅
eyesight = 1.2

Q = '이름 : {}'.format(name)
W = '나이 : {}세'.format(age)
E = '시력 : {}'.format(eyesight)

print(Q)
print(W)
print(E)

# 문자열 메소드
    # str.format() : 문자열 포맷팅하기
    # str.count() : 문자열 개수 세기
    # str.find() : 문자열 내부의 특정 문자열 찾기
    # str.upper() : 문자열 대문자로 바꾸기
    # str.lower() : 문자열 소문자로 바꾸기
    # str.replace() : 문자열 내부의 특정 문자열 바꾸기
    # str.split() : 문자열 분리하기
    # str.isspace() : 문자열에 공백이 있는지 체크하기

# 실행 결과 화면 출력 : print()
    # 콤마(,)를 이용한 출력
    # 문자열 연결 기호(+)를 이용한 출력
    # 문자열 포맷팅(%)을 이용한 출력
    # format()을 이용한 출력
    # 키워드 sep을 활용한 출력
print(year, month, day, sep=' ') # sep = ' '이 생략되어 있다.
print(year, month, day, sep='/')
    # 키워드 end를 활용한 출력
T = '안녕하세요.'
F = '반갑습니다.'

print(T)
print(F)

print('\n') # 줄 바꿈, \t은 탭을 의미, \v은 수직탭을 의미

print(T, end=' ')
print(F)

print(T) # end='\n'이 생략되어 있다.
print(F)

# 널(Null)과 개행문자(\n)
    # Null이란?
    # : 빈 문자열을 뜻하는 것으로 파이썬에서는 Null에 해당되는 것으로 None을 사용한다.

    # 개행문자란?
    # : 파이썬에서 줄바꿈을 할 때는 개행문자가 사용되는데, 개행 문자는 다른 말로 라인 피드라고도 불린다.

# 키보드 입력
NAME = input("이름을 입력하세요. : ")
print('%s님 반갑습니다.' %NAME)

# 키보드 입력받은 두 수 더하기
Z = input('첫 번째 숫자를 입력하시오. : ')
X = input('두 번째 숫자를 입력하시오. : ')

V = int(Z) + int(X)

print(V)

# 인치(inch)를 센티미터(cm)로 변환
inch = float(input('인치(inch)를 입력하시오. : '))
cm = inch * 2.54

print('센티미터 : %.2f' % cm)

# 주석문
# 한 문장 주석 : #
# 긴 문장 주석 : """  """
"""
프로그램 명 : 두 수 더하기
작성자 : 홍길동
작성일 : 2021.09.20.
"""

K = 10
L = 20

J = K + L
print(J)

# 삼각형의 면적 구하기
width = 10
height = 3
area = width * height / 2

print('삼각형의 밑변 길이 : ', width)
print('삼각형의 높이 : ', height)
print('삼각형의 면적 : ', area)

# 거스름돈 계산하기
price = 800
buy = 3
pay = 5000
change = pay - price * buy

print('물건가격 : ', price, '원')
print('구매개수 : ', buy, '개')

# 문자열 추출과 문자열 포맷팅
print('성 : ', name[0])
print('이름 : ', name[1])
print("%s의 나이 : %d세, 키 : %.2fcm" %(name, age, height))

# 성적 평균 구하기
Name = input('학생 이름을 입력하시오. : ')
kor = int(input('국어 성적을 입력하시오. : '))
eng = int(input('영어 성적을 입력하시오. : '))
math = int(input('수학 성적을 입력하시오. : '))

total = kor + eng + math
avg = total / 3

print('이름 :%s, 국어 : %d, 영어 : %d, 수학 : %d, 평균 : %.1f점'%(Name, kor, eng, math, avg))


# Chapter 3
# --- 조건문
    # : 조건에 따라 다른 프로그램 코드를 실행
        # '만약 ~ 하면 ~하다.'와 같은 상황에서 사용된다.
        # ex) 점수가 80점 이상이면 합격이고 80점 미만이면 불합격이다.

    # 조건문은 들여쓰기에 유의하여 작성해야 한다.

# 양수 판별 프로그램
Xx = int(input('숫자를 입력하시오. : '))

if Xx > 0 :
    print('양수입니다.')
else :
    print('0 또는 음수입니다.')
    Xx *= -1
    print('%d, 양수로 바꾸었을 때 다음과 같은 결과를 나타냅니다.' %Xx)

# 비교 연산자와 논리 연산자
    # 비교 연산자 : >, <, ==(같다.), !=(같지않다.), >=, <=
        # 비교 후 결과에 알맞는 True 또는 False를 출력한다.
Qq = 10 
Ww = 3

print(Qq > 9)
print(Ww <= 10)
print(Qq + Ww == 13)
print(Qq % 2 == 0)
print(Ww % 2 == 0)
print(Qq % 4 == 0)
print(Ww % 3 != 0)

        # ex) 짝수/홀수 판별 코드
num = int(input('숫자를 입력하세요. : '))

if num % 2 == 0 :
    print('짝수이다.')
else : 
    print('홀수이다.')

    # 논리 연산자 : AND, OR, NOT
        # 추가적인 조건이 필요할 때 많이 쓰인다.
        # 조건1 AND 조건2 : 둘 다 참이어야 참 출력
        # 조건1 OR 조건2 : 하나만 참이어도 참 출력
        # NOT 조건 : 조건이 참이면 그 결과는 거짓, 조건이 거짓이면 그 결과는 참 출력

        # ex) 시험 합격/불합격 판정
score1 = int(input('필기성적을 입력하시오. : '))
score2 = int(input('실기성적을 입력하시오. : '))

        # ex) 홈페이지 관리자 판별
id = input('아이디를 입력하시오. : ')
level = int(input('회원 레벨을 입력하시오. : '))

if id == 'admin' or 'lever' == 1 :
    print('관리자입니다.')
else:
    print('관리자가 아닙니다.')

        # ex)   


print(5 < 6) # True
print(not (5 == 7)) # True(not False)

Bb = 1
print(1 < Bb and Bb < 10)

Cc = -1
# Bb, Cc 둘 중 하나라도 음수인지?
print(Bb < 0 or Cc < 0)

# age가 65세 이상 혹은 13세 이하인지?
print(age >= 65 or age <= 13)

# ID, PW를 입력하여 판별하는 코드
answerID = 'abcde'
answerPW = '12345'

ID = input("아이디를 입력하시오. : ")
PW = input("비밀번호를 입력하시오. : ")

if ID == answerID and PW == answerPW : 
    print("아이디와 비밀번호가 일치합니다.")
else :
    print("아이디와 비밀번호가 일치하지 않습니다.")

# if~ elif~ else~ 구문의 사용 예시
Score = int(input('점수를 입력하시오. : '))

if Score >= 90 :
    grade = 'A'

elif Score >= 80 :
    grade = 'B'

elif Score >= 70 :
    grade = 'C'

elif Score >= 60 :
    grade = 'D'

else : 
    grade = 'F'

print('성적 : %d' %Score)
print('등급 : %s' %grade)

# if~ 구문으로 월을 입력받아 계절 표시하기
Month = int(input('월을 입력하시오. : '))

if Month >= 3 and Month <= 5 :
    print('%d월은 봄입니다.'%Month)

if Month >= 6 and Month <= 8 :
    print('%d월은 여름입니다.'%Month)

if Month >= 9 and Month <= 11 :
    print('%d월은 가을입니다.'%Month)

if Month == 12 or Month == 1 or Month == 2 :
    print('%d월은 겨울입니다.'%Month)

# if~ 구문으로 4의 배수 / 5의 배수 판별하기
Yy = int(input('숫자를 입력하세요. : '))

if Yy%4 == 0 :
    print('%d은(는) 4의 배수이다.' %Yy)

elif Yy%5 == 0 :
    print('%d은(는) 5의 배수이다.' %Yy)

else :
    print('%d은(는) 4의 배수도 5의 배수도 아니다.')

# 또는

Yy = int(input('숫자를 입력하세요. : '))

if Yy%4 == 0 or Yy%5 == 0 :
    print('%d은(는) 4의 배수 또는 5의 배수이다.' %Yy)

else :
    print('%d은(는) 4의 배수도 5의 배수도 아니다.')

# if~ else~ 구문으로 모음/자음 판별하기
char = input('영어 알파벳을 입력하시오. : ')
char2 = char.upper()

if char2 == 'A' or char2 == 'E' or char2 == 'I' or char2 == 'O' or char2 == 'U' :
    print('%s은(는) 모음이다.' %char2)
else :
    print('%s은(는) 자음이다.' %char2)

# if~ else~ 구문으로 체형 판별하기
Height = int(input('키를 입력해주세요. : '))
Weight = int(input('몸무게를 입력해 주세요. : '))
Ll = (Height - 100) * 9.0

print('-'*30)
print('키 : %dcm' %Height)
print('몸무게 : %dkg' %Weight)

if Weight > Ll :
    print('정상 체중입니다.')
else : 
    print('마름입니다.')

# if문으로 나이 계산하기
now_year = int(input('현재년을 입력해주세요 : '))
now_month = int(input('현재월을 입력해주세요. : '))
now_day = int(input('현재일을 입력해주세요. : '))

birth_year = int(input('출생년을 입력해주세요 : '))
birth_month = int(input('출생월을 입력해주세요 : '))
birth_day = int(input('출생일을 입력해주세요 : '))

if now_month >= birth_month and now_day >= birth_day :
    Age = now_year - birth_year
    print('생일이 지났습니다.')

else :
    Age = now_year - birth_year -1
    print('생일이 지나지 않았습니다.')

print('-------------------------')
print('오늘 날짜 : %d년 %d월 %d일' %(now_year, now_month, now_day))
print('생년월일 : %d년 %d월 %d일' %(birth_year, birth_month, birth_day))
print('-------------------------')

print('나이 : %0d세' %age)
# ---> and와 중첩조건문은 같다.


# Chapter 04
# 반복문
    # 특정 코드를 반복 실행

    # for문으로 반복 출력하기
for Oo in range(5) :
    print('안녕하세요')

    # while문으로 반복 출력하기
Pp = 0 
while Pp < 5 :
    print('안녕하세요.')
    Pp += 1

# 1~10의 합계
sum0 = 0

for i in range(1, 11) : 
    sum0 += i # i에 차례로 하나씩 삽입
    print('i의 값 : %d, 합계 : %d' %(i, sum))

# range() 함수
for i in range(10) :
    print(i, end =' ')
print()

for i in range(1, 11) :
    print(i, end =' ')
print()

for i in range(1, 10, 2):
    print(i, end =' ')
print() # 줄 바꿈과 같은 의미

for i in range(20, 0 -2) :
    print(i, end =' ')

# 3의 배수의 합계
sum3 = 0
for i in range(1, 101) :
    if i%3 == 0 :
        print('%d' % i, end =' ')
        sum3 += i

    print('\n', '-' * 50)
    print('1~100에서 3의 배수의 합계 : %d' %sum3)

# 문자열 세로 출력
word = input('영어 문장을 입력하세요. : ')

for Uu in word :
    print(Uu)

# 섭씨 온도를 화씨로 변환
print('-' * 30)
print(' 섭씨 화씨')
print('-' * 30)

for Ccc in range(-20, 31, 5) :
    Fff = Ccc * 9.0 / 5.0 + 32.0
    price("%8d %6.1f" %(Ccc, Fff))

print('-' * 30)

# 5의 배수가 아닌 수의 합계 구하기(for문의 경우)
n1 = int(input('시작 수를 입력하시오. : '))
n2 = int(input('끝 수를 입력하시오. : '))
sum12 = 0

for i in range(n1, n2+1) :
    if i % 5 != 0 :
        sum12 += i

print('-' * 50)
print('%d에서 %d까지 5의 배수가 아닌 수의 합계 : %d' %(n1, n2, sum12))


# 숙제

# 1. 키오스크 만들기
# 메뉴를 선택해주세요 (메뉴1 -> 가격, 메뉴2 -> 가격, 메뉴3 -> 가격) : (입력)
# 금액을 넣어주세요 : (입력)
# 잔액이 부족합니다. or (메뉴)가 나왔습니다. 거스름돈 ??원이 나왔습니다.

print('메뉴1 : 아이스아메리카노, 3000원 \n메뉴2 : 카페라떼, 3800원 \n메뉴3 : 카페모카, 4500원')
print('메뉴를 선택해주세요. : %s')


# 2. a = 10, b= 20, c = 30  ==> 이것을 보도 c가 가장 크다고 출력할 수 있는 코드 작성(3가지 방법으로 출력)

# 3. pdf, 책에 나오는 내용을 코드로 옮겨보기
