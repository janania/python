from random import randint
from time import sleep

print("Welcome to the Dragon Cave!")
name = input("What is your name?: ").strip().title()

print()

def displayIntro():
    print("""Hello {}, You have entered the realm of the Dragons. There are two caves awaiting you. One contains a friendly dragon,who shares her treasure with you. The other cave holds a vicious dragon who will gobble you down upon first sight. Choose Wisely!""".format(name))

    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave would you like to enter (1 or 2)?: ').strip()
    return cave

def checkCave(chosenCave):
    print("You approach the cave...")
    sleep(2)
    print("It is dark and spooky...")
    sleep(2)
    print("A large dragon jumps out infront of you! She open her jaws and...")
    sleep(4)
   

    friendlyCave = randint(1,2)

    if chosenCave == str(friendlyCave):
        print("shares her treasure with you :)")
    else:
        print("devours you in one bite!!!")

playAgain = "yes"
while playAgain == "yes":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print()

    playAgain = input("Would you like to play again (yes or no)?: ").strip().lower()
