from flask import Flask, render_template
import os, random
app = Flask(__name__)

@app.route("/")
def base():
	# get a random .jpeg
	image = random.choice( [x for x in os.listdir('./static/img')] )
	return render_template('autoplayer.html', image = "./static/img/"+image)


