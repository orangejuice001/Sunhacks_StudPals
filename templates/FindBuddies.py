import openai

className = input("Enter the Class Name you're trying to find a Study Buddy for. ")
timeToStudy = float(input("Input the number of hours you are willing to study for. "))
stressed = int(input("On a scale of 0 - 5, how stressed are you? [ 0 - cool as a cucumber; 5 - DYING]. "))
timeToDeadline = float(input("Input the number of hours you are have until the deadline between 1-10, pick 10 if more than 10 hours are left. "))


existingUsers = [['Sindhu', ['CSE355', 'CSE330', 'CSE360'], 2.5, 3, 4], ['Tejal', ['CSE475', 'CSE445', 'CSE492'], 3, 4, 1],
                      ['Rhea', ['CSE330', 'CSE492'], 4.5, 3, 4], ['John', ['CSE110', 'CSE120'], 6, 2, 2], ['Anushka', ['CSE355', 'CSE360'], 7, 4, 2],
                      ['Stacy', ['CSE205','CSE230'], 3, 3, 2],  ['James', ['CSE110', 'CSE495'], 5, 2, 3],  ['Amaya', ['CSE230', 'CSE472'], 5.5, 3, 4], 
                        ['Saharya', ['CSE365', 'CSE472'], 6, 3, 3],  ['Bob', ['CSE230', 'CSE492'], 5, 2, 3],  ['Dylan', ['CSE340', 'CSE492'], 7, 3, 2],
                         ['Thomas', ['CSE330', 'CSE493'], 8, 3, 2],  ['Mike', ['CSE340', 'CSE492'], 4, 2, 3],  ['Gamaya', ['CSE355', 'CSE493'], 6, 3, 2], 
                           ['Lizzie', ['CSE350', 'CSE492'], 6, 3, 3],  ['Tara', ['CSE355', 'CSE464'], 3.5, 3, 3],  ['Kelsie', ['CSE330', 'CSE464'], 4, 3, 4]]

potentialStudyBuddies = list()
result = True
for i in range(0, len(existingUsers)):
    if className in existingUsers[i][1]:
        potentialStudyBuddies.append(existingUsers[i])
    
if len(potentialStudyBuddies) == 0:
    result = False
    
finalProspects = list()
timeList = list()

# Linear Model used to develop this model will be weighted followingly:
# 1 - 40 % of  (Difference between 2 buddies time to study)
# 1 - 30 % of  (Difference between 2 buddies Stress)
# 1 - 30 % of  (Difference between 2 buddies Time left for deadline)
# We subtract the difference from 1 since the greater the difference the lower it should be rated
# Higher score is good

scoreList = list()

def sortByScore():
    for k in range(0, len(potentialStudyBuddies)):
        timeDiff = abs(timeToStudy - potentialStudyBuddies[k][2])
        stressDiff = abs(stressed - potentialStudyBuddies[k][3])
        deadlineDiff = abs(timeToDeadline - potentialStudyBuddies[k][4])
        score = (1 - timeDiff) * 0.4 + (1 - stressDiff) * 0.3 + (1 - deadlineDiff) * 0.3
        scoreList.append([potentialStudyBuddies[k][0], score])

    scoreList.sort(key=lambda x: x[1], reverse = True)
    
    
    for i in range(0, len(scoreList)):
        for j in range(0, len(potentialStudyBuddies)):
            if scoreList[i][0] == potentialStudyBuddies[j][0]:
                finalProspects.append(potentialStudyBuddies[j])


def findBuddies():
    sortByScore()
    # #ask chatgpt to sort by the remaining parameters
    # openai.api_key = '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'
    # messages = [ {"role": "system", "content":  "You are a intelligent assistant."} ] 
    # message = "Find the best match for this user from finalProspects based on the stressed variable and timeToDeadLine and only display the result in the form of a list." # question
    # if message: 
    #     messages.append(             
    #         {"role": "user", "content": message},         
    #     ) 
    #     chat = openai.ChatCompletion.create( 
    #         model="gpt-3.5-turbo", messages=messages 
    #     ) 
    # reply = chat.choices[0].message.content 
    # print(f"ChatGPT: {reply}") 
    # messages.append({"role": "assistant", "content": reply}) 

        

    print('The matching buddies for you are ranked:')

    print("\nFinal Prospects: ")

    for i in range(0, len(finalProspects)):
        print(finalProspects[i])

if result == True:
    findBuddies()
    
else:
    print("No study buddies are taking this class")


