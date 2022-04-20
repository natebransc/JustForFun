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

def gander(mem):
    print("Take a gander: " + mem)
    sleep(0.6)
    i = 10
    while i != 0:
        print(i)
        sleep(0.25)
        i -= 1
    print("\n" * 20)

def main(correct, streak, mem):
    total = 10
    print(streak)
    if streak <= -2:
        print("Bruh\n( ಠ ¿ ಠ )")
        gander(mem)
    if correct == total:
        return("Congratulations!")
    print(str(correct + 1) + " out of " + str(total))
    x = input("Password: ")
    if x == mem:
        print("Correct!")
        sleep(0.6)
        main(correct + 1, streak + 1, mem)
    else:
        if streak <= 0:
            streak -= 1
        elif streak > 0:
            streak = 0
        print("WRONG! :(")
        checkSimilar(x, mem)
        sleep(0.6)
        main(correct - 1, streak, mem)

def start():
    correct = 0
    streak = 0
    mem = set()
    gander(mem)
    main(correct, streak, mem)


start()