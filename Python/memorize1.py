# Slightly more complex program to memorize a password or similar
# Nathaniel Branscum, 4/20/22

from time import sleep

def set():
    return input("What would you like to memorize?  ")

def checkSimilar(x, mem):
    similar = 0
    i = 0

    if len(x) < len(mem):
        print("Input too short\n")
        while i < len(x):
            if x[i] == mem[i]:
                similar += 1
            i += 1
    elif len(x) > len(mem):
        print("Input too long\n")
        while i < len(mem):
            if x[i] == mem[i]:
                similar += 1
            i += 1

    print(str(similar) + " similar characters.")

    return

def main(correct, mem):
    total = 10
    # Simple, inelegant method to clear screen
    # Replace later with method that gets screen size
    print("\n" * 20)
    if correct == -4:
        print("Bruh\n( ಠ ¿ ಠ )")
    if correct == total:
        return("Congratulations!")
    print(str(correct + 1) + " out of " + str(total))
    x = input("Password: ")
    if x == mem:
        print("Correct!")
        sleep(0.6)
        main(correct + 1, mem)
    else:
        print("WRONG! :(")
        checkSimilar(x, mem)
        sleep(0.6)
        main(correct - 1, mem)

def start():
    correct = 0
    mem = set()
    main(correct, mem)


start()