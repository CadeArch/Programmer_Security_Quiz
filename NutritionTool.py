from BehaviorQuestion import BehaviorQuestion
from AwarenessQuestion import AwarenessQuestion

# these are awareness personal
q1 = "How important is it to have security in mind during ALL stages of software development?"
q2 = "do you generally think of security in most stages of your code development?"
q3 = "Do you believe that libraries of reusable code have security faults within them?"
q4 = "Do you generally think of ways your codes security could be breached when writing code? "
q5 = "Do you believe most apps on the Appstore are fairly secure when it comes to security?"

# awareness workplace
q6 = "Would you say that tools used in your workplace to handle security are verified as working securely?"
q7 = "Does your workplace give opportunities for you to learn about security and security practices in general?"
q8 = "Would you say that security is taken into account in most stages of code development in your workplace?"
q9 = "Would you say that security is often discussed in your workplace for the code being developed?"
q10 = "would you agree that many security measures are being taken care of by the framework you are using at work?"

# these are Behavior personal
q11 = "Would you say that you follow security best practices as a developer to the best of your ability?"
q12 = "Would you say you generally look into possible security issues in the APIs you use in your developed code?"
q13 = "If using Code from online sources would you say you verify that the code in use is secure from a security standpoint?"
q14 = "If an app doesn’t contain use of very sensitive data would you tend to code with security In mind?"
q15 = "If you found an issue relating to the security of an application you wrote would you agree that you would fix it even when the fix wouldn’t affect the functionality of your app?"

# Behavior workplace
q16 = "Would you say you think of security in the DESIGN STAGE of developing code at your workplace?"
q17 = "Would you say you think of security while IMPLEMENTING code at your workplace?"
q18 = "Would you say that you test for security while in the TEST STAGE of developing code at your workplace?"
q19 = "Would you say you have a code ANALYSIS STAGE at your workplace?"
q20 = "Would you say security is considered during the code REVIEW STAGE of code development at your workplace?"

# suggestions if they score less then 3 for each question
s1 = "Hala Assal found that security should be explored during all stages of code development. This way developers will have the best chance on creating secure code."
s2 = "Wether you are a designer, developer, tester, or reviewer, all are responsible for the security of developed code. The more eyes looking and thinking about it the better (Assal)." \
     " \n\t\t\t\t\t\t\tAnd if it is a personal project where you are doing all stages, keep security in mind during all stages of your development!"
s3 = "Daniela Oliveira and her team found that developers tend to trust APIs but can misunderstand or misuse them, introducing vulnerabilities. Make sure you know the tool your using."
s4 = "You may feel you lack the knowledge to develop secure code, the more you think of your code with more openess," \
        " being curious or imaginative, you will be more likely to find the faults (Oliveira)."
s5 = "In a study done by Yasmin Acar they found almost 20,000 apps from the appstore that were vulnerable to 'man in the middle' attacks. As developers we must assure that the code we " \
        "\n\t\t\t\t\t\twrite AND the code we use from other sources are secure."
s6 = "Acar found that sometimes workplaces build thier own frameworks to handle common security features, This may improve security, but verifying the frameworks" \
        " security is a necessary preliminary step."
s7 = "If you think your workplace gives no opportunity to learn more of security go ask! and if the case may be that they do not, you may have to take matters into your own " \
        "hand and learn yourself."
s8 = "Hala Assal took many lists of best practices for code security in development and made a concise, condensed list of best practices. Security should be explored in ALL stages " \
        "of code development."
s9 = "If no one is talking about security, there is a good chance no one is thinking about it, and if that is the case important things " \
     "could be being overlooked! So speak up and ask the questions!"
s10 = "If security isn't being taken care of by the framework, assure that someone is taking care of it! "
s11 = "Everyone starts somewhere! if you are unaware of the best practices or don't follow them currently, familiarize yourself with the security best practices included in this folder! "
s12 = "Daniela Oliveira found that many programmers often blindly trust APIs or misunderstand and misuse them introducing vulnerabilities. Assure you are " \
        "familiar with how it was meant to be used!"
s13 = "Yasemin Acar found that oftentimes online sources (Stack Overflow) for code development may help with functionality but often " \
      "do not consider security in their responses. Always verify that the code you use is secure."
s14 = "It may be easy to rationalize not putting in the effort to create secure code but if you make it a habit the online world would be a much more secure place!"
s15 = "It may be easy to rationalize not puting effort into the security of code, but it is a shared responsibility and we should all work together to make it happen (Assal)."
s16 = "Security best practices include thinking of security while in the DESIGN STAGE of code development (Assal)."
s17 = "Security best practices include thinking of security while in the IMPLEMENTATION STAGE of code development (Assal)."
s18 = "Security best practices include testing for security while in the TEST STAGE of code development (Assal)."
s19 = "Not everyone has a Code ANALYSIS STAGE in software development, but this is a great time use tools to evaluate " \
      "your code for security issues, its part of security best practices! (Assal)."
s20 = "Security best practices include thinking of security while in the REVIEW STAGE of code development (Assal)."

# low area score suggestions
personalBehaviorSuggestion = "your personal habits are inhibiting your 'security nutrition', always strive to write secure code and verify " \
          "\nthat the code you are using (if from a third party) is secure to increase your 'security nutrition' level.\n"

personalAwarenessSuggestion = "your personal awareness of security is inhibiting your 'security nutrition' become more familiar with the  " \
          "\nsecurity best practices located in the this file to increase your 'security nutrition' level.\n"

workplaceBehaviorSuggestion = "your workplaces habits and behaviors may be inhibiting your 'security nutrition' just because no one else is" \
          "\ndoing these things be the one to step up to the plate and take the initiative to create safer more secure code!\n"

workplaceAwarenessSuggestion = "your workplaces awareness of security may be inhibiting your 'security nutrition' if no one else is asking the " \
          "\nquestions, be the one to bring it up to increase general awareness!\n"

# putting the suggestions into an array to work with
awarenessSuggestions = []
behaviorSuggestions = []

awarenessSuggestions.append(s1)
awarenessSuggestions.append(s2)
awarenessSuggestions.append(s3)
awarenessSuggestions.append(s4)
awarenessSuggestions.append(s5)
awarenessSuggestions.append(s6)
awarenessSuggestions.append(s7)
awarenessSuggestions.append(s8)
awarenessSuggestions.append(s9)
awarenessSuggestions.append(s10)
behaviorSuggestions.append(s11)
behaviorSuggestions.append(s12)
behaviorSuggestions.append(s13)
behaviorSuggestions.append(s14)
behaviorSuggestions.append(s15)
behaviorSuggestions.append(s16)
behaviorSuggestions.append(s17)
behaviorSuggestions.append(s18)
behaviorSuggestions.append(s19)
behaviorSuggestions.append(s20)

# building and appending the list of questions
behaviorQuestions = []
awarenessQuestions = []

awarenessQuestions.append(q1)
awarenessQuestions.append(q2)
awarenessQuestions.append(q3)
awarenessQuestions.append(q4)
awarenessQuestions.append(q5)
awarenessQuestions.append(q6)
awarenessQuestions.append(q7)
awarenessQuestions.append(q8)
awarenessQuestions.append(q9)
awarenessQuestions.append(q10)

behaviorQuestions.append(q11)
behaviorQuestions.append(q12)
behaviorQuestions.append(q13)
behaviorQuestions.append(q14)
behaviorQuestions.append(q15)
behaviorQuestions.append(q16)
behaviorQuestions.append(q17)
behaviorQuestions.append(q18)
behaviorQuestions.append(q19)
behaviorQuestions.append(q20)

# to see the questions in string format
def verifyObjectsCorrect(awarenessQuestionsObjects, behaviorQuestionsObjects):
    for x in range(10):
        print(str(x + 1) + " " + awarenessQuestionsObjects[x].type + " (" + awarenessQuestionsObjects[x].focus + ")" + ": " + awarenessQuestionsObjects[x].question + "\n Suggestion: " + awarenessQuestionsObjects[x].suggestion)
        print()
    for x in range(10):
        print(str((x + 11)) + " " + behaviorQuestionsObjects[x].type + " (" + behaviorQuestionsObjects[x].focus + ")" + ": " + behaviorQuestionsObjects[x].question + "\n Suggestion: " + behaviorQuestionsObjects[x].suggestion)
        print()

# creating the question objects with the pre-made classes
def createQuestionObjects():
    behaviorQuestionsObjects = []
    awarenessQuestionsObjects = []
    for x in range(10):
        if x <= 4:
            awarenessQuestionsObjects.append(AwarenessQuestion(awarenessQuestions[x], "personal", awarenessSuggestions[x]))
            behaviorQuestionsObjects.append(BehaviorQuestion(behaviorQuestions[x], "personal", behaviorSuggestions[x]))

        else:
            awarenessQuestionsObjects.append(AwarenessQuestion(awarenessQuestions[x], "workplace", awarenessSuggestions[x]))
            behaviorQuestionsObjects.append(BehaviorQuestion(behaviorQuestions[x], "workplace", behaviorSuggestions[x]))


    return awarenessQuestionsObjects, behaviorQuestionsObjects

def displaySuggestions(questions):
    counter = 1
    for x in questions:
        print("Suggestion " + str(counter) + ": " + x.suggestion)
        counter += 1

def verifyQuestions():
    awarenessQuestionsObjects, behaviorQuestionsObjects = createQuestionObjects()
    verifyObjectsCorrect(awarenessQuestionsObjects, behaviorQuestionsObjects)

def seeScoreSuggestions():
    print("LOW AREA SCORE SUGGESTIONS (4): ---------------------------------------------------")
    print(personalAwarenessSuggestion)
    print(personalBehaviorSuggestion)
    print(workplaceBehaviorSuggestion)
    print(workplaceAwarenessSuggestion)
    print("-----------------------------------------------------------------------------------")

