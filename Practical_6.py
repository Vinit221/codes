map_list = {
    'Mumbai': [('Pune', 750), ('Delhi', 1500), ('Goa', 1300)],
    'Goa': [('Mumbai', 1200)],
    'Delhi': [('Mumbai', 1200), ('Guwahati', 100), ('Pune', 750)],
    'Chennai': [('Pune', 750)],
    'Kolkata': [('Guwahati', 100), ('Pune', 750)],
    'Pune': [('Mumbai', 1200), ('Kolkata', 0), ('Chennai', 1600), ('Delhi', 1500)],
    'Guwahati': [('Delhi', 1500), ('Kolkata', 0)]
}

OPEN = [[("Mumbai",1200), None]]
CLOSED = []

def movegen(node):
    return map_list[node]

def goaltest(node):
    return node == "Kolkata"

final = []

def reconstructpath(path):
    if path is None:
        return ""
    else:
        final.append(path[0][0])
        reconstructpath(path[1])
    return final

def sort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if ((a[j][0][1]),a[j+1][0][1]):
                (a[j],a[j+1])=(a[j+1],a[j])
    return a

def best():
    while len(OPEN) > 0:
        print("OPEN List", OPEN)

        x = sort(OPEN)
        seen = x.pop(0)
        N = seen[0][0]
        CLOSED.append(N)
        print("Closed List Contains", CLOSED)
        print("Node picked", N)

        if goaltest(N):
            print(reconstructpath(seen)[::-1])
            return "FOUND"
        else:
            neigh = movegen(N)
            for i in neigh:
                if i[0] not in CLOSED and i not in OPEN:
                    new = [i, seen]
                    OPEN.append(new)
    return "NOT FOUND"

best()
