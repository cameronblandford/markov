import unittest
from markovgenerator import MarkovGenerator

class MarkovTestCase(unittest.TestCase):
    def setUp(self):
        self.m = MarkovGenerator()

class MarkovBasicTest(unittest.TestCase):
    def runTest(self):
        self.m.generateCorpus(self.m.input('demo/janeeyre.in'))


class MarkovSmallSample(MarkovTestCase):
    def runTest(self):
        self.m.OUTPUT_SIZE = 100
        self.m.generateCorpus('Here is a sample corpus.')
        print(self.m.output())


if __name__ == '__main__':
    unittest.main()