from time import sleep
import sys

tree = open("merry_christmas.txt").read().split("\n")

while True:
    for line in tree:
        print(line)
        sleep(0.1)
    sleep(1)
    for line in tree:
        sys.stdout.write("\033[F") # Cursor up one line
        sys.stdout.write("\033[K") # Clear to the end of line
        sys.stdout.flush()
        sleep(0.1)