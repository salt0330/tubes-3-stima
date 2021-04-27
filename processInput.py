from BoyerMoore import *
from KnuthMorrisPratt import *
from handleUpdateTask import *
from handleMarkDoneTask import *
from handleNewTask import *

def removeNewLine(string):
    newString = ''
    for char in string:
        if (char != '\n'):
            newString = newString + char
    return newString

# Determine what kind of process (add, update, or mark as done)
def processInput(command):
    # Command List
    listTask = []
    listUpdateCommand = []
    listDoneCommand = []
    
    # Load keyword
    addToListTask = False
    addToListUpdateCommand = False
    addToListDoneCommand = False
    with open("KeywordList.txt",'r') as keywordFile:
        for line in keywordFile.readlines():
            # print(removeNewLine(line))
            if (bmMatch(removeNewLine(line),"Task:") != -1):
                addToListTask = True
                continue
            elif (bmMatch(removeNewLine(line),"Task Update:") != -1):
                addToListUpdateCommand = True
                addToListTask = False
                continue
            elif (bmMatch(removeNewLine(line),"Task Done:") != -1):
                addToListDoneCommand = True
                addToListUpdateCommand = False
                continue
            if (addToListTask):
                listTask.append(removeNewLine(line))
            elif (addToListUpdateCommand):
                listUpdateCommand.append(removeNewLine(line))
            elif (addToListDoneCommand):
                listDoneCommand.append(removeNewLine(line))
    
    # Process command
    for update in listUpdateCommand:
        if (kmpMatch(command,update) != -1):
            handleUpdateTask(command)
            return None
    
    for done in listDoneCommand:
        if (kmpMatch(command,done) != -1):
            handleMarkDoneTask(command)
            return None
    
    for task in listTask:
        if (kmpMatch(command,task) != -1):
            return handleNewTask(command,task)
    
    return "Command tidak dikenali!"    # Masuk kesini kalo di for loop task ga diketahuin task apa yg mau ditambahin
                                        # Artinya bisa langsung dikasih tau kalo commmand ga dikenalin