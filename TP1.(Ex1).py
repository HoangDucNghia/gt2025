def PathExistence(G,s,t):
    u=[]
    u.append(s)
    a=len(G)
    for i in range(a):
        b=len(G[i])
        for j in range(b):
            c=len(u)
            for h in range(c):
                if G[i][j]==u[h] | G[i][j+1]==u[h]:
                   u+=G[i][j+1]
    for i in u:
        if(t==i):
            return True
        else:
            return False

def main():
    G=[[1,2],[2,5],[3,6],[6,4],[6,7],[4,7]]
    s=int(input("Enter the first vertex"))
    t=int(input("Enter the second vertex"))
    result=PathExistence(G,s,t)
    print(result)
main()