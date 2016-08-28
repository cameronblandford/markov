import markovgenerator as m

# m = MarkovGenerator()
# m.generate_corpus(m.input('demo/janeeyre.in'))


print(m.generate_text(	string='Here are some words.',
						words=True,
						resolution=2,
						output_size=1000,
						preserve_newlines=False,
						# full_sentences=False
						))
