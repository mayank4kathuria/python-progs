# Implmenting Saving the universe Again problem


def main():
    t = int(input())
    l = 0
    while t > l:
        d,p = input().split(" ")
        d = int(d)

        p = p.lower()
        h = len(p)
        #print("p is {}, d is {}".format(p,d))
        k = 0
        while k < h:
            if damage(p) > d:
                p = hack(p)
                k = k + 1
            else:
                break
        if damage(p) > d:
            print("Case #{}: IMPOSSIBLE".format(l + 1))
        else:
            print("Case #{}: {}".format(l + 1,k))
        
        l = l + 1

def damage(p):
    strength = 1
    D = 0
    for x in p:
        if x == 'c':
            strength = 2*strength
        elif x == 's':
            D = D + strength
    #print("damage is: " + str(D))
    return D
    
            
def hack(p):
    g = list(p)
    g = g[::-1]
    #print(g)
    for x in range(len(g) - 1):
        if g[x] == 's' and g[x + 1] == "c":
            g[x] = 'c'
            g[x+1] = 's'
            break
    #print(g[::-1])
    return "".join(g[::-1])

if __name__ == "__main__":
    main()
