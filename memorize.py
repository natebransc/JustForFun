# Simple program to memorize a password or similar
# Nathaniel Branscum, 4/20/22

from time import sleep

def set():
    return input("What would you like to memorize?  ")

def main(correct, mem):
    total = 10
    # Simple, inelegant method to clear screen
    # Replace later with method that gets screen size
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

def start():
    correct = 0
    mem = set()
    main(correct, mem)


start()