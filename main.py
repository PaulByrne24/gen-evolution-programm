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

        if self.score == len(self.dna):
            print("I am the winner")
        return self.score / len(self.dna)

    def breed(self, dna_other): # takes half of a string and another half of a string and merges them
        new_dna = []
        x = randint(3,5)
        new_dna.append(self.dna[0:x])
        new_dna.append(dna_other[x:8])
        new_dna = "".join(new_dna)
        return new_dna


# a list of people with the best scores, a function that randomly inserts two into the breeder function

def create_community():
    com = []
    for i in range(20):
        com.append(Origin(str_generator()))
    return com


def compare_scores(community):
    score_list = []
    for x in range(len(community)):
        score_list.append(community[x].score_fun(goal))
    score_list.sort(reverse=True)
    # takes the community and converts it all into a list of their scores, then sorts them from highest to lowest

    new_com = community[:int(len(community)/2)] # takes the first half of the community

    top_scorers = score_list[:int(len(score_list)/2)] # takes the first half of the community's scores
    
    print(top_scorers)
    children = []
    for i in range(len(top_scorers)):
        children.append(Origin(new_com[i].breed(new_com[len(new_com)-1-i].get_dna()))) # takes the first person in community and breeds them with the last 
    # to remember, this is creating new "Origins". The first persons breed function is called upon and I added the last persons dna as the secondary dna

    score_child = []
    for w in range(len(children)):
        score_child.append(children[w].score_fun(goal))

    return score_child

# works but problem is I can't use these variables outside the function, need to make it easier to work with.

def str_generator(): # makes the 8 letter string
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    rand_str = []
    for i in range(8):
        rand_str.append(alphabet[randint(0, 25)])

    rand_str = "".join(rand_str)
    return rand_str

goal = str_generator()
print("Goal", goal)

pers1 = Origin(str_generator())
pers2 = Origin(str_generator())
print("Pers1 DNA:", pers1.get_dna())
print("Pers2 Dna:", pers2.get_dna())

child = Origin(pers1.breed(pers2.get_dna()))
print("Child dna:", child.get_dna())
# print(compare_scores(create_community()))