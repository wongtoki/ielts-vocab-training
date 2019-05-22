import os
from os import system
import random

def main():
    path = os.getcwd() + "/wordList.txt"
    refinePath = os.getcwd() + "/refine_wordlist.txt"
    voice = "Daniel"
    file = open(path, "r")
    rows = file.read().split('\n')
    file.close()

    if(os.path.exists(refinePath)):
        rf = open(refinePath, "r")
        excludedwords = rf.read().split('\n')
        rf.close()
    else:
        excludedwords = []

    wordList = []
    for r in rows: 
        w = r.split(' ')[0].replace('*','')
        if w not in wordList:
            wordList.append(w)

    answer = ""
    correct = 0
    wrong = 0
    while True:
        word = wordList[random.randrange(0,len(wordList))]
        if word in excludedwords:
            continue

        system("say " + word + " -v " + voice)
        answer = str(raw_input())
        
        if(answer == word):
            print("correct")
            wordList.remove(word)
            correct += 1
            f = open(refinePath, "a+")
            f.write(word + '\n')
            f.close()

        elif answer == "!q":
            print("Correct: " + str(correct))
            print("Wrong: " + str(wrong))
            return  
        else:
            wrong += 1
            print("Wrong! Correct answer: " + word)

        if(len(wordList) == 0):
            print("Correct: " + str(correct))
            print("Wrong: " + str(wrong))
            return

main()
