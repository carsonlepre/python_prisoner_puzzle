538 Prisoner Puzzle

PUZZLE:

One hundred prisoners are put into 100 completely isolated cells, numbered 1 to 100. Once they are in their cells, they cannot
communicate with each other in any way. They are taken by the warden one at a time, but in no particular order, to a special
room, Cell 0, in which there are two levers. As the prisoners enter the room, each lever is either up or down, but the levers’
starting positions are unknown. When in the room, a prisoner must flip exactly one of the levers. At any point, any prisoner
may declare to the warden that all of the prisoners have been to the room. (The warden will take prisoners to the room
indefinitely until someone makes a guess.) If the prisoner is correct, they are all released. If not, they are all executed.
What strategy can the prisoners devise beforehand that will guarantee their release? How many trips to Cell 0 will it take on
average before they are released?




SOLUTION, described on the fivethirtyeight website (my solution code in python_538.py file):

"To guarantee their freedom, the prisoners can establish a division of labor. First, they designate one among them as the 
Counter. The rest are merely drones. Second, they designate one of the levers the “count lever” and one of the levers the
“dummy lever.” The rest of the details are adapted from the explanation of this week’s winner, Ethan:

The Counter’s job is simple — he adds one to his running total every time he enters Cell 0 and finds the count lever up, and
when he does, he flips the count lever back down. If he sees the count lever down, he leaves it alone and flips the dummy
lever. The drones do the opposite. If they enter Cell 0 and see the count lever down, they flip it up. If they see it up, they
leave it alone and flip the dummy lever instead. Every drone should flip the count lever only twice during their entire stay
in the prison. The Counter should declare to the warden that everyone has entered the room — and guarantee their freedom — 
once his tally hits 199.

Why 199 and not 99? And why do the drones need to flip the count lever twice? Because the prisoners don’t know the initial 
positions of the levers, there is a small chance that the Counter is chosen to enter Cell 0 first and enters to finds the 
count lever up. (This is only a 1-in-200 chance, but 100 lives are on the line!) In that case, he wouldn’t know for sure 
whether to add a legitimate tally to his total or not. So by counting through the prisoners twice, the Counter can be 100 
percent sure they’ve all been to the room and avoid any chance of execution. Once the tally reaches 199, the Counter can be 
certain that 99 of the prisoners have entered Cell 0 at least twice and all 100 prisoners have entered it at least once.

This process will take roughly 20,000 total prisoner trips to the room, on average. You can arrive at a rough approximation of 
this total by observing that the Counter enters the room about once every 100 trips, and he needs to tally 199 up levers, for 
a total of 19,900. (But this ignores those occasions where the Counter enters the room twice finding the count lever 
unflipped.)"