import matplotlib.pyplot as plt
import time
import os
import platform
import sys
import copy
import numpy as np

platform = platform.system()

if len(sys.argv) > 1:
    args = sys.argv
    args.pop(0)
    a, b = int(args[0]), int(args[0])
    print("Using board size {0}x{1}.".format(a, b))
else:
    print("Using default board size of 40x40")
    a,b = 40,40

board1 = [0] * a
for i in range(a):
    board1[i] = [0] * b
gen = 0
pop = 0
gens = []
pops = []
print("\nStructure each input like this: x/y.")
print("\nFor example: 10/10 would set (10,10) to be alive.")
print("\nFor multiple inputs, structure it like this: x/y;x/y;x/y")
print("\nREMEMBER: The matrix starts at index 0, which means the tile or cell \n          in the top left would be 0/0")
print("\nYou can also enter \"random/probability of 1\" to get a random board.\n")
inp = input("? ")
if inp.startswith("random"):
    prob1 = float(inp[inp.find("/")+1:len(inp)])
    prob2 = 1 - prob1
    board1 = np.random.choice([1,0], a*b, p=[prob1, prob2]).reshape(a, b)
else:
    inps = inp.split(";")
    for inp in inps:
        if inp == '':
            break;
        inp_split = inp.split("/")
        x = int(inp_split[0])
        y = int(inp_split[1])
        #useless code because I was an idiot and forgot .split() was a thing
        #but I spent too much time thinking about it so I don't want to remove it
        #x = int(inp[:inp.find("/")]) #finds the first /
        #y = int(inp[inp.find("/")+1:inp.find("/",inp.find("/")+1)]) #finds the first / after the first /, which is the second /
        #state = int(inp[inp.find("/",inp.find("/")+1)+1:(inp.find("/",inp.find("/",inp.find("/")+1))+1)+(len(inp)-inp.find("/",inp.find("/")+1)+1)]) #finds the first / after the first / after the first /, or the first / after the second /, or just the third /
        board1[y][x] = 1
        print("(" + str(x) + "," + str(y) + ") is now " + str(1))
iterations = int(input("\nHow many generations would you like to run? "))
for gen in range(1, iterations+1):
    board2 = copy.deepcopy(board1)
    boardstr = ""
    if platform == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    pop = 0
    for y in range(0, a):
        for x in range(0,b):
            if board1[y][x] == 1:
                pop += 1
            if board1[y][x] == 1:
                boardstr += "██"
            else:
                boardstr += "  "
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
    #R-Pentomino: 10/10;11/10;9/11;10/11;10/12
    time.sleep(0.05)

print("\nDone!\n")

plt.plot(gens, pops)
plt.show()
