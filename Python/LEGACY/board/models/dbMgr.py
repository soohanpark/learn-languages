import pymysql

def getConnection():
    # 연결시에 바로 호스트와 포트 유저 정보, 데이터베이스와 인코딩정보를 설정할 수 있다. 또한 자동으로 commit()을 해줄수도 있으며, 넘겨줄 데이터를 자동으로 dict 형태로 넘겨줄 수도 있다.
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='qkrtngks1', db='boarddb', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return conn


def board_write(_data):
    conn = getConnection()
    cursor = conn.cursor()
    sql = 'INSERT INTO board (name,title,content,pwd) VALUES (%s, %s, %s, %s);'
    affected = cursor.execute(sql, _data)
    print(affected)
    cursor.close()
    conn.close()
    return affected


def board_list():
    rows = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM board ORDER BY num DESC;' # 최신글을 제일 위로
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print("ERROR >>>", e)
    finally:
        conn.close()
        
    return rows


def board_read(num): # num 은 글번호.
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "SELECT * FROM board WHERE num=%s;"
        cursor.execute(sql, (num))  # 튜플로 넣어줘야한다.
        row = cursor.fetchone() #데이터가 1개이면 fetchone, 전부이면 fetchall

    except Exception as err:
        print("ERROR in READ >>>", err)
    finally:
        cursor.close()
        conn.close()

    return row


def board_hit_up(num):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = 'UPDATE board SET hit=hit+1 WHERE num=%s;'
        data = ( num )
        cursor.execute(sql, data)
        cursor.close()
    except Exception as err:
        print('HIT ERROR >>>', err)
    finally:
        conn.close()


def board_update(data):
    result = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = """UPDATE board
                 SET name=%s, title=%s, content=%s, regdate=now()
                 WHERE num=%s and pwd=%s"""
        result = cursor.execute(sql, data) #몇개가 적용되었는지 리턴해준다.
        cursor.close()
    except Exception as err:
        print('ERROR UPDATE >>> ', err)
    finally:
        conn.close()
    return result


def board_delete(data): #글번호 다운!! 필요!!!
    result = None

    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "DELETE FROM board WHERE num=%s and pwd=%s;"
        #data = ( num ) #데이터는 튜플로넘겨줘야 한다!!
        result = cursor.execute(sql, data)
        cursor.close()
    except Exception as err:
        print("ERROR DELETE >>>", err)
    finally:
        conn.close()

    return result


def comment_insert(data):
    result = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "INSERT INTO comment SET c_name=%s, c_content=%s, num=%s;"
        result = cursor.execute(sql, data)
        cursor.close()
    except Exception as err:
        print("ERROR COMMENT INSERT >>> ", err)
    finally:
        conn.close()
    return result


def comment_list(num):
    rows = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM comment WHERE num=%s ORDER BY c_no DESC;'
        cursor.execute(sql, num)
        rows = cursor.fetchall()
        cursor.close()
    except Exception as err:
        print("ERROR COMMENT LIST >>>", err)
    finally:
        conn.close()
    return rows


def board_count():
    result = None
    
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) cnt FROM board;" #COUNT(대상) 별명 --> 대상에 해당하는 갯수를 세어준다. 별명으로 접근 가능/출력.
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as err:
        print("ERROR BOARD COUNT >>> ", err)
    finally:
        conn.close()
    
    return result


def board_limit(data):
    rows = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "SELECT * FROM board ORDER BY num DESC LIMIT %s, %s;"
        cursor.execute(sql, data)
        rows = cursor.fetchall()
    except Exception as err:
        print("ERROR BOARD LIMIT >>> ", err)
    finally:
        conn.close()
    return rows


if __name__ == '__main__':
    print( board_limit( (0,10) ) )