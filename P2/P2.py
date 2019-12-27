input1 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
#input1 = [2,4,4,5,99,0]
def memReset():
  global input1
  input1 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]

def execute():
  global input1
  for i in range(0,len(input1),4):
    #if opcode is 1. This means addition of items i+1 and i+2 and store in location i +3
    if(input1[i]==1):
      input1[input1[i+3]]=input1[input1[i+1]]+input1[input1[i+2]]
    #checkopcode 2 same access and storage
    elif(input1[i]==2):
      input1[input1[i+3]]=input1[input1[i+1]]*input1[input1[i+2]]
    elif(input1[i]==99):
      break
  return input1[0]
  

  #main loop will be nouns, inner will loop through all verbs
  #then keep iterating over nouns
  #make sure to reset mem for each test
for i in range(99):
  for j in range(99):
    memReset()
    input1[1] = i
    input1[2] = j
    #print("Noun = " + str(i) + "Verb =  " + str(j))
    #print(input1)
    answer = execute()
    if (answer == 19690720):
      print("Corret Answer: Noun = " + str(i) + "Verb =  " + str(j))
      print("advent of code answer is : " + str(100 * i + j))
    