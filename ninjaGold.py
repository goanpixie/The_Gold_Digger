import random, datetime
import os
from flask import Flask, render_template, request,session,flash,redirect,g

app=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
	if not 'gold_pot' in session.keys():

		session['gold_pot']=0
	print session['gold_pot']
	session['is_game_in_progress'] = True

	if 'output_text' not in session:
		session['output_text'] = ''
		print session['output_text']

	return render_template('index.html')
	

@app.route("/process_money",methods=['POST'])
def money():
	time=datetime.datetime.now()

	if (request.form).has_key('farmGold'):
		session['farmGold']=random.randint(10,20)
		session['gold_pot']+=session['farmGold']
		# flash('Earned',session['gold_pot'],'golds from the farm!',timestamp = datetime.now())
		session['output_text']+='<p class="green">Earned ' +str(session['farmGold'])+ ' golds from the farm!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))
		# print session['output']

	if (request.form).has_key('caveGold'):
		session['caveGold']=random.randrange(5,10)
		session['gold_pot']+=session['caveGold']
		session['output_text']+='<p class="green"> Earned '+str(session['caveGold'])+' golds from the cave!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))

	if (request.form).has_key('houseGold'):
		session['houseGold']=random.randrange(2,5)
		session['gold_pot']+=session['houseGold']
		session['output_text']+='<p class="green"> Earned '+str(session['houseGold'])+' golds from the house!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))

	if (request.form).has_key('casinoGold'):
		session['casinoGold']=random.randrange(-50,50)
		session['gold_pot']+=session['casinoGold']
		if session['casinoGold']<0: 
			session['output_text']+='<p class="red">Lost '+str((session['casinoGold'])*(-1))+' golds from the casino! </p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))
		elif session['casinoGold']>0:
			session['output_text']+='<p class="green">Earned '+str(session['casinoGold'])+' golds from the casino! </p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))



	return redirect('/')
		# session.pop('gold_pot')
		# session['is_game_in_progress'] = False

@app.route('/clear')
def clear():
	session.clear()
	return redirect('/')

	


		



app.run(debug=True)


