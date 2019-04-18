import sys
import os
from profanity import profanity
import re

def main():
    racial_slurs = ['abbie', 'abe', 'abie', 'abc', 'abcd', 'abid', 'abeed', 'abo', 'abbo', 'annamite', 'arabuh', 'armo', 'aseng', 'arab', 'bamboula', 'beaner', 'bluegum', 'bosche', 'boche', 'bosch', 'boonga', 'boong', 'bunga', 'boonie', 'bootlip', 'brownie', 'chankoro', 'chankoro', 'cheesehead', 'chinaman', 'cholo', 'coon', 'cracker', 'cushi', 'darky', 'dothead', 'fob', 'goy', 'goyim', 'goyum', 'gringo', 'groid', 'guido', 'gypsy', 'hairyback', 'half-breed', 'haole', 'heeb', 'hebe', 'hillbilly', 'honky', 'honkey', 'honkie', 'hymie', 'jap', 'jewboy', 'jigaboo', 'kaffir', 'kaffer', 'kafir', 'kaffre', 'kuffar', 'kalar', 'kanaka', 'mooncricket', 'niglet', 'nignog', 'nig-nog', 'nip', 'oreo', 'paki' , 'raghead', 'russki', 'shylock', 'slant', 'sooty', 'tacohead', 'tar-baby', 'wigger', 'zipperhead','chink', 'nigger', 'kike', 'spic', 'wetback', 'towelhead']
    offbeat_slurs = ['cuck', 'libtard', 'maga' ]
    total_lines = 0
    profanity_lines = 0

    allFiles = getListOfFiles('Multiplayer')
    for filename in allFiles:
        content = [line.rstrip('\n') for line in open(filename)]
        total_lines += 1
        for line in content:
            if profanity.contains_profanity(line):
                profanity_lines += 1
                print(line[25:])
                writeToFile("Profanities.txt", re.sub(r'\W+', ' ', line[25:]).upper())

    print(profanity_lines)

def getListOfFiles(dirName):
    listOfFiles = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFiles:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def writeToFile(fileName, string):
    with open(fileName, 'a') as file:
        file.write(string)

if __name__ == "__main__":
    main()
