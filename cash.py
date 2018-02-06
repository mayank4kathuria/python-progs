# Implementing greedy program in Python

from cs50 import get_float
def main():
    """Prints the minimum number of coin required by the dispenser"""

    print("O hai! How much change is owed?");

    while True:
        c = get_float()
        if c >= 0:
            break
        print("Retry: ")

    c = c * 1000
    c = c / 10
    coin = 0


    while True:

        if c  == 0:
            #coin += 1
            break

        if c >= 25:
            coin += c // 25
            c = c % 25

        elif c >= 10:
            coin += c // 10
            c = c % 10

        elif c >= 5:
            coin += c // 5
            c = c % 5

        elif c >= 1:
            coin += c // 1
            c = c % 1

    print(str(int(coin)))


if __name__ == "__main__":
	main()


