import pprint,sys
def G(n):
    j = 0
    dict ={}
    for i in range(2-n,n):
        if i < 0 :
            j += 1
            for c in range(1,j+1):
                if j == 1 :
                    t = ([(i+1,c)])
                elif j == 2 :
                    if c == 1:
                        t = ([(i+1,c), (i,c+1), (i-1,c)])
                    elif c == 2 :
                        t = ([(i+1,c), (i,c-1)])
                else :
                    if c == 1:
                        t = ([(i+1,c), (i,c+1), (i-1,c)])
                    elif c==j :
                        t = ([(i+1,c), (i,c-1)])
                    else :
                        t = ([(i+1,c), (i,c+1), (i-1,c), (i,c-1)])
                dict[(i,c)] = t 
        elif i == 0 :
            j += 1
            for c in range(0,j+1):
                if c == 0 :
                    t = ([(i+1,c), (i,c+1)])
                elif c == j :
                    t = ([(i,c-1)]) 
                else :
                    t = ([(i+1,c), (i,c+1), (i-1,c), (i,c-1)]) 
                dict[(i,c)] = t
        else :
            j -= 1
            for c in range(0,j+1):
                if i == n-1 :
                    t = ([(i-1,c)])
                else :
                    if c == 0 :
                        t = ([(i+1,c), (i,c+1), (i-1,c)])
                    elif c == j :
                        t = ([(i-1,c), (i,c-1)]) 
                    else :
                        t = ([(i+1,c), (i,c+1), (i-1,c), (i,c-1)])  
                dict[(i,c)] = t 
    return(dict)
class Polyominoes:
    def __init__(self, c) :
        self.c = c
    def CountFixedPolyominoes(self,graph, untried, n, p) :
        while len(untried) != 0 :
            u = untried.pop()
            p.append(u)
            if len(p) == n :
                self.c += 1
            else :
                new_neighbors = set()
                for t in graph[u] :
                    p.remove(u)
                    neigh = False
                    for h in p :
                        if t in graph[h]:
                            neigh = True
                            break
                        else :
                            neigh = False
                    p.append(u)
                    isit = False
                    if t in p :
                        isit = True
                    inside = False
                    if t in untried :
                        inside = True
                    if inside == False and isit == False and neigh == False :
                        new_neighbors.add(t)
                new_untried = untried.union(new_neighbors)
                f1.CountFixedPolyominoes(pol, new_untried, number , p)
            p.remove(u)
        return(self.c)                
f1 = Polyominoes(0)
if len(sys.argv) == 3 :
    pol = G(int(sys.argv[2]))
    pprint.pprint(pol)
    number = int(sys.argv[2])
elif len(sys.argv) == 2 :
    pol = G(int(sys.argv[1]))
    number = int(sys.argv[1])
pprint.pprint(f1.CountFixedPolyominoes(pol, {(0,0)}, number, []))