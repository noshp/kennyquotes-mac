from flask import Flask, render_template

from audio_file_maker import AudioFileMaker
import os, random

app = Flask(__name__)



@app.route("/")
def base():

	# get a random .jpeg
	audio = AudioFileMaker('./static/kenny_quotes.csv', 1).return_filepath()
	image = random.choice( [x for x in os.listdir('./static/img')] )
	return render_template('autoplayer.html', image = "./static/img/"+image, audio = audio)
