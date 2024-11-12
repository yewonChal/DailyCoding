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
    
