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
"""

# 1. 각 단어가 몇 개씩 있는지 (딕셔너리)
"""
# ex1) 단어 'the'의 개수를 알고싶을 때,
# 반복문 및 if, else 활용
word_count = {}
for word in contents.split() :
    if word == 'the' :
        if 'the' in word_count :
            word_count['the'] += 1
        else :
            word_count['the'] = 1 # 1의 값으로 초기화

print('the단어의 사용 빈도수 : %d' %word_count['the'])
"""

"""
# ex2) 단어 'alice'의 개수를 알고싶을 때,
# 대소문자 구분 x
alice_count = contents.lower().count('alice')

print('alice 단어의 사용 빈도수 : %d' %alice_count)
"""


# 2. 로또 번호 생성기 1~45, 7개, 중복되지 않는 리스트
"""
import random

numbers = []
for _ in range(7):
    num = random.randint(1, 45)
    while num in numbers:
        num = random.randint(1, 45)
    numbers.append(num)

print(numbers)
"""


# 3. 공통된 음식 찾기 (컴프리헨션)
"""
person1 = ["치킨", "피자", "햄버거"]
person2 = ["족발", "삼겹살", "치킨"]
person3 = ["피자", "김밥", "떡볶이", "치킨"]

first_two_people = [food for food in person1 if food in person2]
print(first_two_people)

common_foods = [food for food in set(person1) & set(person2) & set(person3)]
print(common_foods)
"""
# all, any를 사용하여 공통된 음식 찾기 (일단, 두명부터)
