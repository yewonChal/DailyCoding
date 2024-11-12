# 05.08. python code
# 과제2 또 다른 코드
"""
str = 'jpgpgjgpjpgjgpjgpjgpjpgjpjgp'

num = 0

for i in range(len(str) - 2) :
    if str[i] + str[1+i] + str[i+2] == 'jpg' :
        num += 1

print(num)

a = []

while 'jpg' in str :
    i = str.index('jpg')
    a.append(str[i:i+3])
    str = str[:i] + str[i+3:]

print(a)
print(len(a))

res = list(filter(lambda x : x[0] == 'j', [str[i:i+3] for i in range(len(str) - 2)]))
print(res)

res = list(filter(lambda y : y == 'jpg', res))
print(res)
"""

# class 외부에 두 개
"""
from notebook import Note
from notebook import NoteBook

# from 파일명 import 클래스명
# notebook.py - 파일명
# Note, NoteBook - 클래스명

good_sentence = "세상사는데 도움이되는 명언들 힘이되는 명언 용기를 주는 명언 위로가되는 명언 좋은명언 글귀 모음 100가지 자주 보면 좋을듯 하여 선별 했습니다."
note1 = Note(good_sentence)
print(note1)

good_sentence = "삶이 있는 한 희망은 있다 -키케로 "
note2 = Note(good_sentence)
print(note2)

good_sentence = "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다.-사무엘존슨"
note3 = Note(good_sentence)
print(note3)

good_sentence = "행복의 문이 하나 닫히면 다른 문이 열린다 그러나 우리는 종종 닫힌 문을 멍하니 바라보다가 우리를 향해 열린 문을 보지 못하게 된다  - 헬렌켈러"
note4 = Note(good_sentence)
print(note4)

notebook = NoteBook("명언노트")
notebook.add_note(note1)
print(notebook.get_number_of_all_pages())

notebook.add_note(note2)
print(notebook.get_number_of_all_pages())

notebook.add_note(note3)
notebook.add_note(note4)
print(notebook.get_number_of_all_pages())
print(notebook.get_number_of_all_characters())

notebook.remove_note(3)
print(notebook.get_number_of_all_pages())

notebook.add_note(note3, 100)
notebook.add_note(note3, 100)

for i in range(300):
    notebook.add_note(note1, i)

print(notebook.get_number_of_all_pages())

notebook.add_note(note3, 100)
notebook.add_note(note3, 100)
"""

"""
class Note(object):
    def __init__(self, contents):
        self.contents = contents

    def get_number_of_lines(self):
        return self.contents.count("\n")

    def get_number_of_characters(self):
        return len(self.contents)

    def remove(self):
        self.contents = "삭제된 노트입니다"

    def __str__(self): # 객체를 출력할 때, 주소값 대신 나오는 역할
        return self.contents

class NoteBook(object):
    def __init__(self, name):
        self.name = name
        self.pages = 0
        self.notes = {}

    def add_note(self, note, page_number=0):
        if len(self.notes.keys()) < 300:
            if page_number == 0:
                if self.pages < 301:
                    self.notes[self.pages] = note
                    self.pages += 1
                else:
                    for i in range(300):
                        if i not in list(self.notes.keys()):
                            self.notes[self.pages] = note
                            break
            else:
                if page_number not in self.notes.keys():
                    self.notes[page_number] = note
                else:
                    print("해당 페이지에는 이미 노트가 존재합니다")
        else:
            print("더 이상 노트를 추가하지 못합니다.")

    def remove_note(self, page_number):
        del self.notes[page_number]

    def get_number_of_all_lines(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_lines()
        return result

    def get_number_of_all_characters(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_characters()
        return result

    def get_number_of_all_pages(self):
        return len(self.notes.keys())

    def __str__(self):
        return self.name
"""

"""
class Animal:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def printSound(self):
        print(self.sound)

dog1 = Dog('행복이', '멍멍~~~')
dog1.printName()
dog1.printSound()
"""

# 사람 클래스(이름, 나이)
# Korean 사람 클래스(자식 클래스)
"""
class Person : # class Person(object) : object = 모든 객체지향 언어의 공통점(모든 클래스의 최상의 부모)(생략 가능))
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def printNameAge(self) :
        print(self.name)
        # print(self.age)

class Korean(Person):
    # pass : 여기에 코드를 작성할건데, 아직은 아니야
    def __init__(self, name, age, nation) :
        super().__init__(name, age)
        # super().__init__(age)
        self.nation = nation
    # 위 코드를 주석처리해도 밑에서 이름과 나이가 제대로 출력하는 모습(약간의 수정은 필요)
    # = 생성자를 작성하지 않으면, 기본 생성자 def__init__(self) 생성
    # 하지만, 상속관계라면, super().__init__()까지 기본 생성자가 숨겨져있다.(부모생성자가 숨겨져 있다.)

    def printPerson(self):
        print(self.name, self.age, self.nation) # 부모 내용을 맘대로 불러오는 모습(잼민이!)
    
person1 = Korean('Choi', 20, 'Korean')
print(person1.name)
print(person1.age)
print(person1.nation)

person1.printPerson()
"""

# super() 함수
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print('이름:%s, 나이:%d' % (self.name, self.age))

    def getInfo(self) :
        return self.name + ', ' + str(self.age)
    
class Student(Person):
    def __init__(self, name, age, department, id):
        super().__init__(name, age)
        self.department = department
        self.id = id

    def printStudentInfo(self):
        name_age = super().getInfo()
        print(name_age)
        print('%s님의 학과:%s, 학번:%s' % (self.name, self.department, self.id))

x = Student('홍지수', 20, '소프트웨어공학과', '20215550001')
x.printInfo()
x.printStudentInfo()
"""

# 추가 지식
# pickle 모듈
"""
import pickle
# 파이썬에 딕셔너리, 리스트, 클래스 - 자료구조, 객체 등을 자료형 변환없이 그대로 파일에 저장하고 싶을 때 사용
# 인수가 여러 개일 때, 게시판(1. 글 번호, 2. 글 제목, 3. 글 내용 ...)

data = {"no" : 1, "title" : "제목", "content" : "내용"}

print(data)

with open("data.p", "wb") as f :
    pickle.dump(data, f)

d = dict()
print(d)

with open('data.p', 'rb') as f :
    d = pickle.load(f)

print(d)

# 입력, 조회, 삭제, 종료
num = 0

def menu() :
    user = int(input("메뉴를 선택해주세요.(1_입력, 2_조회, 3_삭제, 0_종료) : "))

    if user == 1 :
        global num
        num += 1
        # 입력해주는 코드
        title = input("글 제목 : ")
        content = input("글 내용 : ")

        write(title, content)

        print('메뉴 ', write, '가 입력되었습니다.')

    elif user == 2 :
        # 조회해주는 코드
        load()

    elif user == 3 :
        # 삭제해주는 코드
        delete = int(input("삭제할 번호를 입력하시오. : "))
        remove(delete)

    else : 
        # 종료
        print("종료되었습니다.")
        return 1
    
    return 0

def write(num, title, content) :
    dic = {'no' : num, 'title' : title, 'content' : content}
    lst = []

    with open('data.p', 'rb') as f :
        item = pickle.load(f)

    if item != "" :
        if type(item) == dict :
            lst.append(item)
        elif type(item) == list :
            lst += item
        
    lst.append(dic)

    write open('data2.p', 'wb') as f :
        pickle.dump(lst, f)
    
def load() :
    with open("data2.p", "rb") as f :
        data = pickle.load(f)

    for i in range(len(data)) :
        print(f'[{i}] 제목 : {data[i]["title"]}, 글 내용 : {data[i]["content"]}')

def remove(delete) : 
    with open("data2.p", "rb") as f :
        lst = pickle.load(f)

    if delete < 0 or delete >= len(lst) :
        print("잘못된 입력입니다. 삭제할 수 없습니다.")
        return
    
    lst.pop(delete)

    with open("data2.p", "wb") as f :
        pickle.dump(lst, f)

    print("삭제가 완료되었습니다.")
        
try : # 예외처리
    with open('data2.p', 'rb') as f : 
        pickle.load(f)
except :
    with open('data2.p', 'wb') as f :
        pickle.dump("", f)

while True :
    if menu() :
        break
"""