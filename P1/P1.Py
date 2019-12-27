import os
os.chdir("C:\\Users\\Bryan\\Py\\AOC19\\P1")
#grab nums and store them
with open("input.txt") as inputFile:
    inputNum = inputFile.readlines()
    for i in range(len(inputNum)):
        inputNum[i] = inputNum[i].rstrip('\n')

# calc fuel requirments of each one, then add to total req
# calc is (mass/3)-2
total = 0
for i in range(len(inputNum)):
    currentReq=int((int(inputNum[i])/3))-2
    shipTotal = currentReq
    #calculate for extra fuel because of...fuel
    while currentReq > 0:
        currentReq = int(currentReq/3)-2
        if currentReq > 0:
            shipTotal+=currentReq
    total += shipTotal
print(total)
#adding comment because we are praticing source control


