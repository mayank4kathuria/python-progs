# Implementing Caesar's cypher Algorithm in Python

import sys
from cs50 import get_string


def main():

    if len(sys.argv) != 2:
        print("Error!!")
        sys.exit(1)

    else:

        k = int(sys.argv[1])
        print("plaintext: ",end = "")
        s = get_string()
        print("ciphertext: ",end = "")

        for i in s:
            if( ord(i) >= 65 and ord(i) <= 90  ):

                # For upper case alpha
                if( k <= 26):
                    if( ord(i) + k <= 90):
                        print( chr(ord(i) + k),end="" )
                    else:
                        print( chr(65 - 1 +  (ord(i) + k) % 90),end="" )

                else:
                    t = k % 26
                    if ord(i) + t <= 90:
                        print( chr(ord(i) + t),end="" )
                    else:
                        print( chr(65 - 1 +  (ord(i) + t) % 90),end="" )

                    # //printf("%c", s[i] + k % 26 );


            # // For lower case alpha
            elif( ord(i) >= 97 and ord(i) <= 122  ):

                if k <= 26:
                    if( ord(i) + k <= 122):
                        print( chr( ord(i) + k),end="" )
                    else:
                        print( chr( 97 - 1 +  ( ord(i) + k) % 122 ),end="")

                else:
                    t = k % 26
                    if ord(i) + t <= 122 :
                        print( chr( ord(i) + t ),end="")
                    else:
                        print( chr(97 - 1 +  (ord(i) + t) % 122 ),end="" )

                    # //printf("%c", s[i] + k % 26 );

            else:
                print(i, end="")
    print()
    sys.exit(0)

if __name__ == "__main__":
    main()
