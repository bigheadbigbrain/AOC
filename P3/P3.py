import os
os.chdir('C:\\Users\\Bryan\\Py\\AOC19\\P3')
#lets grab the inputs and put them in a list of moves
#moves1 and moves2
with open("line1.txt") as inputFile:
    M1 = inputFile.read().split(",")
with open("line2.txt") as inputFile:
    M2 = inputFile.read().split(",")

#make move to both lines
#have two dicts for each lines current location
line1pos = {"X": 0, "Y":0}
line2pos = {"X": 0, "Y":0}
distance = 0
currentDistance = 0
#make move for both lines
for i in range(len(M1)):
    #line 1
    if M1[i].startswith("U"):
        line1pos["Y"] += int(M1[i][1:])
    elif M1[i].startswith("D"):
        line1pos["Y"] -= int(M1[i][1:])
    elif M1[i].startswith("L"):
        line1pos["X"] -= int(M1[i][1:])
    elif M1[i].startswith("R"):
        line1pos["X"] += int(M1[i][1:])
    #line 2
    if M2[i].startswith("U"):
        line2pos["Y"] += int(M2[i][1:])
    elif M2[i].startswith("D"):
        line2pos["Y"] -= int(M2[i][1:])
    elif M2[i].startswith("L"):
        line2pos["X"] -= int(M2[i][1:])
    elif M2[i].startswith("R"):
        line2pos["X"] += int(M2[i][1:])
    #See if same spot
    print("L1: " + str(line1pos))
    print("L2: " + str(line2pos))
    if line1pos == line2pos:
        print("entered")
        currentDistance = calcDistance(line1pos)
        #store lowest distance
        if(distance == 0 or currentDistance < distance):
            distance = currentDistance
#calc distance
def calcDistance(l1Coords):
    print("in function")
    d = abs(int(l1Coords["X"])) + abs(int(l1Coords["Y"]))
    print("D: " + str(d) )
    return d

print(str(distance))
