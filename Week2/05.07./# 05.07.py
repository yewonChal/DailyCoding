# 05.07. python code

# alice.txt에서 단어가 몇개 있는지
"""
with open('alice.txt', 'r') as f:
    contents = f.read()

#구두점 제거
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for punctuation in punctuations:
    contents = contents.replace(punctuation, "")

print(contents.split())
print(len(contents.split()))

# 1. 각 단어가 몇 개씩 있는지 (딕셔너리)
c = contents.lower()
words = c.split()

print(words)

words_count = {} # key : 단어, value : 개수
for word in words :
    if word in  words_count :
        words_count[word] += 1
    else :
        words_count[word] = 1 # 딕셔너리에 들어있지 않을 때(단어가 처음 나왔을 때)

for word, count in words_count.items() :
    print(word, ":", count)
"""

# 2. 로또 번호 생성기 1~45, 7개, 중복되지 않는 리스트
"""
import random

numbers = []

for _ in range(7) :
    num = (random.randint(1, 45))

    if num in numbers : # 이미 들어가있는 번호라면,
    # 하지만 문제는 뒤 if문에서도 중복이 발생할 수 있다
        num = random.randint(1, 45)
    else :
        numbers.append(num)

    # 따라서
    while num in numbers :
        num = random.randint(1, 45)
    
    numbers.append(num)

numbers.sort()
print(numbers)
"""

# 3. 공통된 음식 찾기 (컴프리헨션)
# all, any를 사용하여 공통된 음식 찾기 (일단 두명부터)
"""
person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]

first_two_people = [food for food in person1 if food in person2]
print(first_two_people)

common_foods = [food for food in set(person1) & set(person2) & set(person3)]
print(common_foods)
"""

"""
person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]

res = any(food in person2 for food in person1)
print(res)

foods = [food for food in person1 if any(food == food2 for food2 in person2)]
print(foods)

lst = [food for food in foods if any(food == food3 for food3 in person3)]
print(lst)
"""

"""
# 컬렉션 : '파이썬에서 여러 요소들은 한 번에 저장하고 처리할 수 있게 만들어진 데이터 구조'이다.
# ex_ 리스트, 튜플, 딕셔너리

# 집합(Set) : '순서가 없고, 중복된 값을 허용하지 않는 요소의 모음'이다.
# 중괄호 {} 를 사용한다. 단일 데이터만 요소로 가진다.(딕셔너리는 두 개씩임을 유의하며 구분한다.)

s = {1, 2, 3}

print(s)

s.add(3)
print(s)

s.add(4)
print(s)

person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]

menu1 = set(person1)
print(person1)
menu2 = set(person2)
print(person2)
menu3 = set(person3)
print(person3)

# 합집합(|), 교집합(&)
print(menu1 & menu2 & menu3)
print((menu1 & menu2) | (menu1 & menu3) | (menu2 & menu3))
print(menu1 | menu2 | menu3)
"""

# 파일 입출력

# 모드
    # "r" : 읽기모드
    # "w" : 쓰기모드(기존 데이터를 모두 삭제하고 새로 작성)
    # "r+" : 읽기와 쓰기를 모두 사용할 수 있는 모드
    # "a" : 추가모드(기존 파일에 데이터를 추가하기 위해 사용(이어쓰기))
    # "x" : 생성모드(파일을 생성해주는 모드, 이미 파일이 있는 경우엔 에러 발생)
    # "t" : 텍스트모드(텍스트 데이터를 다루기 위해 사용(기본값))
    # "b" : 바이너리 모드(바이너리 데이터를 다루기 위해 사용)
        # 바이너리 데이터(이진 데이터) : 일반적으로 0과 1로 이루어진 데이터
        # (기존 단위가 2개의 상태만 가지는 데이터)
            # "rb" : 읽기 바이너리 모드
            # "wb" : 쓰기 바이너리 모드
            # "ab" : 추가 바이너리 모드
            # "xtb" : 생성모드
            # "rb+", "wb+", "ab+""

"""
# 재귀함수(recusion function)
# 1. 함수 내부에서 자기 자신 함수를 호출헤야 한다.
# 2. 재귀를 종료시켜주는 조건문이 존재해야 한다.
def test(end) :
    if end == 0 :
        return
    test(end - 1)
    print(end)

test(5)

# 람다식 : lambda는 '익명 함수를 생성하는 키워드'이다.

# lambda argments : expression

def add(x, y) :
    return x+y

add_lambda = lambda x, y : x+y
# lembda : 람다 키워드
# argments : 매개변수 x, y
# expression : 표현식 x+y

print(add(3, 4))
print(add_lambda(3, 4))

# map 함수
# 주어진 함수를 반복 가능한(iterable) 객체의 각 원소에 적용하고 결과를 반복한다.

def square(x) :
    return x*x

lst = [1, 2, 3, 4, 5]
square_lst = map(square, lst)
print(list(square_lst))

# 람다로 바꿔보기
lst = [1, 2, 3, 4, 5]
square_lst = map(lambda x : x*x, lst)
print(list(square_lst))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 반복문
for i in range(len(a)) :
    if a[i] % 2 == 0 :
        a[i] = 0
print(a)

# 람다함수
def f(x) :
    if x % 2 == 0 :
        return 0
    else : 

        return x

for i in range(len(a)) :
    a[i] = f(a[i])

print(a)

# map
print(list(map(f, a)))
print (list(map(lambda x : 0 if x%2 == 0 else x, a)))


# filter gkatn
# 주어진 함수를 반복 가능한(iterable) 객체의 결과가 참인 요소들만 반환한다.

# filter(function, iterable)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x) : # return 값이 boolean
    return x%2 == 0

even_list = filter(is_even, a)
print(list(even_list))

# 람다식으로 변환
odd_list = filter(lambda x : x%2 == 1, a)
print(list(odd_list))
"""

"""
# 시험 성적 별 합격, 과락 판별
scores = [12, 30, 90, 70, 60, 40, 80, 55, 85, 92, 100, 77, 66]
# 70점 이상 -> 합격, 60점 미만 -> 불합격
print(list(map(lambda x : '합격' if x >= 70 else "재시험" if x >= 50 else "불합격", scores)))
# --- 내가 적은 코드
def f(x) : 
    if x >= 70 :
        print("합격")
    elif x < 50 :
        print("불합격")
    elif 50 <= x <= 69 :
        print("재시험")
    else :
        print("잘못 입력된 점수가 존재합니다.")
    return 0

x_list = filter(f, scores)
print(list(x_list))

# 파일 형식이 jpg인 파일들만 불러오기
files = ["memo.txt", "1.jpg", "dog.jpg", "cat.jpg", "bird.png", "05-07.txt"]
print(list(filter(lambda x : '.jpg' in x, files)))
# 또는
print(list(filter(lambda x : x.find(".jpg") != -1, files)))
# --- 내가 적은 코드
files = ["memo.txt", "1.jpg", "dog.jpg", "cat.jpg", "bird.png", "05-07.txt"]
def f(y) :
    if y == 'jpg' :
        print(y)
    else :
        y = 0    
    return 0

y_list = filter(f, files)
print(list(y_list))

# 리스트 세 개의 곱
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 3, 5, 7, 9]
lst3 = [2, 4, 6, 8]

print(list(map(lambda x, y, z : x*y*z, lst1, lst2, lst3)))
print(list(zip(lst1, lst2, lst3)))
"""


# Chapter 09 | 객체지향 프로그래밍

# 객체지향 프로그래밍
    # 객체 : 클래스로부터 생성되어 클래스의 속성과 메소드를 가진다.
    # 클래스 : 객체에서 사용되는 속성과 메소드를 정의한 틀
    # 속성 : 클래스와 객체에서 사용되는 변수
    # 메소드 : 클래스와 객체에서 사용되는 함수

    # 보다 쉽게 이해하기 위해_
    # 클래스(와플기계)(=설계도), 객체(와플) | 1:N 관계

# 객체지향 예시
"""
class Calculator :
    def set(self, x, y) :
        self.first = x
        self.second = y

    def add(self) :
        result = self.first + self.second
        return result

cal1 = Calculator()

cal1.set(10, 20)
print('%d + %d = %d' %(cal1.first, cal1.second, cal1.add()))

cal1.set(100, 200)
print('%d + %d = %d' %(cal1.first, cal1.second, cal1.add()))

cal2 = Calculator()

cal2.set(30, 40)
print('%d + %d = %d' %(cal2.first, cal2.second, cal2.add()))
"""

# 변수 -> 컬렉션 -> 함수 -> 모듈 -> 객체
# 생성자 : 객체를 생성할 때, 값을 전달해주려고 존재하는 코드
# 생성과 동시에 전달해주기 위해
# 속성(인스턴스 변수) : 각 객체가 가지고 있는 변수
"""
class Member :
    def __init__(self, name, age) : # __init__ : 생성자 메소드
        self.name = name
        self.age = age

    def showMember(self) :
        print('이름 : %s' % self.name)
        print('나이 : %d' % self.age)

mem1 = Member('홍지수', 24)
mem1.showMember()
mem2 = Member('안지영', 20)
mem2.showMember()
"""

#생성자 또 다른 예시
"""
class Dog :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def sayHello(self) :
        print("멍멍")
        print("야옹")

    def ageCal(self) :
        print("사람 나이로 환산하면 %d세입니다." %(24+(self.age - 2)*4))

    def compareToAge(self, personAge) :
        return 24+(self.age - 2)*4 > personAge
                
dog = Dog("뽀삐", 3)
dog.sayHello()
dog.ageCal()

class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        # self.arr = [1, 2, 3] 형식으로도 삽입이 가능하다.
        # self.job = "데이터 분석가" 형식으로도 삽입이 가능하다.
    
    def sayHello(self) :
        print("안녕하세요. 저의 이름은 {}입니다.".format(self.name)) 

    def ageCal(self) :
        print("저는 %d살입니다." %(self.age))

    def compareToDog(self, dog) :
        if 24 + (dog.age-2)*4 > self.age :
            print("{}의 나이가 {}의 나이보다 많습니다.".format(dog.name, self.name))
        else :
             print("{}의 나이가 {}의 나이보다 적습니다.".format(dog.name, self.name))

person = Person("홍길동", 22)
person.sayHello()
person.ageCal()

print(dog.compareToAge(person.age))
# True라면, 강아지의 사람나이가 더 크다.
# False라면, 사람나이가 강아지보다 크다.
person.compareToDog(dog) # 반드시 dog를 전달해줘야 한다.(속성으로 name과 age있는 걸 전달해야 한다.)
person.compareToDog(Dog("뽀삐", 1)) # 객체 생성과 동시에 객체 활용(뽀삐 나이와 1을 비교)
"""

# 클래스 속성
"""
class MyClass :
    number = 100 # 클래스 속성
    def inc_10(self):
        MyClass.number += 10
    
    def inc_20(self):
        MyClass.number += 20

obj1 = MyClass()
obj1.inc_10()
print(obj1.number)
obj2 = MyClass()
obj2.inc_20()
print(obj2.number)
"""

# 인스턴스 속성
"""
class MyClass :
    def __init__(self, number) :
        self.number = number # 인스턴스 속성
    
    def inc_10(self):
        self.number += 10
    
    def inc_20(self):
        self.number += 20

obj1 = MyClass(100)
obj1.inc_10()
obj1.inc_20()
print(obj1.number)

obj2 = MyClass(200)
obj2.inc_10()
obj2.inc_20()
print(obj2.number)
"""

# 객체지향 원의 면적과 원주
"""
import math

class Circle :
    def __init__(self, radius) :
        self.radius = radius # 인스턴스 변수
    
    def getArea(self) :
        area = math.pi * self.radius * self.radius # 지역 변수
        return area

    def getCircum(self) :
        circum = 2 * 3.141592 * self.radius
        return circum

cir = Circle(10)

print('반지름: %d' % cir.radius)
print('원의 면적 : %.2f' % cir.getArea())
print('원주의 길이 : %.2f' % cir.getCircum())
"""

# 객체지향 합계 / 평균
"""
class SumAvg :
    title = '- 3과목 합계와 평균'

    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math 
    
    def getSum(self) :
        sum = self.kor + self.eng + self.math
        return sum
    
s1 = SumAvg('김성윤', 85, 90, 83)
print(SumAvg.title) 
print('이름 : %s' % s1.name) 
print('국어 : %d, 영어 : %d, 수학 : %d' % (s1.kor, 
s1.eng, s1.math)) 
print('합계 : %d, 평균 : %.1f' %(s1.getSum(), s1.getSum()/3.0))
"""

# 생성자 매개변수 리스트
"""
class Person :
    def __init__(self, info) :
        self.info = info

    def getName(self) :
        return self.info[0]

    def getEmail(self) :
        return self.info[1]

    def getPhoneNum(self) :
        return self.info[2]

info = ['김지혜', 'rubato@hanmail.net', '010-1234-4567'] 
person = Person(info)
print('성명 : %s' % person.getName()) 
print('이메일 : %s' % person.getEmail()) 
print('전화번호 : %s' % person.getPhoneNum())
"""

# 객체지향 문자열 다루기
"""
class EngSentence :
    def __init__(self, sentence) :
        self.sentence = sentence
        self.length = len(self.sentence)
    
    def reverse(self) :
        tmp = ''
        for i in range(self.length) : 
            tmp += (self.sentence[self.length-i-1])
        return tmp

    def insertHypen(self) :
        tmp = ''
        for i in range(self.length) :
            if self.sentence[i] == ' ' :
                tmp += '-'
            else :
                tmp += self.sentence[i]
        return tmp

a = 'We are the champions!' 
eng1 = EngSentence(a) 
print('역순 : %s' % eng1.reverse()) 
print('하이픈(-) 삽입 : %s' % eng1.insertHypen())
"""

"""
class MyClass : 
    number = 100 # 클래스 생성

    def inc_10(self) :
        MyClass.number += 10
    
    def inc_20(self) :
        MyClass.number += 20
    # 같은 글래스를 공유하고 있기 때문에 같은 이름을 작성해주어야 한다.

obj1 = MyClass()
obj1.inc_10()
print(obj1.number)
print(MyClass.number) # 접근이 가능하다.
"""

# 학생 클래스(학번, 이름), 자기소개
# 학번 학생 객체가 생성될 때마다 1부터 순서대로 부여할 수 있도록
"""
class Student :
    num = 1
    def __init__(self, number, name) :
        self.number = Student.num
        self.name = name
        Student.num += 1
    
    def student(self) :
        print("안녕하세요. 저는 %s %s입니다." %(self.number, self.name))


s1 = Student('20211111', '홍길동')
s1.student()
s2 = Student('20212222', '안예은')
s2.student()
s3 = Student('20213333', '안재현')
s3.student()


# 또는 
s1 = Student('홍길동')
s2 = Student('안예은')
s3 = Student('안재현')

s1.student()
s2.student()
s3.student()
"""
# 다시

# 생성자 예시
"""
class Calculator :
    num = 1
    # 생성자 : 객체가 생성될 때, 처음에 한 번 실행되는 메소드
    # 기본 생성자
    # def __init__(self) : 기본 생성자는 작성하지 않을 수 있다.
    def __init__(self) : 
        Calculator.num += 1
    
    def set(self, x, y) :
        self.first = x
        self.second = y

    def add(self) :
        return self.first + self.second
    
cal1 = Calculator()

cal1.set(10, 20)
print("%d + %d = %d" %(cal1.first, cal1.second, cal1.add()))
"""

# 또 다른 예시
"""
class Member : 
    def __init__(self, name, age = 20, *hobbies, **scores) : # 기본 인자, 키워드 인자, 가변인수 리스트, 위치 인지 리스트
        self.name = name # 
        self.age = age
        self.hobbies = hobbies
        self.scores = scores

member = Member("Kim", age = 30)
"""

# 금일 과제
"""
1. 사람 3명이 각각 음식을 가지고 있다. 여러분들이 person1이라고 가정하고, 다른 두 명과 음식을 교환해보자.
   (이미 갖고있는 음식은 교환이 불가하다.)
person1 = []
person2 = []
person3 = []

while True :
    print(person1)
    print(person2)
    print(person3)

    inputSet = int(input("1. 교환하기 2. 종료하기"))
"""

"""
2. str = '' # 몇 개의 jpg가 들어가 있는지 확인
   (반복문, 컴프리헨션으로 작성)
"""