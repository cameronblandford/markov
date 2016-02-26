from collections import defaultdict
import random


class MarkovGenerator:
	corpus = defaultdict(list)
	text_in = ""

	letters = True
	case_sensitive = False

	RESOLUTION = 7
	OUTPUT_SIZE = 1000


# for weird elven language shit: letters, not case sensitive, res = 2
# 

	def __init__(self):
		pass



	def input(self, filename):
		lines = []
		file = open(filename, "r")
		for line in file:
			lines.append(line)

		lines = [x.strip() for x in lines]
		lines = [x for x in lines if x != ""]
		lines = " ".join(lines)
		return lines

	def generateCorpus(self, text_in):
		self.text_in = text_in
		if self.letters:
			pass
		else: #words
			self.text_in = self.text_in.split(" ")
		
		words = []
		for i in range(0,self.RESOLUTION):
			words.append(self.text_in[i])

		for i in range(self.RESOLUTION, len(self.text_in)):

			for j in range(0, self.RESOLUTION):
				words[j] = self.text_in[i-(self.RESOLUTION-j)]

			keystring = []

			for k in range(0,self.RESOLUTION):
				if self.case_sensitive:
					keystring.append(words[k])
				else:
					keystring.append(words[k].lower())

			self.corpus[' '.join(keystring)].append(self.text_in[i])



	def output(self):
		seed = random.randint(0, len(self.text_in)-self.RESOLUTION)

		# initialize seed_words
		seed_words = []
		for i in range(0, self.RESOLUTION):
			seed_words.append("FILLER")
		for i in range(0, self.RESOLUTION):
			seed_words[i] = self.text_in[seed+i]

		output_words = []

		for i in range(0,self.OUTPUT_SIZE):

			output_words.append(seed_words[0])

			next_word = ""
			if self.case_sensitive:
				next_word = random.choice(self.corpus[' '.join(seed_words)])
			else:
				next_word = random.choice(self.corpus[' '.join(seed_words).lower()])

			for j in range(0,self.RESOLUTION-1):
				seed_words[j] = seed_words[j+1]
				# print seed_words[:-1]

			if self.case_sensitive:
				seed_words[self.RESOLUTION-1] = next_word
			else:
				seed_words[self.RESOLUTION-1] = next_word



		# cleanup
		for i in range(1,self.RESOLUTION):
			output_words.append(seed_words[i])

		# prettifying output
		if self.letters:
			return ''.join(output_words)
		else:
			return ' '.join(output_words)