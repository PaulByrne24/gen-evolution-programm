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

    def score_fun(self, goal):
        score = 0
        for i in range(len(self.dna)):
            if self.dna[i] == goal[i]:
                score += 1

        return score

    def breed(self, dna_other): # takes half of a string and another half of a string and merges them
        new_dna = []
        x = randint(int(0.375*len(self.dna)), int(0.75*len(self.dna)))
        dice_roll = randint(1, 100)
        new_dna.append(self.dna[0:x])
        new_dna.append(dna_other[x:len(self.dna)])
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
    def __init__(self, community, goal):
        self.community = community # the first dict of the community, looks kind of like this: {"dna1": score, "dna2": score, ...}
        self.goal = goal
        self.sorted_scores = []
        self.next_gen = []
        self.best_guess = 0
        self.best_score = 0
        self.avg_score = 0

    def sort_scores(self):
        self.sorted_scores = sorted(self.community.items(), key=lambda item: item[1], reverse=True)

        total_score = 0
        for i in range(len(self.sorted_scores)):
            total_score += self.sorted_scores[i][1]/len(self.goal)
        self.avg_score = total_score / len(self.sorted_scores)
        # to give my future self a reference, sorted_scores looks like this: (("dna_best": score_best), ("dna_sec": score_sec), ...)
        self.best_guess = self.sorted_scores[0][0].get_dna()
        self.best_score = self.sorted_scores[0][1]/len(self.goal)
        # clears old community and makes it ready to be replaced with the next generation
        return self.sorted_scores

    def make_new_gen(self):
        n = len(self.sorted_scores)
        self.community.clear()
        self.next_gen.clear()
        # clears the next generation incase it was already full with the last "next" generation
        for i in range(n):
            if i <= n//3:
                new_child = Origin(self.sorted_scores[i][0].breed(self.sorted_scores[randint(0, n//3)][0].get_dna()))
                # while I wanted the breeding process to be random I made the randint so that the top third has a guaranteed chance of breeding with the top third's
                self.next_gen.append(new_child)
            else:
                new_child = Origin(self.sorted_scores[i][0].breed(self.sorted_scores[randint(0, n-1)][0].get_dna()))
                self.next_gen.append(new_child)
        # to remember, this is creating new "Origins", whose dna is the bred version of it's parents
        self.replace_old_gen()
    
    def replace_old_gen(self): # recreates the dict community with members of the next_generation list
        keep_best = self.sorted_scores[0][0] # [0][0] is the object Origin
        self.community[keep_best] = keep_best.score_fun(self.goal)
        for i in self.next_gen:
            self.community[i] = i.score_fun(self.goal)
        self.community.popitem()
        return self.community

"""Getting a lot better and much more familiar with how my program works. Have been experimenting with some changes like
saving the best of one generation for the next generation, and it's made it much more efficient which is awesome."""

def create_community(goal, size, str_length):
    com = {}
    for i in range(size):
        pers = Origin(str_generator(str_length))
        com[pers] = pers.score_fun(goal)
    return com

def str_generator(length): # makes the 8 letter string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand_str = []
    for i in range(length):
        rand_str.append(alphabet[randint(0, 25)])

    rand_str = "".join(rand_str)
    return rand_str