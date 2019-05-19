#! python3
# audio_file_maker.py - receive an input from a text file and convert it into an audio file

import random, os
from gtts import gTTS 


class AudioFileConverter:

	def __init__(self, input_filepath, number_of_quotes):
		self.output_filepath = "./static/audio/kenny_quotes.mp3"

		self.input_filepath = input_filepath
		self.number_of_quotes = int(number_of_quotes)

		self.quotes = self.select_from_file()
		self.quotes_mp3 = self.quote_to_audio()



	def select_from_file(self):
		quotes = []
		with open(self.input_filepath, "r") as f:
			lines = f.readlines()

		for i in range(self.number_of_quotes):
			quotes.append( random.choice(lines) )

		return quotes


	def quote_to_audio(self):

			audio_object = gTTS(
								text = '. '.join(self.quotes),
								lang = 'en',
								slow = False
								).save(self.output_filepath)

			






bot = AudioFileConverter('./static/kenny_quotes.csv', 3)
