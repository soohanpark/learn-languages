# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print(' ')
print(" ")
print(""" """)
print(''' ''')

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('T', 'E', 'S', 'T', sep='^')

# End 옵션 사용
print('Welcome To', end='')
print('the black parade', end=' ')
print('piano notes')

# format 사용
print('{0} and {1} and {0}'.format('you', 'me'))  # 이렇게 값을 매핑하여 재사용 가능!
print('{a} are {b}'.format(a='you', b='me'))  # 이렇게 map 처럼 값을 지정하여 사용 가능!