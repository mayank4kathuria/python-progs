# Implementing Trouble Sort problem

 #TroubleSort(L): // L is a 0-indexed list of integers
  #  let done := false
   # while not done:
    #  done = true
     # for i := 0; i < len(L)-2; i++:
      #  if L[i] > L[i+2]:
       #   done = false
        #  reverse the sublist from L[i] to L[i+2], inclusive

def main():
    t = int(input())
    h = 0
    while t > h:
        n = int(input())
        v = input()
        v = v.split(" ")
        v = [int(x) for x in v]
        done = False
        while not done:
            done = True
            for i in range(len(v) - 2):
                if v[i] > v[i + 2]:
                    v[i],v[i+2] = v[i+2],v[i]
                    done = False

        if v == sorted(v):
            print("Case #{}: {}".format(h + 1,"OK"))
        else:
            for i in range(len(v) - 1):
                if v[i] > v[i+1]:
                    print("Case #{}: {}".format(h + 1,i))
                    break

        h = h + 1


if __name__ == "__main__":
    main()
