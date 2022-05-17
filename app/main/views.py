from curses import flash
from flask import render_template,abort,redirect, url_for,request
from . import main 


# from ..email import mail_message


@main.route ('/')
def index():
    msg= 'heeloo'
    return render_template('index.html',msg=msg)
@main.route('/quiz',methods=['GET','POST'])
def quiz():
    return render_template('quiz.html')
