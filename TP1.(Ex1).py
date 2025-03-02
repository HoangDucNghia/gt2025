def PathExistence(G, s, t):
    visited = set()
    visited.add(s)
    while True:
        new_visited = set()
        for u in visited:
            if u in G:  
                for v in G[u]:
                    if v not in visited:
                        new_visited.add(v)
        if not new_visited:
            break
        visited.update(new_visited)
    
    if t in visited:
        return "Yes"
    else:
        return "No"

def main():
    G = {1: [2], 2: [1, 5], 3: [6], 4: [6, 7], 5: [2], 6: [3, 4, 7], 7: [4, 6]}
    s = int(input("Enter the first vertex: "))
    t = int(input("Enter the second vertex: "))
    result = PathExistence(G, s, t)
    print(result)

main()
