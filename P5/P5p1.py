import os
os.chdir('C:\\Users\\Bryan\\Py\\AOC19\\AOC\\P5')
with open("input.txt") as inputFile:
    input1 = inputFile.read().split(",")

def toInt():
    global input1
    for i in range(len(input1)):
        input1[i]=int(input1[i])

def retrieveNum(mode,parameter):
    global input1
    #takes a mode and returns the value that the intCode computer is supposed to compute with
    if(mode == 0):
        return input1[parameter]
    elif(mode == 1):
        return parameter

def execute():
    global input1
    i=0
    while i < len(input1):       
        #inst  is our instruction
        #p1,p2,p3 will be our parameters modes
        # 0 means positions(retrieve data from that position)
        # 1 means immediate(that integer)
        #opc will be our op code       
        inst = str(input1[i])
        opc,p1,p2,p3 = 0,0,0,0
        opc = int(inst[-1])
        if(len(inst)>1):
            for j in range(len(inst)):
                if(j==1):
                    opc = int(inst[-2]+inst[-1])
                elif(j==2):
                    p1 = int(inst[-3])
                elif(j==3):
                    p2 = int(inst[-4])
                elif(j==4):
                    p3 = int(inst[-5])    
        #if opcode is 1. This means addition of items i+1 and i+2 and store in location i +3
        if(opc==1):
            input1[input1[i+3]]=retrieveNum(p1,input1[i+1])+retrieveNum(p2,input1[i+2])
            i+=4
        #checkopcode 2 same access and storage
        elif(opc==2):
            input1[input1[i+3]]=retrieveNum(p1,input1[i+1])*retrieveNum(p2,input1[i+2])
            i+=4
        elif(opc==3):
            x = input("Please input the correct part ID")
            input1[input1[i+1]] = int(x)
            i+=2
        elif(opc==4):
            if (p1==1):
                print(input1[i+1])
            else:
                print(input1[input1[i+1]])
            i+=2
        elif(opc==99):
            break

def main():   
    toInt() 
    execute()
    
main()
  
