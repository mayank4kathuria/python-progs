# Implementing Mario less in Python

from cs50 import get_int

def main():
	"""Prints the Mario Pyramid"""
	while True:
		h = get_int()

		if h > 0 or h < 24:
			break

	for x in range(h):
		print(" " * (h - 1 - x),end="")
		print("#" * (x + 2))

if __name__ == "__main__":
	main()
