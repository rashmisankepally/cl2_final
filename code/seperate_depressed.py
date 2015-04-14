__author__ = 'yogarshi'

"""
"""

import sys
import cPickle as pickle

class User:
	"""
	A class to store information about each user
	"""
	def __init__(self, user_id, score, isDepressed=False):
		self.user_id = user_id
		self.score = score
		self.isDepressed = isDepressed


def main(argv):

	#The mypersonalty_depression/939_userScores.csv file
	scores_file = open(argv[0], 'r')
	#The mypersonalty_depression/cesd_item_level.csv file
	item_level_file = open(argv[1], 'r')

	#The threshold for depression cut_off
	depression_threshold = int(argv[2])

	#The output pickle file
	user_dict_p = argv[3]

	#user_id -> User object dict
	user_dict = {}


	#Read through the scores_file
	header = scores_file.readline()

	for each_line in scores_file:
		user_id, time_completed, score = each_line.strip().split(',')
		if int(score) >= depression_threshold:
			isDepressed = True
		else:
			isDepressed = False
		current_user = User(user_id, int(score), isDepressed)
		user_dict[user_id] = current_user

	depressed_list = [user_dict[key] for key in user_dict if user_dict[key].isDepressed]

	#Read through the item level file
	header = item_level_file.readline()
	for each_line in item_level_file:
		x = each_line.strip().split(',')

		user_id = x[0]
		ethnicity = x[23]
		marital_status = x[24]
		par_together = x[25]

	#Dump user_dict into a pickle
	pickle.dump(user_dict, open(user_dict_p, 'wb'))




if __name__ == "__main__":
	main(sys.argv[1:])