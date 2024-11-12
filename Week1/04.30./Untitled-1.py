"""
# 과제 강사님 코드

# 문제 1
menu = input("메뉴를 선택하세요. 아메리카노 - 4500원, 카페라떼 - 5000원, 바닐라라떼 - 5500원 : ")
price = int(input('금액을 넣어주세요. : '))

menu1 = '아메리카노'
menu2 = '카페라떼'
menu3 = '바닐라라떼'

pay1 = 4500
pay2 = 5000
pay3 = 5500

check = 0 # 잘못 입력했을 때, 검증 변수

if menu == menu1 : 
    price -= pay1
elif menu == menu2 : 
    price -= pay2
elif menu == menu3 :
    price -=pay3
else :
    print('메뉴를 잘못입력하였습니다.')
    check = 1

if check == 0 :
    if price >= 0 :
        print('%s가 나왔습니다. 거스름돈 %d원이 나왔습니다.' %(menu, price))
    else :
        print('금액이 부족합니다.')


# 문제 2
a = 10
b = 20
c = 30

if c > a and c > b : # 논리연산자
    print('c가 가장 크다.')

if c > a : # 중첩 조건문
    if c > b :
        print('c가 가장 크다.')

# 기본 조건문
if c < a :
    print('c보다 a가 더 크다.')
elif c < b :
    print('c보다 b가 더 크다.')
else : # c > a  and c > b
    print('c가 가장 크다.')


# 반복문
# 어제 배웠던 내용 : for, range


# ----- 외출 복귀 후 작성한 코드

# 전화번호에서 하이픈 삭제하기
number = input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요. : ')



# 전체 구구단표 만들기
print('-' * 50)

for a in range(2, 10) :
    for b in range(1, 10) :
        c = a * b
        print('%d x %d = %d' %(a, b, c))

    print('-' * 50)

# 반복문 마지막(부터 시작)(조건문과 반복문 내용)

num = int(input('홀수단 - 1, 짝수단 - 2를 입력하세요. : '))

for a in range(2, 10, 2) :
    if num == 1 and a % 2 != 1 :
        continue
    if num == 2 and a % 2 != 0 :
        continue
    if a % 2 != 0 :
        continue
    print(a, '단')
          
    for b in range(1, 10):
        print("%d x %d = %d" %(a, b, a*b))
    print('-'*30)


# 리스트 Chapter 05
    # '박스를 이어붙인 상태'라고 생각할 수 있다.
    # 여러 개가 나열되어 있는 상태

# 리스트 생성과 추출
fruits = ['사과', '오렌지', '딸기', '포도', '감']

list1 = [5, 10, 2, '탁구', True, [4, 5, 6]]

numbers = list(range(1, 10, 2))

print(fruits)
print(list1)
print(numbers)

print(fruits[0])
print(fruits[1:4])
print(fruits[2:])
print(fruits[-1])
print(fruits[-4:-2])
print(fruits[-3:])

# 리스트 요소 추가
a = ['red', 'green', 'blue']
a.append('yello') # yello 삽입
print(a)

a.insert(1, 'black') # 1번 위치에 black 삽입
print(a)

b = ['purple', 'white']
a.extend(b) # a에 b 내용 추가
print(a)

c = a + b
print(c)


# 리스트 요소 삭제
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = a.index(30) # 몇 번째 index에 30이 포함되어 있는지 확인
print(x)

a.pop(x) # del a[x]와 동일한 코드
print(a) # 위치를 기준으로 삭제

a.remove(90) # 특정 숫자 삭제(직접 지정)
print(a) 

a.clear() # 모든 배열 삭제
print(a)

# 리스트 요소 카운트
list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa']
count(list1)

# 리스트 정렬
list1.sort() # 오름차순 정렬

list1.sort(reverse=True) # 내림차순 정렬
print(list1)

# 리스트 주요 메소드 정리하기

# 리스트 추출하기
color = ['red', 'green', 'blue', 'black', 'white']

print(color[0])
print(color[-1])
print(color[1:4])


# list()와 range()로 리스트 생성하기
num = list(range(1, 20, 2))

# 리스트 요소 추가하기
mylist = ['사과', '바나나', '파인애플', '배']
mylist.append('키위')

for a in mylist :
    print(a) # mylist에 들어가 있는 데이터 꺼내서 a에 삽입

# 리스트 요소 삭제하기
mylist.remove('바나나')
print(mylist)

# 리스트 요소 삭제하기
person1 = ['kim', 24]
person2 = ['park', 35]

person = person1 + person2 
print(person)

# for문에서 리스트 활용
fruits = ['apple', 'orange', 'banana']

for fruit in fruits :
    print(fruit)

# 리스트로 합계와 평균 구하기
scores = [88, 75, 90, 95, 77, 69, 80, 92]
# 합계, 평균 
# 합계
for score in scores :
    sum += score

print("합계 : %d, 평균 : #f"%(sum, sum/len(scores)))

# while문에서 리스트 활용
animals = ['토끼', '거북이', '사자', '호랑이']

i = 0

# 리스트 요소 삭제하기

i = 0

while i < len(s) :
    if s[i] >= 90 and 
"""

"""
s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

i = 0
count = [0, 0, 0, 0, 0]
grade = "수우미양가"

while i < len(s) :
    if s[i] > 100 or s[i] < 0 :
        print("잘못된 성적을 입력하였습니다. 성적을 확인하세요.")
        i += 1
        continue
    elif s[i] >= 90 :
        count[0] += 1
    elif s[i] >= 80 :
        count[1] += 1
    elif s[i] >= 70 :
        count[2] += 1
    elif s[i] >= 60 :
        count[3] += 1
    else :
        count[4] += 1
    i += 1

    for i in range(0,5) :
        print(' %s : %d명' %(grade[i], count[i]))
"""
        
# 리스트 생성
"""
count = []

for i in range(10):
    count.append(0)

print(count)

count = [0]

count = count*10 

print(count)


# 1부터 100까지 넣은 리스트
count = []

for i in range(100):
    count.append(i+1)

print(count)

# 리스트를 이용한 영어단어 퀴즈
questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answer = ['a', 'u', 't', 'p']
for i in range(len(questions)):
    q = '%s에서 밑줄(_) 안에 들어갈 알파벳은?' %questions[i]
    ans = input(q)

    if ans == answer[i] :
        print('정답입니다!')
    else :
        print('틀렸습니다!')


# index() : 특정 요소의 첫 번째 값의 인덱스 번호를 구한다.
menu = ["참치김밥", "치즈김밥", "꼬마김밥", "떡볶이", "순대"]

find = input("원하는 메뉴를 선택하시오. : ")

for i in range(len(menu)) :
    if menu[i] == find :
        print("음식이 존재합니다.")
        print(i)
        break
    
    if i == len(menu) - 1 :
        print("음식이 존재하지 않습니다.")
        print(-1) # 끝까지 왔을 때 검증해주는 코드

        
# len() 함수 : 리스트, 문자열에 포함된 요소의 개수를 나타낸다. NULL 문자
str = "음식이 존재합니다."
count = 0
index = 0

while True :
    count += 1
    if(str[index] == '.') :
        break
    index += 1

print(count)

# count : 리스트에 포함된 특정 요소의 개수를 나타낸다.
list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa', 'b', 'cc', 'd', 'aaa']

length = 0
find = 'aaa'

for i in list1 :
    if i == find :
        length += 1

print(length)


# min, max()
s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

print(min(s))
print(max(s))

s_max = 0 # 박스 하나 생성 / 또는 s[0]
# 0부터 넣어서 비교 시작

# 반복문 돌리기
for x in s :
    if s_max < x :
        s_max = x

print(s_max)

s_min = 1000
# 1000부터 넣어서 비교 시작

for x in s :
    if s_min > x :
        s_min = x

print(s_min)


# sum() : 리스트의 요소의 전제의 합

print(sum(s)) 

s_sum = 0

for x in s :
    s_sum += x

print(s_sum)

# storted : 정렬

# ----------- 1차원 종료



# 2차원 리스트의 구조
numbers = [[10, 20, 30], [40, 50, 60]]

print(numbers[0])
print(numbers[1])
print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])

# 8명 학생 3과목 성적 합계와 평균
scores = [[96, 84, 80], [96, 86, 76], [76, 95, 84], [89, 96, 69], [90, 76, 91], [82, 66, 88], [83, 86, 79], [85, 90, 83]]

for i in range(len(scores)):
    sum = 0
    for j in range(len(scores[i])):
        sum = sum + scores[i][j] # i가 0부터 7까지 쭉(행), j가 0부터 2까지 쭉(열)

    avg = sum / len(scores[i])

    print('%d번째 학생의 합계 : %d, 평균 : %.2f' %(i+1, sum, avg))

# 위 코드를 while문으로 작성
scores = [[96, 84, 80], [96, 86, 76], [76, 95, 84], [89, 96, 69], [90, 76, 91], [82, 66, 88], [83, 86, 79], [85, 90, 83]]

i = 0
while i < len(scores) :
    sum = 0
    j = 0
    
    while j < len(scores[i]):
        sum = sum + scores[i][j]
        j += 1

    avg = sum / len(scores[i])

    print('%d번째 학생의 합계 : %d, 평균 : %.2f' %(i+1, sum, avg))
    i += 1
"""

# 리스트를 이용한 합계/평균 구하기
scores = []
s_max = 0
s_min = 1000

while True :
    score = int(input('성적을 입력하세요.(종료 시 -1 입력) : '))
    if score == -1 :
        break
    else : 
        scores.append(score)

    if s_max < score :
        s_max = score

    if s_min > score :
        s_min = score

s_max = 0
s_min = 1000
sum = 0
for i in range(0, len(score)) :
    sum += scores[i]
    if s_max < scores[i]:
        s_max = scores[i]
    if s_min > scores[i]:
        s_min = scores[i]

avg = sum / len(scores)

print('합계 : %d, 평균 : %.2f' %(sum, avg))
print('최고점 : %d, 최저점 : %d' %(s_max, s_min))

# 영화관 빈 좌석 표시하기
i = 0
j = 0
seats = 0

for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == 0:
            print('%3s' %'ㅁ', end=' ')
        else:
            print('%3s' %'ㅇ', end=' ')
        print()

print('\n *예약 가능 : ㅁ, 예약 불가능 : ㅇ')

# 금일 과제

# 1. 
"""
*
**
***
****
*****

    *
   **
  ***
 ****
*****

*****
****
***
**
*

*****
 ****
  ***
   **
    *

     *
    ***
   *****
  *******
***********
    --> 반복문이랑 print로 출력

"""

# 2. reverse 구현해보기
"""

# + reverse() : 리스트를 역순으로 변환
menu = ["김밥", "치즈"]
menu2 = menu.reverse()

print(menu2)


"""
