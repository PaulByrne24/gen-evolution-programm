"""
GOAL: guess a random 8 letter string of text
METHOD: a parent guesses and is told how good their guess is, the best mate with the other top 20 guesses (randomly) 
and a random portion of their Dna (guess) is mixed with the other, the child is then the product of this fusion,
they are then compared and the best are then fused together. This cycle repeats until the string is guessed.
"""

from random import randint

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
        x = randint(3,5)
        new_dna.append(self.dna[0:x])
        new_dna.append(dna_other[x:8])
        new_dna = "".join(new_dna)
        return new_dna

class Community:
    def __init__(self):
        self.comm = self.create_community()
        self.score_comm = self.sort_scores(self.comm)
        self.next_gen = []

# a list of people with the best scores, a function that randomly inserts two into the breeder function
    def get_community(self):
        temp_list = []
        for x in range(len(self.comm)):
            temp_list.append(self.comm[x].get_dna())

        return temp_list


    def create_community(self):
        com = []
        for i in range(20):
            com.append(Origin(str_generator()))
        return com


    def sort_scores(self, comm):
        score_list = []
        for x in range(len(comm)):
            score_list.append(comm[x].score_fun(goal))
        score_list.sort(reverse=True)
        # takes the community and converts it all into a list of their scores, then sorts them from highest to lowest
        return score_list

    def make_new_gen(self):
        new_com = self.comm[:int(len(self.comm)/2)]
        top_scorers = self.score_comm[:int(len(self.score_comm)/2)]

        for i in range(len(top_scorers)):
            self.next_gen.append(Origin(new_com[i].breed(new_com[len(new_com)-1-i].get_dna()))) # takes the first person in community and breeds them with the last 
        # to remember, this is creating new "Origins". The first persons breed function is called upon and I added the last persons dna as the secondary dna

    def replace_old_gen(self):
        self.comm = self.next_gen

"""Huge Problem I didn't realize until now. I sorted the scores but didn't save their dna/list position. Meaning I have to now
manually sort through every one and find which score belongs to which dna. I've thought of a few ways of doing this: 
1. save the index of each dna and its score in a separate list and then call on that
2. make a manual sorter that compares each score and puts it from best to worst and at the same time moves the asociated dna to its postiion
3. don't sort the scores keep them as is but take the indicies of each one and breed them that way"""

def str_generator(): # makes the 8 letter string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand_str = []
    for i in range(8):
        rand_str.append(alphabet[randint(0, 25)])

    rand_str = "".join(rand_str)
    return rand_str

goal = str_generator()
print("Goal", goal)

# pers1 = Origin(str_generator())
# pers2 = Origin(str_generator())
# print("Pers1 DNA:", pers1.get_dna())
# print("Pers2 Dna:", pers2.get_dna())

# child = Origin(pers1.breed(pers2.get_dna()))
# print("Child dna:", child.get_dna())
new_comm = Community()
print("First Gen:", new_comm.get_community())
new_comm.make_new_gen()
print(new_comm.compare_scores(new_comm.comm))
print("Second Gen:", new_comm.get_community())
new_comm.make_new_gen()
print(new_comm.compare_scores(new_comm.comm))
new_comm.make_new_gen()
print(new_comm.compare_scores(new_comm.comm))