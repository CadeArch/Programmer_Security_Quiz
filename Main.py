from NutritionTool import *
import random

# importing the function i need to create the questions for the user
awarenessQuestionsObjects, behaviorQuestionsObjects = createQuestionObjects()

# this will print out the question objects in a readable format
# verifyQuestions()
# seeScoreSuggestions()

# grabbing all questions to ask developer and shuffling to minimize bias
allQuestions = awarenessQuestionsObjects + behaviorQuestionsObjects
random.shuffle(allQuestions)

# instructions
print("Answer the questions as honestly as you can to the best of your ability, this tool is to evaluate your personal "
      "\nsecurity nutrition level. The more accurately you answer the questions the more personal the suggestions will be.\n ")

print("please input your answers using the following Likert scale: "
      "\n0 = strongly disagree "
      "\n1 = disagree "
      "\n2 = neither agree or disagree "
      "\n3 = agree "
      "\n4 = strongly agree "
      "\n")

# asking for user input and storing data in the answer variable of the class
counter = 1
for x in allQuestions:
    x.answer = input("Q" + str(counter) + ": " + x.question)
    go = True
    while go:
        try:
            while x.answer.isalpha() or int(x.answer) < 0 or int(x.answer) > 4:
                x.answer = input("Answer must be one of the following 0-4: ")
            go = False
        except BaseException:
             x.answer = "n"

    counter += 1

# computing individual scores
workplaceBehaviorScore = 0
workplaceAwarenessScore = 0
personalBehaviorScore = 0
personalAwarenessScore = 0
for x in allQuestions:
    if x.focus == "personal" and x.type == "Awareness Question":
        personalAwarenessScore += int(x.answer) * x.weight
    if x.focus == "personal" and x.type == "Behavior Question":
        personalBehaviorScore += int(x.answer) * x.weight
    if x.focus == "workplace" and x.type == "Behavior Question":
        workplaceBehaviorScore += int(x.answer) * x.weight
    if x.focus == "workplace" and x.type == "Awareness Question":
        workplaceAwarenessScore += int(x.answer) * x.weight

# showing suggestions based on answers
print()
y = 0
for x in allQuestions:
    y += 1
    if int(x.answer) < 3:
        print("Suggestion for Question " + str(y) + ": " + x.suggestion)
print()

# showing user individual scores
pbp = (personalBehaviorScore / 40) * 100
pap = (personalAwarenessScore / 40) * 100
wbp = (workplaceBehaviorScore / 20) * 100
wap = (workplaceAwarenessScore / 20) * 100
print("Personal Behavior Score: " + str(personalBehaviorScore) + "/40 " + "(" + str(pbp) + "%" + ")"
      "\nPersonal Awareness Score: " + str(personalAwarenessScore) + "/40 " + "(" + str(pap) + "%" + ")"
      "\nworkplace Behavior Score: " + str(workplaceBehaviorScore) + "/20 " + "(" + str(wbp) + "%" + ")"
      "\nworkplace Awareness Score: " + str(workplaceAwarenessScore) + "/20 " + "(" + str(wap) + "%" + ")")

# showing total score
totalScore = workplaceBehaviorScore + personalBehaviorScore + personalAwarenessScore + workplaceAwarenessScore
tsp = (totalScore / 120) * 100
print("Total Score: " + str(totalScore) + "/120 " + "(" + str(tsp) + "%" + ")\n")

# if the indivudual scores are less than 75 percent for each section it will give further guidance
if personalBehaviorScore < 30:
    print("your personal habits are inhibiting your 'security nutrition', always strive to write secure code and verify "
          "\nthat the code you are using (if from a third party) is secure to increase your 'security nutrition' level.\n")

if personalAwarenessScore < 30:
    print("your personal awareness of security is inhibiting your 'security nutrition' become more familiar with the  "
          "\nsecurity best practices located in the this file to increase your 'security nutrition' level.\n")

if workplaceBehaviorScore < 15:
    print("your workplaces habits and behaviors may be inhibiting your 'security nutrition' just because no one else is"
          "\ndoing these things be the one to step up to the plate and take the initiative to create safer more secure code!\n")

if workplaceAwarenessScore < 15:
    print("your workplaces awareness of security may be inhibiting your 'security nutrition' if no one else is asking the "
          "\nquestions, be the one to bring it up to increase general awareness!\n")

if totalScore >= 90:
    print("good job on your security 'nutrition level'! Keep on learning about security and keep writing secure code!\n")

    print("would you like to see some suggestions to better your security behaviors and awareness?")
    answer = str(input("(y or n): "))
    incorrect = True
    while incorrect:
        if answer == "y":
            displaySuggestions(allQuestions)
            incorrect = False
        elif answer == "n":
            incorrect = False
        else:
            answer = str(input("(y or n): "))


#giving credit to suggestions
print("\nThe suggestions presented are based on 3 research studies whose titles are: "
      "\n\t'Security in the Software Development Lifecycle' (Assal)"
      "\n\t'API Blindspots: Why Experienced Developers Write Vulnerable Code' (Oliveira)"
      "\n\t'You Get Where You’re Looking For The Impact of Information Sources on Code Security' (Acar)\n")

print("Thanks for taking the questionnaire! (see suggestions above)")

