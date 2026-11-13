from main import *
import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter desired population size: "))
length = int(input("Enter desired string length: "))
goal = str_generator(length=length)

the_community = create_community(goal, size=size, str_length=length)
community = Community(community=the_community, goal=goal)

gen = 0
scores = []
avg_scores = []
while community.best_score < 1.0:
    community.sort_scores()
    community.make_new_gen()
    gen += 1
    avg_scores.append(community.avg_score)
    scores.append(community.best_score)
print("GOAL:", goal, "BEST GUESS:", community.best_guess, "GUESSED IN:", gen, "Generations")

arr_scores = np.array(scores)
arr_avg = np.array(avg_scores)


plt.plot(arr_scores, color="blue", label="Best Score")
plt.plot(arr_avg, color="orange", label="Average Score")

plt.grid()
plt.xlabel("Generation")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
plt.legend(loc="lower right")
plt.show()