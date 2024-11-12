# 24.05.03 금일 코드

# 강사님 과제 코드
"""
s = 123456 # s에 123456 입력(숫자)
lst = [] # 리스트 공간 생성
i = 0

for i in int(s) : 
    lst.append(i) # lst 리스트에 i append(추가)


print(lst) # lst 출력


s = 123456
lst = []

while s > 0 :
    lst.append(s%10) # 6
    s = s//10 #12345

lst.reverse()

print(lst) # [1 2 3 4 5 6] 문제오류

# 또는 
# 특정 위치에 삽입
s = 123456
lst = []

while s > 0 :
    lst.insert(0, s%10) # 6 # 위치 지정 : 0
    s = s//10 #12345

print(lst)
"""


# 2번
# 1 6 11 16 21
# 2 7 12 17 22
# 3 8 13 18 23
# 4 9 14 19 24
# 5 10 15 20 25
"""
a = []

for i in range(5): 
    b = []
    for j in range(5): 
        b.append(0)
    a.append(b)

for i in range(len(a)): 
    for j in range(len(a[i])):
        a[j][i] = 5*i+j+1 # 또는 a[i][j] = 5*j + i+1로도 가능하다.

for i in a :
    print(i)
"""

# 1 2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
"""
a = []

for i in range(5): 
    b = []
    for j in range(5): 
        b.append(0)
    a.append(b)

for i in range(len(a)): 
    for j in range(len(a[i])):
        if i%2 == 0 :
            a[i][j] = 5*i+j+1
        else :
            a[i][j] = 5*i-j+5

for i in a :
    print(i)
"""

# 1 10 11 20 21
# 2 9 12 19 22
# 3 8 13 18 23
# 4 7 14 17 24
# 5 6 15 16 25
"""
a = []

for i in range(5): 
    b = []
    for j in range(5): 
        b.append(0)
    a.append(b)

for i in range(len(a)): 
    for j in range(len(a[i])):
        if j%2 == 0 :
            a[i][j] = 5*j+i+1
        else :
            a[i][j] = 5*j-i+5

for i in a :
    print(i)
"""

"""
# 어제 배웠던 내용 복습
# 함수 매개변수

# 1. 기본 인자값(Default Argument Values)
#   : 함수에 전달되는 기본 매개변수 값을 지정해주는 것

def func1(pa1, pa2=7, pa3=9) : # 함수의 기본 매개변수값을 지정해주었다.
    return 0

func1(1, 2, 3) # 이런식으로 지정해주어도 된다.
func1(1, 2) # pa1과 pa2엔 1, 2가 들어가지만, pa3엔 따로 지정값이 없기 때문에 기본값이 들어간다.
func1(1)

# 2. 키워드 인자(Keyword Argument)
#   : 함수에 전달되는 인자를 키-값 형태로 전달하는 것
#  - 순서와 상관없이 키값에 일치하는 곳에 값이 전달된다.

def greeting(name, message="Hello") : # 문자의 기본값 지정
    print(name, message)

greeting("철수", "안녕")
greeting(message="안녕", name="철수야")
greeting(name="영희")

# 3. 가변 인수 리스트(Arbitrary Argument Lists)
# 함수에 전달되는 매개변수 앞에 (*)을 붙여서 가변인수로 전달해주는 것
# 인자가 일렬로 나열돼서 전달되는데, tuple 형태로 전달된다.
def sum(*args) :
    res = 0
    for arg in args :
        res += arg
    
    return res

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 4. 위치 인자 리스트(Positional Argument Lists)
# 함수에 전달되는 매개변수 앞에 (**)을 붙여서 인자 리스트로 지정해주는 것
# 만약 함수를 호출했을 경우 key 값에 쌍의 형태로 전달되면 딕셔너리로 전달된다.
def greeting2(**kwargs) :
    for name, message in kwargs.items() :
        print(name, message)

greeting2(kim="안녕", lee="hello")
"""

# calc 함수를 만들어서 값을 더하거나 곱해준다.
# + : 모든 값을 더해준다.
# * : 모든 값을 곱해준다.
"""
def calc(*args) :

    if args[0] == "+" :
        res = 0 
        for arg in args[1:] : # 또는 for arg in args :
            res += arg

    elif args[0] == "*" : 
        res = 1
        for arg in args[1:] :
            res *= arg
    
    return res

print(calc('+', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # 55
print(calc('*', 1, 2, 3, 4, 5)) # 120
"""


"""
file = open("test.txt", "w")
file.write("hi?")
file.close()

file = open('test.txt', 'r', encoding='utf8')
lines = file.readlines()

print("test.txt 파일의 내용 : ")
for line in lines :
    print(line, end="")

file.close()
"""

"""
def matchWord(word, answer) :
    if word == answer :
        msg = '맞습니다!'
    else :
        msg = '틀렸습니다!' 
    return msg

eng_dict = {'orange':'오렌지', 'cookie':'과자', 'mother':'어머니', 'brother':'형 제', 'python':'파이썬'} 

for key in eng_dict : 
    string = input(eng_dict[key] + '에 맞는 영어 단어는? ') 
    result = matchWord(string, key)
    print(result)
"""

"""
def maxTwo(i, j):
    if i > j:
        return i
    else :
        return j
    
def maxThree(x, y, z) :
    max1 = maxTwo(x, y) 
    max2 = maxTwo(y, z)
    if max1 > max2 :
        largest = max1
    else :
        largest = max2 
    
    return largest

a = int(input('첫 번째 수를 입력하세요: ')) 
b = int(input('두 번째 수를 입력하세요: ')) 
c = int(input('세 번째 수를 입력하세요: '))

max_num = maxThree(a, b, c) 
print('%d, %d, %d 중 가장 큰 수 : %d' % (a, b, c, max_num))
"""

"""
file = open('test.txt', 'r', encoding='utf8') 
lines = file.readlines() 
file.close()

print('-' * 50) 

for line in lines : 
    student = line.split()
    i = 0
    sum = 0

    while i < len(student) :
        if i == 0 :
            print(student[i])
        else :
            sum += int(student[i])
        i += 1
    
    print('합계 : %d, 평균 : %.2f' % (sum, sum/6))
    print('-' * 50)
"""

"""
# 다이어리 프로그램
# 날짜 입력, 일기 작성, 날짜 입력-작성일기 출력

def menu() : 
    print("1 : Write a diary")
    print("2. Read a diary")
    print("3. Close a diary")

choice = int(input("어느 것을 선택하시겠습니까? : "))

def menu() :
    if choice == 1 :
        write_diary()
        return 0
    
    elif choice == 2 :
        read_diary()
        return 0 
    
    elif choice == 3 :
        return 1
    
def write_diary() :
    date = input("날짜를 입력하시오. (dd-mm-yyyy) : ")
    text = input("오늘의 하루는 어땠나요? : ")

    file = open(f"{date}.txt", "w")
    file.write(text)

    print("파일 저장이 완료되었습니다.")
    file.close()

def read_diary() :
    date = input("보고싶은 다이어리 날짜를 입력하시오. (dd-mm-yyyy) : ")

    file = open(f'{date}.txt', 'r')

    file.read()

    print(file.read())
    file.close()

while True :
    if menu() : 
        break
"""

# 위 코드를 res 형태로 변환
# 다이어리 프로그램
# 날짜 입력, 일기 작성, 날짜 입력-작성일기 출력
"""
def menu() : 
    print("1 : Write a diary")
    print("2. Read a diary")
    print("3. Close a diary")

choice = int(input("어느 것을 선택하시겠습니까? : "))

def menu() :
    if choice == 1 :
        write_diary()
        return 0
    
    elif choice == 2 :
        read_diary()
        return 0 
    
    elif choice == 3 :
        return 1
    
def write_diary() :
    date = input("날짜를 입력하시오. (dd-mm-yyyy) : ")
    text = input("오늘의 하루는 어땠나요? : ")

    with open(f"{date}.txt", "w") as file :
        file.write(text)
        print("파일 저장이 완료되었습니다.")

def read_diary() :
    date = input("보고싶은 다이어리 날짜를 입력하시오. (dd-mm-yyyy) : ")

    with open(f'{date}.txt', 'r') as f :
        print(f.read())

while True :
    if menu() : 
        break
"""

"""
# yesterday 개수 출력하는 코드
file = open('yesterday.txt', 'r', encoding='utf8')
yesterday = "" # testerday 저장해줄 공간 생성

while 1 :
    line = file.readline() # 한 줄씩 읽어와서 리스트화
    # readline : 한 줄 읽어오기

    if not line :
        break
    
    yesterday += line.strip() + "\n" # 문자열에서 공백 제거

file.close()


num = yesterday.lower().count("yesterday") # num에 yesterday을 카운트한 값 삽입
# lower(또는 upper)을 사용하여, 대소문자 구분없이 개수를 카운트해준다.
print(num) # num 출력




# Chapter 08 | 모듈과 패키지
# 모듈 : 여러 함수들이 선언되어있는 하나의 .py 파일
# 패키지 : 여러 개의 모듈을 그룹화한 것 (라이브러리)

"""

"""
import random

def whoWin(x, y) :
    if x == '가위' : 
        if y == '가위' :
            msg = '무승부입니다!'
        elif y == '바위' :
            msg = '당신의 승리입니다!'
        else :
            msg = '나의 승리입니다!'

    elif x == '바위' :
        if y == '가위' :
            msg = '나의 승리입니다!'
        elif y == '바위' :
            msg = '무승부입니다!'
        else :
            msg = '당신의 승리입니다!'

    else :
        if y == '가위' :
            msg = '당신의 승리입니다!'
        elif y == '바위' :
            msg = '나의 승리입니다!'
        else :
            msg = '무승부입니다!'
    return msg

print("=" * 30)
print("\t가위 바위 보 게임")
print("=" * 30)

gawibawibo = ['가위', '바위', '보']
again = 'y'

while again == 'y' :
    me = random.choice(gawibawibo) # 컴퓨터
    you = input("가위, 바위, 보 중 선택하시오. : ")

    result = whoWin(me, you)

    print("나 : %s" %you)
    print("상대 : %s" %me)
    print(result)
    print('-' * 30)

    again = input("계속해려면 y를 입력하시오.")
    print()

# 리스트 컴프리헨션
"""

"""
a = [i for i in range(10) if i == 0]
a = [i*0 for i in range(10)]
print(a)

# 또는

a = [0 for i in range(10)] # i를 사용하지 않음
a = [0 for _ in range(10)] # 사용하지 않을 변수를 보통 '_'로 많이 쓴다.
print(a)

word=["school", "game", "piano", "science", "hotel", "mountain"]
a = [i for i in word]
"""

"""
# 글자수가 6개 이상인 문자만 추가
word = ["school", "game", "piano", "science", "hotel", "mountain"]
b = [i for i in word if len(i) >= 6]
print(b)
"""

"""
# 또 다른 방법
word = ["school", "game", "piano", "science", "hotel", "mountain"]
b = [i for i in word if len(i) >= 6]
c = [word[i] for i in range(len(word)) if len(word[i]) >= 6]
d = [len(i) for i in word]

print(b)
print(c)
print(d)

# 100 이하의 소수(약수가 1과 자기자신뿐인)로 이루어진 1차원 리스트 생성
prime = []

for i in range(2, 101) : 
    for j in range(2, i) :
        if i % j == 0 :
            break
        elif i-1 == j : # j가 i전까지 도착을 했다면
            prime.append(i)

print(prime)
"""

"""
# 다른 유사 예시
prime = []

for i in range(2, 101) : 
    for j in range(2, i) :
        if i % j == 0 :
            break
        elif i-1 == j : # j가 i전까지 도착을 했다면
            prime.append(i)

# prime = [i for i in range(2, 101) if i%j != 0 for j in range(2, i)]
# 1) prime = [i]를 넣을거야
# 2) i가 뭔데? -> 2...100
# 3) 근데 i%j == 0이 되면 안돼.
# 4) j가 뭔데? -> 2...i-1
    #  ===> 이대로 삽입 불가능
# print(prime)
    # 따라서 다음과 같은 함수를 작성해야 함
    # all 또는 any 함수
    # 여러 개의 조건 또는 값이 있는 자료구조 값의 조건에 따라 True, False를 return하는 함수
"""

"""
# 1번 : all 함수
  # 모든 값이 True일 때, True
num = [i+1 for i in range(10)] # 1...10
lst = [x for x in num if x%2 == 0]

print(lst)

res = all(x%2 == 0 for x in lst)
print(res)


# 2번 : any 함수
  # 하나라도 True면 True
res = any(x == 5 for x in num)
print(res)

res = any(x == 5 for x in lst)
print(res)

prime = [i for i in range(2, 101) if all(i%j != 0 for j in range(2, i))]
# all의 디폴트값 때문에 2도 포함해서 결과값이 나온다.
print(prime)
"""

"""
# 2차원
lst = []

for i in range(5) :
    temp = ""
    for j in range(5) :
        temp += "*"
    lst.append(temp)

for i in lst :
    print(i)
print(lst)
"""

"""
lst = ["*****" for _ in range(5)]

print(lst)

lst2 = [["*" for i in range(5)] for _ in range(5)]
print(lst2)
"""


# 금일 과제

# alice.txt에서 단어가 몇 개 있는지
with open('alice.txt', 'r') as f :
    contents = f.read()

# 구두점 제거
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for punctuation in punctuations : 
    contents = contents.replace(punctuation, "") # 특수기호 제거

print(contents.split())
print(len(contents.split()))

# 과제 1
# 각 단어가 몇 개씩 있는지 카운트(딕셔너리)


# 과제 2
# 로또 번호 생성기 1~45, 7개, 중복 x(리스트 생성)
import random


# 과제 3
# 공통된 음식 찾기, 컴프리헨션 활용, all, any 사용하여 공통된 음식찾기(일단 두 명부터하면 쉬울 것)
person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]

