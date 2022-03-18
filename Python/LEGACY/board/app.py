from flask import Flask, render_template, request, redirect
from models import dbMgr
import math

# 1. writeform            DB처리없음
# 2. write (POST)         INSERT
# 3. list                 SELECT
# 4. read/글번호          SELECT
# 5. updateform/글번호    UPDATE
# 6. update 
# 7. deleteform/글번호
# 8. delete               DELETE
# 9. commentform
# 10. comment            INSERT


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/writeform')
def writeform():
    return render_template('writeform.html')


@app.route('/write', methods=['POST'])
def write():
    print('넘어온 값들', request.form)
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']
    pwd = request.form['pwd']
    data = (name, title, content, pwd)
    dbMgr.board_write(data)
    return redirect('/list')


# @app.route('/list')
# def printList():
#     rows = dbMgr.board_list()
#     return render_template('/list.html', rows=rows)

# 127.0.0.1:5000/list/{{page}}

@app.route('/list')
def printList0():
    return redirect('/list/1')


@app.route('/list/<int:page>') # <자료형:변수명> 변수를 자동으로 해당 자료형으로 형변환 시켜준다.
def printList(page):
    size = 10
    begin = (page-1)*size
    result = dbMgr.board_count()
    cnt = result['cnt']
    total_page = math.ceil(cnt/size) # ceil 소숫점 올림
    data = (begin, size)
    rows = dbMgr.board_limit(data)
    link_size = 10
    start_link = math.floor((page-1)/link_size) * link_size + 1 # floor 소숫점 버림
    end_link = start_link + (link_size - 1)
    if end_link > total_page:
        end_link = total_page
    max_guel = cnt - ((page-1) * link_size)
    datas = { "rows":rows, "page":page, "total_page":total_page, "link_size":link_size,
              "start_link":start_link, "end_link":end_link, "max":max_guel}
    return render_template('list.html', datas=datas)


@app.route("/read/<num>/<page>") # 이렇게 동적으로 페이지를 구성할 수 있다.
def read(num, page):
    dbMgr.board_hit_up(num) #게시글을 읽을 때, 조회수를 증가시킴.
    row = dbMgr.board_read(num)
    comments = dbMgr.comment_list(num)
    return render_template('read.html', row=row, comments=comments, page=page)


@app.route("/updateform/<num>/<page>")
def updateform(num, page):
    row = dbMgr.board_read(num)
    return render_template('updateform.html', row=row, page=page)


@app.route('/update', methods=['POST'])
def update():
    print("넘어온 값들 >>>", request.form)
    num = request.form['num']
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']
    pwd = request.form['pwd']
    page = request.form['page']
    data = (name, title, content, num, pwd) # 튜플 형태로 넘겨줌.
    result = dbMgr.board_update(data)
    print(result)
    if result == 0:
        return """<script>alert('비밀번호가 틀립니다!'); 
                  history.back();
                  </script>
               """
               # script로 실행!! html 형식이다!
    else:
        return redirect('/list/' + page) # 해당하는 주소로 돌아감.


@app.route('/deleteform/<num>/<page>')
def deleteform(num, page):
    print(num)
    return render_template('deleteform.html', num=num, page=page) # num=num 은 dictionary { 'num' : 2 } 라고 보내는 것이다!


@app.route('/delete', methods=['POST'])
def delete():
    print('DELETE COMPLETE', request.form)
    num = request.form['num']
    pwd = request.form['pwd']
    page = request.form['page']
    data = (num, pwd)
    result = dbMgr.board_delete(data)
    if result == 0:
        return """<script>alert('비밀번호가 틀립니다!'); 
                  history.back();
                  </script>
               """
               # script로 실행!! html 형식이다!
    else:
        return redirect('/list/' + page) # 해당하는 주소로 돌아감.


@app.route('/commentform/<num>/<page>')
def commentform(num, page):
    return render_template('commentform.html', num=num, page=page)


@app.route('/comment', methods=['POST'])
def comment():
    print('Comment request form >>>', request.form)
    num = request.form['num']
    name = request.form['name']
    content = request.form['content']
    page = request.form['page']
    data = ( name, content, num )
    result = dbMgr.comment_insert(data)
    return redirect( '/read/'+ num + '/' + page )


@app.route('/write300')
def write300():
    for i in range(1,301):
        name = '타잔' + str(i) 
        title = name + '이' + str(i) + '원 짜리 팬티를...'
        content = name + '이' + str(i+1) + '원 짜리 칼을 차고...'
        pwd = '1234'
        data = (name, title, content, pwd)
        dbMgr.board_write(data)
    return 'OK'


if __name__ == '__main__':
    app.debug = True
    app.run()


"""
update board
SET name='AMOOGAE', title='CHANGE TITLE', content='CHANGE CONTENTS', regdate=now()
WHERE num=1 and pwd='1234';
"""