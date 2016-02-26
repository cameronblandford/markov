from markov_generator.markovgenerator import MarkovGenerator

mg = MarkovGenerator()

mg.generateCorpus(mg.input('janeeyre.in'))
mg.generateCorpus(mg.input('test2.in'))
mg.generateCorpus(mg.input('test2.in'))
print "\n" + mg.output() + "\n"