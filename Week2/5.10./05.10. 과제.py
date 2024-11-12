#2. 각 학년별로 학생수가 가장 많은 학교 찾기
import csv
import numpy as np

f = open('high_school_2019.csv', 'r', encoding='utf-8') # 파일열기

lines = csv.reader(f)
header = next(lines)

list_data = [] # 빈공간(리스트) 생성

for line in lines : # line이 lines 안에 있는 동안(반복)
    list_data.append(line[:]) # line_data에 line 슬라이싱 부분을 추가해준다.
    
length = len(list_data) # list data의 길이를 'length'로 정의하고,

data = np.zeros((length, 3), dtype='int32') # data의 행 수와 타입은 다음과 같다.

for i in range(length) : # i를 length의 길이동안 반복한다.
    for j in range(3) : # j가 길이 3 안에 있는동안 반복한다.
        data[i][j] = list_data[i][j+2] # data의 i(행)과 j(열) = 리스트 데이터의 i(행)rhk j+2(열)

max_index = np.argmax(data, axis = 0)
print(max_index)

max_index = np.argmax(data, axis = 0) # 각 학년별 최대값의 인덱스 찾기
max_class1 = list_data[max_index[0]][1] # 1학년 최대 학생 수 학교
num_class1 = list_data[max_index[0]][3] # 1학년 최대 학생 수

max_class2 = list_data[max_index[1]][1] # 2학년 최대 학생 수 학교 
num_class2 = list_data[max_index[1]][5] # 2학년 최대 학생 수

max_class3 = list_data[max_index[2]][1] # 3학년 최대 학생 수 학교
num_class3 = list_data[max_index[2]][7] # 3학년 최대 학생 수

print('1학년 학생 수가 최대인 고등학교 : %s, 학생수 : %s개 ' % (max_class, num_class))
print('2학년 학생 수가 최대인 고등학교 : %s, 학생수 : %s명' % (max_student, num_student))
print('3학년 학생 수가 최대인 고등학교 : %s, 학생수 : %s명' % (max_teacher, num_teacher))

f.close()