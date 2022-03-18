# pip install flask
# pip install flask-mysql
# pip install dbutils

from flask import Flask, render_template, request, redirect, session
from models import dbMgr
import sha3

k = sha3.keccak_256() # keccak-256 활용!!
k.update(b'soohanpark') # update 안에 "b" 가 없으면 encoded error 가 발생한다!!


app = Flask(__name__)
app.secret_key = str(k.hexdigest())

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/joinform')
def joinform():
    return render_template('joinform.html')

@app.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    tel = request.form['tel']
    data = (id, pwd, name, gender, email, tel)
    result = dbMgr.member_insert(data)
    if result == 1:
        return  """
                <script>alert('SUCESS! IT WILL BACK TO MAIN PAGE.');
                location.href='/';
                </script>
                """
    else:
        return  """
                <script>alert('FAILED! IT WILL BACK TO JOIN PAGE.');
                history.back();
                </script>
                """


@app.route('/loginform')
def loginform():
    return render_template('loginform.html')


@app.route('/login', methods=['POST'])
def login():
    tmp = 0
    print(request.form)
    id = request.form['id']
    pwd = request.form['pwd']
    data = ( id, pwd )
    result = dbMgr.member_login(data)
    # print('여기서 리절트는 ', result['id'])
    try:
        if result['id'] != None:
            tmp = 1
    except Exception as err:
        print('ERROR ><><><')
    
    if tmp == 1:
        session['userid'] = id
        return  """
                <script>
                alert('LOGIN SUCCESS!');
                location.href='/';
                </script>
                """
    else:
        return  """
                <script>
                alert('LOGIN FAILED!');
                history.back();
                </script>
                """


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()





"""
    CREATE TABLE `member` (
        `id` VARCHAR(20) NOT NULL,
        `name` VARCHAR(10) NOT NULL,
        `pwd` VARCHAR(20) NOT NULL,
        `gender` VARCHAR(1) NOT NULL,
        `email` VARCHAR(50) NOT NULL,
        `tel` VARCHAR(13) NOT NULL,
        `regdate` DATETIME NOT NULL DEFAULT '',
        PRIMARY KEY (`id`)
    )
    COLLATE='utf8_general_ci'
    ENGINE=InnoDB
    ;
"""