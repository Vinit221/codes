import random
OPEN=["S"]

mylist = {
    "S":["A","B","C"],
    "A":["S","D"],
    "B":["S","E"],
    "C":["S","F"],
    "D":["A","G"],
    "E":["B","G","F"],
    "F":["C","E"],
    "G":["D","E"],
    
}

def movegen(node):
    return mylist[node]

def goaltest(node):
    return node=="G"

def ss1():
    while len(OPEN)>0:
        random.shuffle(OPEN)
        N=OPEN.pop()

        if goaltest(N):
            return "FOUND"
        else:
            n=movegen(N)
            for i in n:
                if n not in OPEN:
                    OPEN.append(i)
                    print("OPEN_LIST",OPEN)
    return ("NOT FOUND")
print(ss1())