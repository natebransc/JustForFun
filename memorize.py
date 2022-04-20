# Simple program to memorize a password
# Nathaniel Branscum, 4/20/22

from time import sleep
correct = 0

def set():
    return input("What would you like to memorize?  ")

def main(correct, mem):
    total = 10
    print("\n" * 20)
    if correct == total:
        print("Congratulations!")
        quit(0)
    print(str(correct + 1) + " out of " + str(total))
    x = input("Password: ")
    if x == mem:
        print("Correct!")
        sleep(0.6)
        main(correct + 1, mem)
    else:
        print("WRONG! :(")
        sleep(0.6)
        main(correct - 1, mem)

def start(correct):
    mem = set()
    main(correct, mem)


start(correct)