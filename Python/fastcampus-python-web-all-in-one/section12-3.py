# Section 12-3
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB 생성
conn = sqlite3.connect('./resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
c.execute("""
    UPDATE users SET username = ? WHERE id = ?"
""", ('niceman', 2))

# 데이터 수정2
c.execute("""
    UPDATE users SET username = :name WHERE id = :id"
""", {"name": "goodman", "id": 5})


# 중간 데이터 확인1
for user in c.execute("SELECT * FROM users"):
    print(user)


# ROW DELETE 1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# ROW DELETE 2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5})

# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()

conn.close()