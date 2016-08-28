import markovgenerator as m

# m = MarkovGenerator()
# m.generate_corpus(m.input('demo/janeeyre.in'))


print(m.generate_text(	file='demo/janeeyre.in',
						words=True,
						resolution=2,
						output_size=1000,
						preserve_newlines=False
						))
