import os
RED = "\u001B[31m"
BOLD = "\033[1m"
WHITE = "\u001b[0m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
bg_Red =  "\u001b[41;1m"
bg_White = "\u001b[47;1m"
bg_Black = "\u001b[40;1m"
bg_Cyan = "\u001b[46;1m"
Underline = "\u001b[4m"
def pickWord():
    import random
    words = []
    f = open("Words", "r")
    for w in f:
        words.append(w.rstrip())
    r = random.randint(0, len(words) - 1)
    f.close()
    return words[r].upper()


def createSecretList(word):
    Secret_List = []
    for i in (word):
        Secret_List.append(i)
    return (Secret_List)


def buildHintList(secretList):
    Hint_List = []
    for i in range(len(secretList)):
        Hint_List.append("_")
    return Hint_List


def printHintList(hintList):
    printHintList = ""
    for item in hintList:
        printHintList += " " + item
    return printHintList


def checkLetter(secretList, letter):
    for item in (secretList):
        if (letter) == item:
            return True
    return False


def updateHintList(secretList, hintList, letter):
    for i in range(len(secretList)):
        if secretList[i] == letter:
            hintList[i] = secretList[i]
    return hintList


def isWordGuessed(hintList, secretList):
    if hintList == secretList:
        return True
    else:
        return False


#### Game set up ####
w = pickWord()
SecretList = createSecretList(w)
# print(SecretList)
print("try to guess the word")
HintList = buildHintList(SecretList)
# print (NewHintList)
print ( bg_Cyan + str((printHintList(HintList))))
tries = 0
GlobalLetters = []
while isWordGuessed(HintList, SecretList) == False:
    tries = tries + 1
    UserAnswer = input(WHITE + "what letter do you want to guess? ").upper()
    if (checkLetter(SecretList, UserAnswer)) == True:
        os.system("clear")
        print(GREEN + bg_White + Underline + "congrats" +  WHITE + " that is in the word")
        print(WHITE +  bg_Cyan + BOLD +  printHintList(updateHintList(SecretList, HintList, UserAnswer)))
        print( WHITE +  "Here's all the " +  bg_Red + BOLD  + Underline +   "incorrect"  + bg_Black  + WHITE + " letters you have guessed so far:")
        print (RED + BOLD + str(GlobalLetters))
    else:
        GlobalLetters.append(UserAnswer)
        os.system("clear")
        print(RED + "try again")
        print(WHITE +  bg_Cyan + BOLD + printHintList(HintList))
        print( WHITE +  "Here's all the " +  bg_Red + BOLD  + Underline +   "incorrect"  + bg_Black  + WHITE + " letters you have guessed so far:")
        print (RED + str(GlobalLetters))
print( GREEN + bg_White + "YAY you got the word in " + str(tries) + " tries")

