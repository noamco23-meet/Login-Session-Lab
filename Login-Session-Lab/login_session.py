from turtle import back
from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


#app doesnt reset values with each run
@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		try:
			login_session[str(request.form['quote'])] = {"quote": str(request.form['quote']), "author":str(request.form['author']), "age": int(request.form['age'])}
			print(login_session)
			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))



@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', login_session=login_session) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)

