#Main method
#Project truty.ai, DoraHacks hackathon

#importing random for random()
import random

#importing functions
import excScore
import captLog
import pldChoices

#Creating data array

#Seeindg data with 0's
num_people = 6
data = [['Austin',0,0,0,0,0], ['Sidney',0,0,0,0,0], ['Becky',0,0,0,0,0], 
['Andrew',0,0,0,0,0], ['Kevin',0,0,0,0,0], ['Mitali',0,0,0,0, 0]]

#Seeing data with student names via input
for i in range(num_people):
    print("Please enter the names of each student {i}:".format(**locals()))
    data[i][0] = input() 
    name = data[i][0]
    print("Student {i} added as {name}".format(**locals()))

#Print all studnets to verify
print("Results:")
print("*****************")
for studentPrint in range(num_people):
    print(data[studentPrint])

#Creating weighted array for later
weight_arr = [1, 1, 1]

#Implement AI function
wrand = [1, 1, 1]
wrand[0] = weight_arr[0] * random.randrange(90000,110000)/100000
wrand[1] = weight_arr[1] * random.randrange(90000,110000)/100000
wrand[2] = weight_arr[2] * random.randrange(90000,110000)/100000

#Getting score
for gettingScores in range(num_people):
    name = data[gettingScores][0]
    cap_score = captLog.cap_log(name) * wrand[0] / (data[gettingScores][2] + 1)
    score = excScore.exer_score(name) * wrand[0] / (data[gettingScores][2] + 1)
    pld_score = (10 - data[gettingScores][2]) * wrand[0] / (data[gettingScores][2]+1)
    data[gettingScores][4] = cap_score + score + pld_score 

#Creating chocies store
choices = pldChoices.pld_choices(data)

#Printing choices and changes PLD average
print(data[choices[0]])
print(data[choices[1]])

#Setting initial Target/Error to 0
error = 0
sum = 0
for leadChoice in range(num_people):
    name = data[choices[0]][0]
    print("Enter your vote for " + name)
    sum += int(input())
data[choices[0]][1] = (data[choices[0]][1] + sum)/(data[choices[0]][1]+1)
error += sum;
sum = 0
for assitantChoice in range(num_people):
    name = data[choices[1]][0]
    print("Enter your vote for " + name)
    sum+= int(input())
data[choices[1]][1] = (data[choices[1]][1] + sum)/(data[choices[1]][1]+1)
error += sum

#Checking for target/error for AI, more magic happens

if error > 0:
    for sendMemory in weight_arr:
        print("DEBUG---->")
        print(sendMemory)
        sendMemory = int(sendMemory)
        print("Results before ----> INPUT:")
        print(weight_arr)
        weight_arr[sendMemory] = weight_arr[sendMemory] + (weight_arr[sendMemory] - wrand[sendMemory]) * .9
        print("Results after ----> OUTPUT:")
        print(weight_arr)
              
else:
    for sendMemory in weight_arr:
        print("Results before ----> INPUT:")
        print(weight_arr)
        weight_arr[sendMemory] = weight_arr[sendMemory] - (weight_arr[sendMemory] - wrand[sendMemory]) * 1.1
        print("Results after ----> OUTPUT:")
        print(weight_arr)
    
