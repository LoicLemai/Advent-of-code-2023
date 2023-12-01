import time
word_to_digit = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'r': 'r'
    }
word_to_detect = {
        'one': 'one', 'two': 'two', 'thr': 'three', 'fou': 'four', 'fiv': 'five',
        'six': 'six', 'sev': 'seven', 'eig': 'eight', 'nin': 'nine', 'r': 'r'
    }
with open('C:/Users/loiic/Desktop/code/advt/1/input.txt', 'r') as input:
    finalNumber = 0
    for row in input :
        currentString = ""
        lastDigit = ""
        first = False
        for i in range(len(row) - 2) :
            if row[i].isdigit() and first == False :
                currentString += row[i]
                first = True
            elif row[i].isdigit() and first == True:
                lastDigit = row[i]
            if row[i:i+3] in word_to_detect and first == False:
                stringLen = len(word_to_detect.get(row[i:i+3]))
                stringContent = word_to_detect.get(row[i:i+3])
                if(i+stringLen <= len(row)):
                    if(row[i:i+stringLen] == stringContent):
                        currentString += word_to_digit.get(stringContent)
                        first = True
            elif row[i:i+3] in word_to_detect and first == True:
                stringLen = len(word_to_detect.get(row[i:i+3]))
                stringContent = word_to_detect.get(row[i:i+3])
                if(i+stringLen <= len(row)):
                    if(row[i:i+stringLen] == stringContent):
                        lastDigit = word_to_digit.get(stringContent)

        if row[len(row)-2].isdigit():
            lastDigit = row[len(row)-2]
        if row[len(row)-1].isdigit():
            lastDigit = row[len(row)-1]
        
        if len(currentString) + len(lastDigit) != 2 :
            if len(lastDigit) == 0:
                currentString = currentString + currentString
            else:
                currentString = lastDigit + lastDigit
        else :
            currentString += lastDigit

        
        finalNumber += int(currentString)
        
        
print(finalNumber)

temps_fin = time.time()
duree_execution = temps_fin - temps_debut
print(duree_execution)