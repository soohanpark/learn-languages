# Section 12-1
# 파이썬 데이터베이스 연동 (SQLite)

# 테이블 생성 및 삽입
import sqlite3
import datetime

# sqlite3 version
print('sqlite3.version:', sqlite3.version)
print('sqlite3.sqlite_version:', sqlite3.sqlite_version)

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

# DB 생섣 & Auto Commit
conn = sqlite3.connect('./resource/database.db', isolation_level=None)  # isolation_level=None => Auto Commit

# Cursor
c = conn.cursor()
print('Cursor Type:', type(c))

# 테이블 생성 (Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute(
    """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            phone TEXT,
            website TEXT,
            regdate TEXT
        )
    """
)

# 데이터 삽입
c.execute("""INSERT INTO users VALUES(11, 'KIM', 'kim@naver.com', '010-0000-0000', 'kim.com', ?)""", (nowDateTime,))
c.execute(
    """
        INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)
    """, (2, 'KIM', 'kim@naver.com', '010-0000-0000', 'kim.com',nowDateTime,)
)

# MANY 삽입 (튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDateTime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDateTime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDateTime),
)
c.executemany(
    """
        INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)
    """, userList
)

# 테이블 데이터 삭제
conn.execute("""DELETE FROM users""")

# 커밋: isolation_level = None일 경우 오토 커밋
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()