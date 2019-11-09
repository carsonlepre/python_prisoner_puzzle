# Python Script for 
# 538.com Prisoner Puzzle
# Script by Carson Lepre

import os
import numpy as np
import random

first_lever_state = random.randint(0,1) # count lever position, randomized initially
second_lever_state = random.randint(0,1) # dummy lever position, randomized initially
#print(str(first_lever_state) + " " + str(second_lever_state))
#print("------")

prisoners = np.arange(0,99,1) # Generate list of prisoners
lever_tally = 0 # Counter for number of times COUNT PRISONER sees the COUNT LEVER in "up" position.
visit_tally = 0 # Counter for number of visits by any prisoner to Cell Zero

random.shuffle(prisoners)

total_runs_to_try = 100 # We want to find the average number of visits it would take to free the prisoners 
                        # if you ran this experiment many times. This variable describes the number of 
                        # tries we'll be testing. Let's just call it 100 runs.

total_runs = total_runs_to_try # We'll use this later to find the average.

total_runs_tally = 0

while total_runs > 0:
    total_runs -= 1
    lever_tally = 0
    visit_tally = 0
    random.shuffle(prisoners)

    while lever_tally < 199:
        first_lever_state = random.randint(0,1) # Randomize count lever position before every iteration
        second_lever_state = random.randint(0,1) # Randomize dummy lever position before every iteration
        random.shuffle(prisoners)

### Encounter possibilies are:
### count lever up, dummy lever up 
### count lever down, dummy lever up
### count lever up, dummy lever down
### count lever down, dummy lever down

        for i in prisoners:
            visit_tally += 1
            if i == 0: # Let's say that PRISONER ZERO is the COUNT PRISONER
                if first_lever_state == 0 and second_lever_state == 0: ## Count lever up, dummy lever up
                    first_lever_state = 1 # COUNT PRISONER flips COUNT LEVER back down
                    second_lever_state = 0
                    lever_tally += 1 #(COUNT PRISONER increases tally)
                    if lever_tally > 198:
                        break
                elif first_lever_state == 0 and second_lever_state == 1: ## Count lever up, dummy lever down
                    first_lever_state = 1 # COUNT PRISONER flips COUNT LEVER back down
                    second_lever_state = 1
                    lever_tally += 1 #(COUNT PRISONER increases tally)
                    if lever_tally > 198:
                        break
                elif first_lever_state == 1 and second_lever_state == 0: ## Count lever down, dummy lever up
                    first_lever_state = 1
                    second_lever_state = 1 # COUNT PRISONER flips DUMMY LEVER
                elif first_lever_state == 1 and second_lever_state == 1: ## Count Lever down, dummy lever down
                    first_lever_state = 1
                    second_lever_state = 0 # COUNT PRISONER flips DUMMY LEVER                  
            else:
                if first_lever_state == 0 and second_lever_state == 0:
                    first_lever_state = 0
                    second_lever_state = 1
                elif first_lever_state == 0 and second_lever_state == 1:
                    first_lever_state = 0
                    second_lever_state = 0
                elif first_lever_state == 1 and second_lever_state == 0:
                    first_lever_state = 0
                    second_lever_state = 0
                elif first_lever_state == 1 and second_lever_state == 1:
                    first_lever_state = 0
                    second_lever_state = 1                 
    print("RUN: " + str(visit_tally))
    total_runs_tally += visit_tally
average_tally = total_runs_tally / total_runs_to_try
print("AVG: " +str(average_tally))