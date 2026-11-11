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

    def breed(self, dna_other): # takes half of a string and another half of a string and merges them
        new_dna = []
        new_dna.append(self.dna[0:4])
        new_dna.append(dna_other[4:8])
        new_dna = "".join(new_dna)
        return new_dna


# a list of people with the best scores, a function that randomly inserts two into the breeder function

def create_community():
    com = []
    for i in range(20):
        com.append(Origin(str_generator()))
    return com


def compare_scores():
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
the_sec = Origin(str_generator())

print(the_first.dna)
print(the_first.score_fun(goal))
print(the_sec.dna)
print(the_sec.score_fun(goal))

child = Origin(the_first.breed(the_sec.get_dna()))
print(child.get_dna())
print(child.score_fun(goal))