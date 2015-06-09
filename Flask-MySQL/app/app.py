from flask import Flask
from flask import request
from model import db
from model import User
from model import CreateDB
from model import app as application
import simplejson as json
from sqlalchemy.exc import IntegrityError
import os

# initate flask app
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World! Docker-Compose for Flask & Mysql\n'

@app.route('/user')
def show_user():
	#return json.dumps({'username':request.args['username']})
	try:
		user = User.query.filter_by(username=request.args['username']).first_or_404()
		return json.dumps({user.username:{ 'email': user.email, 'phone': user.phone,'fax':user.fax}})
	except IntegrityError:
		return json.dumps({})

# http://localhost/
@app.route('/insert')
def insert_user():
	try:
		user = User(request.args['username'], 
				request.args['email'], 
				request.args['phone'], 
				request.args['fax'])
		db.session.add(user)
		db.session.commit()
		return json.dumps({'status':True})
	except IntegrityError:
		return json.dumps({'status':False})

@app.route('/createtbl')
def createUserTable():
	try:
		db.create_all()
		return json.dumps({'status':True})
	except IntegrityError:
		return json.dumps({'status':False})

@app.route('/users')
def users():
	try:
		users = User.query.all()
		users_dict = {}
		for user in users:
			users_dict[user.username] = {
							'email': user.email,
							'phone': user.phone,
							'fax': user.fax
						    }

		return json.dumps(users_dict)
	except IntegrityError:
		return json.dumps({})

@app.route('/createdb')
def createDatabase():
	HOSTNAME = 'localhost'
	try:
		HOSTNAME = request.args['hostname']
	except:
		pass
	database = CreateDB(hostname = HOSTNAME)
	return json.dumps({'status':True})

@app.route('/info')
def app_status():
	return json.dumps({'server_info':application.config['SQLALCHEMY_DATABASE_URI']})

# run app service 
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082, debug=True)

