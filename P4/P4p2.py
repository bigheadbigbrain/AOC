def checkPair(num):
    num = str(num)
    containAdj = False
    numSet =[]
    #lets split our 6 diggets up
    #i.e 1933255 = numSet[1,9,33,2,55]
    #then we can check if anyone of those have a string length of two and return true
    for i in range(len(num)):
        if i ==0:
            numSet.append(num[i])
        #if equal to previous number
        elif num[i] == num[i-1]:
            numSet[-1]= numSet[-1] + num[i]
        #only other case would be if it was different
        else:
            numSet.append(num[i])
    for i in range(len(numSet)):
        if(len(numSet[i])==2):
            containAdj = True
            break
    return containAdj

    

def checkIncreasing(num):
    num = str(num)
    isIncreasing = True
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            isIncreasing = False
    return isIncreasing
def main():
    poss=0
    for i in range(193651,649729+1):
        if checkPair(i) and checkIncreasing(i):
            poss+=1
            
    print("number of possibilities are " + str(poss))

main()
