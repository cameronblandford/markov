from markovgenerator import MarkovGenerator

m = MarkovGenerator()
m.generate_corpus(m.input('demo/janeeyre.in'))
print(m.output())