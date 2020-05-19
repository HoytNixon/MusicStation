from flask import render_template, redirect, flash, url_for
from app import app, db
from .forms import SigninForm
from .models import Radio





@app.route('/')
@app.route('/index')
def index():
	radios = Radio.query.all()
	return render_template('index.html',radios= radios )


@app.route('/signin', methods= ['GET', 'POST'])
def signin():
	form= SigninForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me= {}'.format(form.username.data, form.remember_me.data))
		return redirect (url_for('index'))
	return render_template('signin.html', form=form)

@app.route('/<radiokey>/listen')
def radiopage(radiokey):
	radio = Radio.query.filter_by(id = radiokey).first()
	return render_template('radiopage.html', radio= radio)
