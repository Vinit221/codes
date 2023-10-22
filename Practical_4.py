graph = {
    "S":["A","B","C"],
    "A":["S","D"],
    "B":["S","E"],
    "C":["S","F"],
    "D":["A","G"],
    "E":["B","G","F"],
    "F":["C","E"],
    "G":["D","E"],
    
}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m)
        for neigh in graph[m]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
print(bfs(visited,graph,"S"))