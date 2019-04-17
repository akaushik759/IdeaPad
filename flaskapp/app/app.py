from flask import Flask, redirect, url_for, request,render_template
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
import datetime
#from models import *
app=Flask(__name__)


#MongoDB initialization
app.config['MONGO_DBNAME'] = 'ideaDb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/ideaDb"
mongo = PyMongo(app)

#client=MongoClient("mongodb://127.0.0.1:27017")
#db=client.mymongodb
#ideas=db.idea
#Variables
#ideas_list=['Personal Blog','My Portfolio Page','My CSS framework','Entrepreneurship Book Recommender']


@app.route('/home')
def home():
	ideas=mongo.db.ideas
	ideas_list=ideas.find()
	return render_template('index.html',count=ideas_list.count(),ideas=ideas_list)

@app.route('/idea/1')
def idea():
	return render_template('idea.html',idea='Personal Blog')

@app.route('/<name>')
def random_page(name):
	return 'Hello Stalker ! Welcome to %s '%name


@app.route('/postidea',methods=['GET','POST'])
def post_idea():
	ideas=mongo.db.ideas
	if request.method=='POST':
		new_idea=request.values.get('new_idea')
		ideas.insert({'idea_title':new_idea,'datestamp':datetime.datetime.now().strftime('%d %B %Y'),'timestamp':datetime.datetime.now().strftime('%H:%M:%S')})
		return redirect(url_for('home'))
	else:
		return render_template('postidea.html')

if __name__=='__main__':
	app.run(debug=True)