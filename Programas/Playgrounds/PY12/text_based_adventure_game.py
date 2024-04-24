def intro():
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")
    print("A. Grab a nearby rock and throw it at the orc")
    print("B. Lie down and wait to be mauled")
    print("C. Run")
    opt = input().upper()
    if opt == "A":
        option_rock()
    elif opt == "B":
        print("Welp, that was quick. You died!")
    else:
        option_run()

def option_rock():
    print("The orc is stunned, but regains control. He begins running towards you again.")
    print("A. Run")
    print("B. Throw another rock")
    print("C. Run towards a nearby cave")
    opt = input().upper()
    if opt == "A":
        option_run()
    elif opt == "B":
        print("The rock flew well over the orcs head. You missed. You died!")
    else:
        option_cave()

def option_run():
    print("You run as quickly as possible.")
    print("A. Hide behind boulder")
    print("B. Trapped, so you fight")
    print("C. Run towards an abandoned town")
    opt = input().upper()
    if opt == "A":
        print("You're easily spotted. You died!")
    elif opt == "B":
        print("You're no match for an orc. You died!")
    else:
        option_town()

def option_cave():
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    answ = input()
    if answ in "yY":
        can_win = True
    else:
        can_win = False
    print("What do you do next?")
    print("A. Hide in silence")
    print("B. Fight")
    print("C. Run")
    opt = input().upper()
    if opt == "A":
        print("I think orcs can see very well in the dark, right? You died!")
    elif opt == "B":
        if can_win:
            print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
        else:
            print("You're defenseless. You died!")
    else:
        print("The orc turns around and sees you running.")
        option_run()

def option_town():
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")
    answ = input()
    if answ in "yY":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
    else:
        print("Maybe you should have picked up the flower. You died!")

intro()