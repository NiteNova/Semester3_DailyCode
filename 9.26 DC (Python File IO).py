import random

myfile = open("scores.txt", "r") #Open the "scores.txt" file in read mode
lines = myfile.readlines() #Read all lines from the file
myfile.close() 

# Convert each line to a tuple of (score, name) and store them in a list
scores = [(int(line.split()[0]), line.split()[1].strip()) for line in lines]

#print the stuff in the list
for score, name in scores: 
    print(score, " - ", name)
#insert game logic here!


num = random.randrange(1, 101)
score = 5000
progress = 0
while progress < 3:
    check_num = int(input("Guess between 1-100: "))
    if check_num > num:
        print("Testing num", num)
        score -= 100
        #print("Lower")
    elif check_num < num:
        print("Testing num", num)
        score -= 100
        #print("Higher")
    elif check_num == num:
        print("You won!")
        progress += 1
        num = random.randrange(1, 101)
        print("Progress: " + str(progress)+'/3')
    else:
        print("Not a valid number") 



#get user info
user_score = (score) #this part should be automated in your game
user_name = input("Enter your name: ")

scores.append((user_score, user_name))#Append the user's score and name to the scores list
scores.sort(reverse=True) #Sort the scores list in descending order

while len(scores) > 10:
    scores.pop()
    
myfile = open("scores.txt", "w") #Open the "scores.txt" file in write mode
iterate = [(int(i.split()[0]), i.split()[1]) for i in lines]
iterate.append((user_score, user_name))
iterate.sort(reverse=True, key=lambda x: x[0])
for score, name in iterate:
    myfile.write(f"{score} {name}\n")
for score, name in scores: 
    print(score, " - ", name)
myfile.close()  # Close the file after writing