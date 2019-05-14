#! python3
# batch_file_parser.py - script to parse our "interesting" quotes from a dump of all NoEsri Slack channel's conversations

import json, os

class Parser:
	def __init__(self, username, output_file):
		self.data_dir = "./data/"
		self.user_data_file = json.load( open(self.data_dir+"users.json") )

		self.user_id = self.get_user_id(username)
		print(self.user_id)

		self.output_file = output_file

		self.keywords = ['FUCK', 'SHIT', 'ZAPIER', 'CTRL F', 'EXERCISE', 'DRINKING', 'DRINK', 'DRUNK', 'DRINKS', 'CLIENT', 'CLIENTS', 'TASK', 'OVERWATCH', 'KEN', 'CALENDAR', 'SALESFORCE', 'GOOGLE', 'GOOGLESHEET','GOOGLESHEETS','STRATEGY','STRATEGIC','GOAL','GOALS','MEETING','MEETINGS','TOILET', 'ASS', 'SONAL', 'GRANTBOOK', 	]



	def get_user_id(self, username):
		for user in self.user_data_file:
			try:
				if user['real_name'] == username:
					return user['id']
			except:
				continue
		



	def file_to_dict(self, file):
		with open(file) as input:
			input_json = json.load(input)
			return input_json


	def parse_interesting_quotes(self, input_dict):
		interesting_quotes = []
		for object in input_dict:
			#print(object)
				 
			if (
				object['type'] == 'message' and 
				object['user'].upper().strip() == self.user_id.upper().strip() and 
				len(object['text']) >= 10 and
				any( x for x in self.keywords if x in object['text'].upper().split(" ")) and
				object['text'] != '<@U9APJ3XKN> has joined the channel' and
				"\n" not in object['text']
				
				): #and len(object['reactions']) >= 1:

				interesting_quotes.append( object['text'] )

		if len(interesting_quotes) > 0:
			return interesting_quotes


	def start(self):
		quotes_master_list = []

		dirs = [dir for dir in os.listdir(self.data_dir) if "." not in dir]
		for dir in dirs:
			#print(dir)

			for file in os.listdir(self.data_dir+dir):
				input_dict = self.file_to_dict(self.data_dir+dir+"/"+file)

				try:
					print(self.parse_interesting_quotes(input_dict))
					quotes_master_list = quotes_master_list + self.parse_interesting_quotes(input_dict)

				except:
					pass

		with open(self.output_file, 'w') as output:
			for quote in quotes_master_list:
				output.write(quote+'\n')
			output.close()




bot = Parser('Kenny Li', './out/kenny_quotes.csv')

print( bot.start() )


