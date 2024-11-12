# 방법 1
# 전체 데이터 중 최고, 최저기온
"""
f = open('jeju_2019.csv', 'r', encoding='utf-8') # 파일열기(데이터열기)
lines = csv.reader(f) # 쓰기모드
header = next(lines) # 헤더 제거(넘기기)

max = -1000 # 초기값 설정
min = 1000 # 초기값 설정

for line in lines: # 반복문 실행(line이 lines안에 있을 동안)
    if float(line[4]) > max :
        # 만약 line[4](최고기온)이 max보다 크다면, 
        max = float(line[4])
        # max에 최고기온 값을 넣어준다.
        # 본 과정을 반복하며 최댓값을 찾아 대입해준다.

    if float(line[3]) < min :
        # 만약 line[3](최저기온)이 min보다 작다면, 
        min = float(line[3])
        # max에 최저기온 값을 넣어준다.
        # 본 과정을 반복하며 최솟값을 찾아 대입해준다.

print('제주 전체 데이터 중 최고기온 : %.1f' %max) # 찾아낸 최댓값을 출력해준다.
print('제주 전체 데이터 중 최저기온 : %.1f' %min) # 찾아낸 최댓값을 출력해준다.

f.close() # 파일닫기(필수)
"""

# 방법 2
# 전체 데이터 중 최고, 최저기온
# 각 월별 최대, 최소 기온을 구하고 그 중 최댓값, 최솟값 구하기
# 작일 코드 작성을 해보았지만 type error 등의 문제가 발생하여 완벽하게 끝내진 못했습니다...
"""
import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8') # 파일열기
lines = csv.reader(f) # 읽기모드
header = next(lines) # 헤더 생략(넘기기)

max_temp = [float('-inf')] * 12  # 음의 무한대 값으로 초기화
min_temp = [float('inf')] * 12  # 양의 무한대 값으로 초기화

# 최고, 최저온도의 리스트(출력표) 제작
for line in lines: # line이 lines 안에 있을 동안(반복문)
    for i in range(12) : # i를 길이 12만큼 반복
        if int(line[2][5:7]) == i+1 : # 만약 월(일시 데이터 중)이 i+1값과 동일하다면,
            max_temp[i] += float(line[4])
            min_temp[i] += float(line[3]) 

print('(1) 최고온도, 최저온도를 갖는 달과 그 온도')

max_month_temp = max(max_temp)
max_month = max_temp.index(max_month_temp) + 1
print('최고온도를 갖는 달과 그 온도 : %s월 %.1f 도\n' % (max_month, max_month_temp))

min_month_temp = min(min_temp)
min_month = min_temp.index(min_month_temp) + 1
print('최저온도를 갖는 달과 그 온도 : %s월 %.1f 도\n' % (min_month, min_month_temp))

print('\n(2) 월별 최고, 최저온도')
for i in range(1, 13) :
    print('%d월 : %.1f 도' % (i, max_temp[i-1]))
    print('%d월 : %.1f 도' % (i, min_temp[i-1]))

f.close()
"""
