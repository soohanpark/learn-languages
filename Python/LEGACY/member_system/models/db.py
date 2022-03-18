import pymysql
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(
    creator = pymysql,
    maxconnections = 100,
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'qkrtngks1',
    database = 'pythondb',
    charset = 'utf8',
    autocommit = True,
    cursorclass = pymysql.cursors.DictCursor
)