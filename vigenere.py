# Implementing Vigenere Cypher problem in Python

import sys
from cs50 import get_string,get_int


def main():
    if( len(sys.argv) != 2 ):
        print("Error!!")
        sys.exit(1)

    else:
        j = 0
        k = sys.argv[1]

        for i in k:
            if not isalpha1(i):
                print("Error!!")
                sys.exit(1)

        print("plaintext: ",end="")
        s = get_string()
        print("ciphertext: ",end="")

        for i in s:
            #print("Debug: " + str(i))
            if j >= len(k):
                j = 0

            t = 0

            if isupper1(k[j]):
                t = ord(k[j]) % 65
            else:
                t = ord(k[j]) % 97

            if isalpha1(i):
                if isupper1(i):
                # For upper case alpha
                    if ord(i) + t <= 90 :
                        print( chr( ord(i) + t),end="" )
                        j += 1
                    else:
                        print( chr( 65 - 1 +  ( ord(i) + t) % 90 ),end="")
                        j += 1

                    # For lower case alpha
                elif islower1(i):
                    if( ord(i) + t <= 122):
                        print( chr(ord(i) + t) ,end="")
                        j += 1
                    else:
                        print( chr( 97 - 1 +  ( ord(i) + t) % 122 ),end="")
                        j += 1
            else:
                print(i,end="")

        print()

def isalpha1(c):

    j = ord(c)
    if (j >= 65 and j <= 90 ) or ( j >=97 and j <= 122 ):
        return True
    else:
        return False

def isupper1(c):
    j = ord(c)
    if j >=65 and j <= 90:
        return True
    else:
        return False

def islower1(c):
    j = ord(c)
    if j >= 97 and j <= 122:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
