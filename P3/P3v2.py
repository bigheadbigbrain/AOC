import os
os.chdir('C:\\Users\\bagui\\py\\AOC19\\P3')
#lets grab the inputs and put them in a list of moves
#moves1 and moves2
with open("line1.txt") as inputFile:
    M1 = inputFile.read().split(",")
with open("line2.txt") as inputFile:
    M2 = inputFile.read().split(",")
def plotCoords(cmds):
    xyloc=[(0,0)]
    for i in range(len(cmds)):
        if cmds[i].startswith("U"):
            for j in range(int(cmds[i][1:])):
                xyloc.append((xyloc[-1][0],xyloc[-1][1]+1))    
        elif cmds[i].startswith("D"):
            for j in range(int(cmds[i][1:])):
                xyloc.append((xyloc[-1][0],xyloc[-1][1]-1))
        elif cmds[i].startswith("R"):
            for j in range(int(cmds[i][1:])):
                xyloc.append((xyloc[-1][0]+1,xyloc[-1][1]))
        elif cmds[i].startswith("L"):
            for j in range(int(cmds[i][1:])):
                xyloc.append((xyloc[-1][0]-1,xyloc[-1][1]))
    return xyloc
def findInter(line1, line2):
    return set(line1)&set(line2)
def calcDistance(coords):
    shortest =0
    for i in coords:
        d = abs(i[0])+abs(i[1])
        if shortest == 0 or d < shortest:
            shortest = d
    return shortest
def calcFastestDistance(coords,line1,line2):
    #passing in the intersection(stop) points. 
    #also passing in the command instructions for each move
    shortest = 0
    line1moves =0
    line2moves=0
    
    for i in coords:
        print('passing cords: '+str(i))
        
        line1moves = countMoves(i,line1)
        line2moves = countMoves(i,line2)
        if shortest == 0 or (line1moves+line2moves)<shortest:
            
            shortest = (line1moves+line2moves)
    return shortest

def countMoves(stoppt, cmds):
    xyloc=[(0,0)]
    moves =0
    print("receiving coords " + str(stoppt))
    for i in range(len(cmds)):
        if cmds[i].startswith("U"):
            for j in range(int(cmds[i][1:])):
                if xyloc[-1]==stoppt:
                    break 
                xyloc.append((xyloc[-1][0],xyloc[-1][1]+1))
                moves+=1 
        elif cmds[i].startswith("D"):
            for j in range(int(cmds[i][1:])):
                if xyloc[-1]==stoppt:
                    break 
                xyloc.append((xyloc[-1][0],xyloc[-1][1]-1))
                moves+=1 
        elif cmds[i].startswith("R"):
            for j in range(int(cmds[i][1:])):
                if xyloc[-1]==stoppt:
                    break  
                xyloc.append((xyloc[-1][0]+1,xyloc[-1][1]))
                moves+=1 
        elif cmds[i].startswith("L"):
            for j in range(int(cmds[i][1:])):
                if xyloc[-1]==stoppt:
                    break
                xyloc.append((xyloc[-1][0]-1,xyloc[-1][1]))
                moves+=1 
                
    print("Our stop point was " + str(stoppt)+ "and we stopped at pt " + str(xyloc[-1]))
    return moves
#make graph
l1graph  = plotCoords(M1)
l2graph = plotCoords(M2)
#find matching points
intersections = findInter(l1graph,l2graph)
#find smallest distance
end = calcDistance(intersections)
SD= calcFastestDistance(intersections,M1,M2)
print('The intersection with the least amount of moves required is ' + str(SD))




                