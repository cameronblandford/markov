import random
import re
import sys
from collections import defaultdict


class MarkovGenerator:
    corpus = defaultdict(list)
    text_in = ""

    letters = False
    case_sensitive = False
    full_sentences = True
    preserve_newlines = True

    RESOLUTION = 2
    OUTPUT_SIZE = 500

    def __init__(self):
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
            if self.case_sensitive:
                next_word = random.choice(self.corpus[' '.join(seed_words)])
            else:
                next_word = random.choice(self.corpus[' '.join(seed_words).
                                          lower()])

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
        print("\nERROR, TRIMMING FAILED\n")
        sys.exit(0)
    return result[0]
