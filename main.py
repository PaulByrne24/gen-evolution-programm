"""
GOAL: guess a random 8 letter string of text
METHOD: a parent guesses and is told how good their guess is, the best mate with the other top 20 guesses (randomly) 
and a random portion of their Dna (guess) is mixed with the other, the child is then the product of this fusion,
they are then compared and the best are then fused together. This cycle repeats until the string is guessed.
"""

from random import randint

class Origin: # the blueprint for the "people" of the community. Their "dna" are their guesses
    def __init__(self, dna):
        self.dna = dna

    def get_dna(self):
        return self.dna

    def score_fun(self, guess):
        score = 0
        for i in range(8):
            if self.dna[i] == guess[i]:
                score += 1

        return score / len(self.dna)

    def breed(self, dna_other): # takes half of a string and another half of a string and merges them
        new_dna = []
        x = randint(3,6)
        dice_roll = randint(1, 100)
        new_dna.append(self.dna[0:x])
        new_dna.append(dna_other[x:8])
        new_dna = "".join(new_dna)
        if dice_roll <= 10:
            new_dna = self.mutate(new_dna)

        return new_dna

    def mutate(self, new_dna):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_dna = list(new_dna)
        new_dna[randint(0, len(new_dna)-1)] = alphabet[randint(0, 25)]
        return "".join(new_dna)

class Community:
    def __init__(self, community):
        self.community = community # the first dict of the community, looks kind of like this: {"dna1": score, "dna2": score, ...}
        self.sorted_scores = []
        self.next_gen = []
        self.best_guess = 0
        self.best_score = 0

    def sort_scores(self):
        self.sorted_scores = sorted(self.community.items(), key=lambda item: float(item[1]), reverse=True)
        # to give my future self a reference, sorted_scores looks like this: (("dna_best": score_best), ("dna_sec": score_sec), ...)
        self.best_guess = self.sorted_scores[0][0].get_dna()
        self.best_score = self.sorted_scores[0][1]
        self.community.clear()
        # clears old community and makes it ready to be replaced with the next generation
        return self.sorted_scores

    def make_new_gen(self):
        top_community = self.sorted_scores
        n = len(top_community)
        self.next_gen.clear()
        # clears the next generation incase it was already full with the last "next" generation
        for i in range(n):
            if i <= n//3:
                new_child = Origin(top_community[i][0].breed(top_community[randint(1, i+1)][0].get_dna()))
                # while I wanted the breeding process to be random I made the randint so that the top third has a guaranteed chance of breeding with the top third's
                self.next_gen.append(new_child)
            else:
                new_child = Origin(top_community[i][0].breed(top_community[randint(0, n-1)][0].get_dna()))
                self.next_gen.append(new_child)
        # to remember, this is creating new "Origins", whose dna is the bred version of it's parents
        self.replace_old_gen()
    
    def replace_old_gen(self): # recreates the dict community with members of the next_generation list
        for i in self.next_gen:
            self.community[i] = i.score_fun(goal)
        return self.community

"""Finally got it to work. It's fucking awesome that I managed to make this. It's been fun and a nightmare to
make this and to be honest I think I've gotten really good at working with lists. At least a lot better than I used to be.
I do want to tighten it up a bit because I feel it's a bit unreadable at the moment. I made the strings 16 letters in this version 
and it still works which is awesome.
But for now if it's not broken I'm not gonna fix it."""

def create_community():
    com = {}
    for i in range(50):
        pers = Origin(str_generator())
        com[pers] = pers.score_fun(goal)
    return com

def str_generator(): # makes the 8 letter string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand_str = []
    for i in range(8):
        rand_str.append(alphabet[randint(0, 25)])

    rand_str = "".join(rand_str)
    return rand_str

goal = str_generator()

the_community = create_community()
community = Community(the_community)

gen = 0
while community.best_score < 1.0:
    if gen % 500 == 0:
        print("GEN:", gen, "best:", community.best_score, community.best_guess)
    print("GEN:", gen)
    community.sort_scores()
    community.make_new_gen()
    gen += 1
print("GOAL:", goal, "BEST GUESS:", community.best_guess, "SCORE:", community.best_score)