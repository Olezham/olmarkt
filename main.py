
from flask import Flask, render_template, session, request, redirect, url_for

from mysql import *

import secrets


app = Flask(__name__)


app.secret_key = secrets.token_hex(16)

@app.context_processor
def inject_user():
    return dict(email=session.get('email'))

@app.route('/')
def index():
    return render_template('index.html', articles=get_all_articels())

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if log(email,password):
                session['email'] = email
                return redirect(url_for('cabinet'))
            else:
                return render_template('login.html')

        except:
            print('not existed combination with email and password')
    else:
        return render_template('login.html')

@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        repeatpassword = request.form['repeatpassword']
        if password == repeatpassword:
            if not exist_email(email):
                if reg(email,password):
                    session['email'] = email
                    return redirect(url_for('cabinet'))
                else:
                    print('reg is no sucssed')
                    return render_template('reg.html')
            else:
                print('this email already exist')
                return render_template('reg.html')
        else:
            print('password not the same')
            return render_template('reg.html')
    else:
        print('get response')
        return render_template('reg.html')

@app.route('/cabinet')
def cabinet():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('cabinet.html', email=session['email'],articles = get_user_articles(session['email']))

@app.route('/add-article',methods=['GET','POST'])
def add_article():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']
        price = request.form['price']
        image = request.files['image']
        print('[LOG] call add_article function')
        if add_articles(name,about,price,image,session['email']):
            print('article added')
            return redirect(url_for('cabinet'))
        else:
            print('something with adding go wrong')
    else:
        return render_template('add_article.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/article/<string:uuid>')
def article(uuid):
    return render_template('article.html', data = get_article(uuid))

@app.route('/search')
def search():
    response = request.args.get('response')
    answer = 1
    lenth = len(get_articles_by_name(response))
    if lenth == 0:
        answer = 0
    return render_template('search.html', articles = get_articles_by_name(response), resp=response, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
