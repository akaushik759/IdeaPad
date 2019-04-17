
@app.route('/postidea',methods=['GET','POST'])
def post_idea():
	ideas=mongo.db.ideas
	if request.method=='POST':
		new_idea=request.values.get('new_idea')
		ideas.insert({ "idea_title":new_idea,"timestamp":datetime.datetime.now()})
		return 'Successfully added new idea !'
	else:
		return render_template('postidea.html')