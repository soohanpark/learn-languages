# Section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

import csv

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)

    print(reader)

    for c in reader:
        print(c)



import pandas as pd

# sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())

# 하위 데이터 확인
print(xlsx.tail())

# 행, 열 확인
print(xlsx.shape)