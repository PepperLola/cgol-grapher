import matplotlib.pyplot as plt
import time
import os
import sys
import copy
import numpy as np

args = sys.argv

if len(args) > 1:
    a,b = int(args[1]),int(args[1])
else:
    a,b = 40,40
board1 = [0] * a
for i in range(a):
    board1[i] = [0] * b
gen = 0
pop = 0
gens = []
pops = []
print("\nStructure each input like this: x/y/state.")
print("\nFor example: 10/10/1 would set (10,10) to be alive.")
print("\nFor multiple inputs, structure it like this: x/y/s;x/y/s;x/y/s")
print("\nREMEMBER: The matrix starts at index 0, which means the tile or cell \n          in the top left would be 0/0")
print("\nYou can also enter \"random/probability of 1/probability of 0\" to get a random board.\n")
input = raw_input("? ")
inputs = input.split(";")
for input in inputs:
    if input.startswith("random"):
        chance1 = float(input[input.find("/")+1:input.find("/",input.find("/")+1)])
        chance2 = float(input[input.find("/",input.find("/")+1)+1:(input.find("/",input.find("/",input.find("/")+1))+1)+(len(input)-input.find("/",input.find("/")+1)+1)])
        board1 = np.random.choice([1,0], a*b, p=[chance1, chance2]).reshape(a, b)
    else:
        x = int(input[:input.find("/")]) #finds the first /
        y = int(input[input.find("/")+1:input.find("/",input.find("/")+1)]) #finds the first / after the first /, which is the second /
        state = int(input[input.find("/",input.find("/")+1)+1:(input.find("/",input.find("/",input.find("/")+1))+1)+(len(input)-input.find("/",input.find("/")+1)+1)]) #finds the first / after the first / after the first /, or the first / after the second /, or just the third /
        if state != 0 and state != 1:
            print("Invalid state! The state has to be 0 or 1, not " + str(state))
            break
        board1[y][x] = state
        print("(" + str(x) + "," + str(y) + ") is now " + str(state))
iterations = int(raw_input("\nHow many generations would you like to do? "))
for gen in range(1, iterations+1):
    board2 = copy.deepcopy(board1)
    boardstr = ""
    os.system('clear')
    pop = 0
    for y in range(0, a):
        for x in range(0,b):
            if board1[y][x] == 1:
                pop += 1
            if board1[y][x] == 1:
                boardstr += "O"
            else:
                boardstr += "-"
        boardstr += "\n"
    print(boardstr)
    print("GEN: " + str(gen))
    print("POP: " + str(pop))
    gens.append(gen)
    pops.append(pop)
    for y in range(0, a):
        for x in range(0,b):
            total = int(board1[(y-1) % a][(x-1) % b] + board1[(y-1) % a][x % b] + board1[(y-1) % a][(x+1) % b] +
                        board1[y % a][(x-1) % b] + board1[y % a][(x+1) % b] +
                        board1[(y+1) % a][(x-1) % b] + board1[(y+1) % a][x % b] + board1[(y+1) % a][(x+1) % b])
            if board1[y][x] == 1:
                if (total < 2) or (total > 3):
                    board2[y][x] = 0
            else:
                if total == 3:
                    board2[y][x] = 1
            #print(str(b*(y)+x) + " : " + str(total) + " : " + str(board1[y][x]) + " : " + str(board2[y][x]))
            #time.sleep(0.1)
    board1 = copy.deepcopy(board2)
    #print(board1)
    #R-Pentomino: 10/10/1;11/10/1;9/11/1;10/11/1;10/12/1
    time.sleep(0.05)

print("\nDone!\n")

plt.plot(gens, pops)
plt.show()
