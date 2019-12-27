def checkPair(num):
    num = str(num)
    containAdj = False
    
    for i in range(len(num)-1):
        if(num[i]==num[i+1]):
           
            containAdj=True
            
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
