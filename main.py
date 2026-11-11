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
        self.score = 0
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
    def __init__(self, community):
        self.community_list = community # list of Origins
        self.id_and_score = {}
        self.sorted_scores = []
        self.next_gen = []
        self.best_score = 0

    def create_comm_dict(self):
        for x in range(len(self.community_list)):
            self.id_and_score[self.community_list[x]] = self.community_list[x].score_fun(goal)
        self.community_list.clear()
        return self.id_and_score

    def sort_scores(self):
        self.sorted_scores = sorted(self.id_and_score.items(), key=lambda item: float(item[1]), reverse=True)
        self.best_score = self.sorted_scores[0][1]
        self.id_and_score.clear()
        return self.sorted_scores

    def make_new_gen(self):
        top_community = self.sorted_scores
        self.next_gen.clear()
        for i in range(len(top_community)):
            new_child = Origin(top_community[i][0].breed(top_community[randint(1, len(top_community)-1)][0].get_dna()))
            self.next_gen.append(new_child) # takes the first person in community and breeds them with the last 
        # to remember, this is creating new "Origins". The first persons breed function is called upon and I added the last persons dna as the secondary dna
        self.replace_old_gen()
    
    def replace_old_gen(self):
        self.community_list = list(self.next_gen)
        return self.community_list

"""Sorter finally finished. It kind of works, and made a central loop. Only thing left is the mutations. This code was a fucking nightmare to write
and rewrite. I think I reset like 4 times before getting an epiphany and finishing the last bit"""

def create_community():
    com = []
    for i in range(50):
        com.append(Origin(str_generator()))
    return com

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
# print("Pers1 DNA:", pers1.summary)
# print("Pers2 Dna:", pers2.get_dna())

# child = Origin(pers1.breed(pers2.get_dna()))
# print("Child dna:", child.get_dna())

the_community = create_community()
community = Community(the_community)
gen = 0
while community.best_score < 1.0:
    if gen % 100 == 0:
        print("GEN:", gen, "best:", community.best_score)
    print("GEN:", gen)
    community.create_comm_dict()
    community.sort_scores()
    community.make_new_gen()
    gen += 1


