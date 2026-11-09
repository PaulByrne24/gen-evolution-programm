"""
GOAL: guess a random 8 letter string of text
METHOD: a parent guesses and is told how good their guess is, the best mate with the other top 20 guesses (randomly) 
and a random portion of their Dna (guess) is mixed with the other, the child is then the product of this fusion,
they are then compared and the best are then fused together. This cycle repeats until the string is guessed.
"""

import random

class Origin: # the parents, the original guessers
    def __init__(self, dna):
        self.dna = dna
        self.score = 0

    def get_dna(self):
        return self.dna

    def score_fun(self, guess):
        for i in range(8):
            if self.dna[i] == guess[i]:
                self.score += 1
        return self.score / len(self.dna)

    def breed(self):
        pass

def str_generator(): # makes the 8 letter string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand_str = []
    for i in range(8):
        rand_str.append(alphabet[random.randint(0, 25)])

    rand_str = "".join(rand_str)
    return rand_str

goal = str_generator()
print(goal)
the_first = Origin(str_generator())
print(the_first.dna)
print(the_first.score_fun(goal))
