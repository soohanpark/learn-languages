# Section 12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회
conn = sqlite3.connect('./resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("""SELECT * FROM users""")

# 커서 위치가 변경
# 1개 로우 선택
print('One => ', c.fetchone())
# 지정 로우 선택
print('Three => ', c.fetchmany(size=3))
# 전체 로우 선택
print('All => ', c.fetchall())
print('All => ', c.fetchall()) # 빈 리스트 반환. (커서의 위치가 맨 끝이기 때문에)

# 순회1
rows = c.fetchall()
for row in rows:
    print('retreive1 => ', row)

# 순회2
for row in c.execute('SELECT * FROM users ORDER BY id DESC'):
    print('retreive2 => ', row)

# WHERE Retrieve 1
param1 =(3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1 =>', c.fetchone())
print('param1 =>', c.fetchall())  # 데이터 없음

# WHERE Retrieve 2
param2 = 4 
c.execute('SELECT * FROM users WHERE id=%s' % param2)
print('param1 =>', c.fetchone())
print('param1 =>', c.fetchall())  # 데이터 없음

# WHERE Retrieve 3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})  # 딕셔너리 형태로 넣어줄 떄는 : 을 활용!
print('param1 =>', c.fetchone())
print('param1 =>', c.fetchall())  # 데이터 없음

# WHERE Retrieve 4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN (?,?)", param4)
print('param4 => ', c.fetchall())

# WHERE Retrieve 5
c.execute("SELECT * FROM users WHERE id IN ('%d', '%d')" % (3, 4))
print('param5 => ', c.fetchall())

# WHERE Retrieve 6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param4 => ', c.fetchall())

# Dump 출력 (백업을 할 떄 사용)
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write("%s\n"%line)
        print('Dump Complete')