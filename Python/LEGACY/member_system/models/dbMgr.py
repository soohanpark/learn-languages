from models.db import POOL # __init__.py 는 현재 폴더에 있는 파일들을 컨트롤 하겠다는 파일.

def test_connection():
    conn = POOL.connection()
    print(conn)


def member_insert(data):
    result = None
    try:
        conn = POOL.connection()
        cursor = conn.cursor()
        sql = "INSERT INTO member SET id=%s, pwd=%s, name=%s, gender=%s, email=%s, tel=%s;"
        result = cursor.execute(sql, data)
        cursor.close()
    except Exception as err:
        print('ERROR MEMBER INSERT >>> ', err)
    finally:
        conn.close()
    
    return result


def member_login(data):
    result = None
    try:
        conn = POOL.connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM member WHERE id=%s and pwd=%s;"
        cursor.execute(sql, data)
        result = cursor.fetchone()
        
        
    except Exception as err:
        print("ERROR MEMBER LOGIN >>>", err)
    finally:
        print('리절트 값은', result)
        conn.close()
        cursor.close()

    return result


if __name__ == '__main__':
    print(member_login(('hong', '1234')))