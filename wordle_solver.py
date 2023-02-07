from collections import Counter


def letter_repeats_multiplier(word):
    letter_set = set(word)
    return (5 + len(letter_set) - len(word)) * 0.2


class wordle_solver:
    def __init__(self):
        self.words = self.load_words()
        self.word_clues = self.words
        self.word_psbl = self.words
        self.cnts = self.prevalence()
        self.word = [None] * 5
        self.not_in_word = set()
        self.in_word_ordered = {i: [] for i in range(5)}

    # Loads a list of words from a file
    @staticmethod
    def load_words():
        # Extracts text from file
        with open('wordle-allowed.txt', 'r') as text:
            lines = text.readlines()

        # Gets rid of new lines in list
        words = []
        for line in lines:
            words.append(line.replace("\n", ""))

        return words

    # Calculates the prevalence of each letter in the word clues
    def prevalence(self):
        cnts = [Counter() for i in range(5)]
        for word in self.word_psbl:
            cnts[0][word[0]] += 1
            cnts[1][word[1]] += 1
            cnts[2][word[2]] += 1
            cnts[3][word[3]] += 1
            cnts[4][word[4]] += 1
        return cnts

    # Prints the top 10 word clues based on prevalence
    def clue(self):
        self.update_words()
        word_scores = []
        self.cnts = self.prevalence()
        for word in self.word_clues:
            score = 0
            for letter in range(5):
                score += self.cnts[letter][word[letter]]
            score *= letter_repeats_multiplier(word)
            score = round(score)
            word_scores.append([word, score])
        word_scores.sort(key=lambda w: w[1])
        print(word_scores[-1:-10:-1])
        print(len(word_scores))

    # Prints the top 10 possible words based on prevalence
    def psbl_word(self, word_print=False):
        self.update_words()
        word_scores = []
        self.cnts = self.prevalence()
        for word in self.word_psbl:
            score = 0
            for letter in range(5):
                score += self.cnts[letter][word[letter]]
            score *= letter_repeats_multiplier(word)
            score = round(score)
            word_scores.append([word, score])
        word_scores.sort(key=lambda w: w[1])
        if word_print:
            print(word_scores[-1:-10:-1])
            print(len(word_scores))
        else:
            return word_scores[-1][0]

    # Updates the list of clues and possible words based on letters that are known to be in or not in the word
    def update_words(self):
        self.word_clues = [word for word in self.word_clues
                           if all(character not in word for character in self.not_in_word)]

        self.word_psbl = [word for word in self.word_psbl
                          if all(character not in word for character in self.not_in_word)
                          and all(word[pos] == self.word[pos] or self.word[pos] is None for pos in range(5))
                          and all(word[pos] != character for pos in range(5) for character in self.in_word_ordered[pos])]

    def out_word_add(self, letters):
        for letter in list(letters):
            if letter not in self.word and not any(letter in lst for lst in self.in_word_ordered.values()):
                self.not_in_word.update(letter)

    def letter_add(self, letter, pos):
        self.not_in_word.discard(letter)
        self.word[pos] = letter

    def out_of_order_letter_add(self, letter, pos):
        self.not_in_word.discard(letter)
        self.in_word_ordered[pos].append(letter)

    def complete(self):
        if None not in self.word:
            return True
        else:
            return False
