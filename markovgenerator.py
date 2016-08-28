import random
import re
import sys
from collections import defaultdict


class MarkovGenerator:
    corpus = defaultdict(list)
    text_in = ""

    def __init__(self):
        self.letters = False
        self.case_sensitive = False
        self.full_sentences = True
        self.preserve_newlines = True
        self.RESOLUTION = 2
        self.OUTPUT_SIZE = 500
        pass

    def input(self, filename):
        """
        Takes in the name of a text document, and outputs the contents of the
        text document as a single string.

        :param filename: A string representation of the text document's
        file-path
        :return: A single string containing all the text from said document
        """
        lines = []
        file = open(filename, "r")
        for line in file:
            lines.append(line)

        if self.preserve_newlines:
            lines = [x.strip() + '\n' for x in lines]
        else:
            lines = [x.strip() for x in lines]
        lines = [x for x in lines if x != ""]
        lines = " ".join(lines)
        return lines

    def generate_corpus(self, text_in):
        """
        Takes in a string and adds it to the corpus.

        :param text_in: the string to add to the corpus
        :return: nothing
        """
        self.text_in = text_in
        if self.letters:
            pass
        else:  # words
            self.text_in = self.text_in.split(" ")

        words = []
        for i in range(0, self.RESOLUTION):
            words.append(self.text_in[i])

        for i in range(self.RESOLUTION, len(self.text_in)):
            for j in range(0, self.RESOLUTION):
                words[j] = self.text_in[i - (self.RESOLUTION - j)]

            keystring = []

            for k in range(0, self.RESOLUTION):
                if self.case_sensitive:
                    keystring.append(words[k])
                else:
                    keystring.append(words[k].lower())

            self.corpus[' '.join(keystring)].append(self.text_in[i])

    def output(self):
        """
        :return: Text generated from corpus
        """
        seed = random.randint(0, len(self.text_in) - self.RESOLUTION)

        # initialize seed_words
        seed_words = []
        for i in range(0, self.RESOLUTION):
            seed_words.append("FILLER")
        for i in range(0, self.RESOLUTION):
            seed_words[i] = self.text_in[seed + i]

        output_words = []

        for i in range(0, self.OUTPUT_SIZE):
            output_words.append(seed_words[0])

            next_word = ""
            if self.case_sensitive and len(self.corpus[' '.join(seed_words)]) > 0:
                    next_word = random.choice(self.corpus[' '.join(seed_words)])
            elif len(self.corpus[' '.join(seed_words).lower()]) > 0:
                next_word = random.choice(self.corpus[' '.join(seed_words).
                                          lower()])
            else:
                break

            for j in range(0, self.RESOLUTION - 1):
                seed_words[j] = seed_words[j + 1]

            if self.case_sensitive:
                seed_words[self.RESOLUTION - 1] = next_word
            else:
                seed_words[self.RESOLUTION - 1] = next_word

        # cleanup
        for i in range(1, self.RESOLUTION):
            output_words.append(seed_words[i])

        # making output pretty
        if self.letters:
            out = ''.join(output_words)
        else:
            out = ' '.join(output_words)
        if self.full_sentences:
            return trim_output(out)
        else:
            return out


def trim_output(output):
    """
    Removes anything after the last ending punctuation in the output,
    in order to remove any incomplete sentences.

    :param output: text to be trimmed
    :return: The result of the trimming
    """
    pattern = '[A-Z][\S\s]*[\.\!\?]'
    result = re.findall(pattern, output)
    if len(result) == 0:
        print("\nERROR, TRIMMING FAILED. With short inputs, try setting full_sentences=False.\n")
        sys.exit(0)
    return result[0]


def generate_text(  
                    string="",
                    file="",
                    words=False, 
                    letters=False, 
                    case_sensitive=False, 
                    full_sentences=True, 
                    preserve_newlines=False,
                    resolution=2,
                    output_size=500,
                    ):

    m = MarkovGenerator()

    if words:
        m.letters = False

    if letters:
        m.letters = True

    m.case_sensitive = case_sensitive
    m.full_sentences = full_sentences
    m.RESOLUTION = resolution
    m.OUTPUT_SIZE = output_size

    if len(file) > 0:
        m.generate_corpus(m.input(file))
    elif len(string) > 0:
        m.generate_corpus(string)
    return m.output()
