# 파일 읽기
f = open('./resource/review.txt', 'r')
content = f.read()  # content's type => <class 'str'>
print(content)
f.close()  # 반드시 close로 리소스 반환


# 파일 쓰기
with open('./resource/test1.txt', 'w') as f:
    f.write('Niceman!')

with open('./resource/test1.txt', 'a') as f:
    f.write('Goodman!')


# 예제 4
# writelines: 리스트 -> 파일로 저장
with open('./resource/test3.txt', 'w') as f:
    targetList = ['Lim\n', 'Park\n', 'Cho\n']
    f.writelines(targetList)

# 예제 5
# print에서 바로 파일로 저장!
with open('./resource/test4.txt', 'a') as f:
    print('Test Context1', file=f)
    print('Test Context2', file=f)