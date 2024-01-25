#Week 3 | Project Milestone - Adventure Game
"""
Author: Martina Toebe

Purpose: Write a program using decisions to accomplish a meaningful task.

"""
print("\nHello Adventure Gamer!\n\nIn this challenge from professor Hillyard you...a little elf known for your pancake-cooking skills, find yourself in a wild forest with dangerous animals and giant sequoias. Your best friend, a magical horse who loves your pancakes, accompanies you. You are equipped with a FRYING PAN, a FLAMING BOW AND ARROW, and a PANCAKE SPATULA that can transform into a sword.\n")

# Level 1
print("\nYou notice a rustling in the bushes. Do you want to INVESTIGATE or IGNORE it?\n")
adventure_gamer = input().lower()

if adventure_gamer == "investigate":
    print("\nYou cautiously approach the bushes and discover a magical portal. Do you want to ENTER the portal or STAY in the forest?\n")
    adventure_gamer = input().lower()

    if adventure_gamer == "enter":
        print("\nYou find yourself in a mystical realm with floating islands. A dragon approaches. Do you want to FLY on your magical horse or SHOOT the dragon with your flaming bow and arrow?\n")
        adventure_gamer = input().lower()

        if adventure_gamer == "fly":
            print("\nYou and your magical horse soar through the skies, avoiding the dragon. You discover a hidden treasure chest. Do you want to OPEN it or LEAVE it?\n")
            adventure_gamer = input().lower()

            if adventure_gamer == "open":
                print("\nCongratulations! You find a rare artifact that enhances your pancake-cooking skills. You and your magical horse return to the forest.\n")
            elif adventure_gamer == "leave":
                print("\nYou decide to leave the treasure chest undisturbed and continue exploring the mystical realm with your magical horse.\n")
            else:
                print("\nInvalid choice. Your indecision makes the dragon attack, and you barely escape with your life.\n")
        elif adventure_gamer == "shoot":
            print("\nYour flaming arrow pierces the dragon's scales, angering it. Do you want to ATTACK with your pancake spatula sword or RUN away?\n")
            adventure_gamer = input().lower()

            if adventure_gamer == "attack":
                print("\nWith a mighty swing of your pancake spatula sword, you defeat the dragon. You and your magical horse celebrate the victory.\n")
            elif adventure_gamer == "run":
                print("\nYou attempt to run, but the dragon catches you. Your magical horse intervenes and sacrifices itself to save you.\n")
            else:
                print("\nInvalid choice. The dragon breathes fire, and you barely escape with your life.\n")
        else:
            print("\nInvalid choice. The dragon attacks while you hesitate, and you barely escape with your life.\n")
    elif adventure_gamer == "stay":
        print("\nYou choose to stay in the forest. Suddenly, a pack of wolves approaches. Do you want to FIGHT them with your pancake spatula sword or ESCAPE?\n")
        adventure_gamer = input().lower()

        if adventure_gamer == "fight":
            print("\nYour pancake spatula sword proves surprisingly effective against the wolves. You and your magical horse continue your journey.\n")
        elif adventure_gamer == "escape":
            print("\nYou and your magical horse manage to escape from the pack of wolves, but not without a few scratches.\n")
        else:
            print("\nInvalid choice. The wolves overwhelm you, and you barely escape with your life.\n")
    else:
        print("\nInvalid choice. You stand still, and the magical portal disappears.\n")
elif adventure_gamer == "ignore":
    print("\nYou choose to ignore the rustling in the bushes and continue your journey. Suddenly, you encounter a mystical creature. Do you want to GREET it or ATTACK?\n")
    adventure_gamer = input().lower()

    if adventure_gamer == "greet":
        print("\nThe mystical creature turns out to be friendly and grants you a magical blessing. You and your magical horse feel invigorated.\n")
    elif adventure_gamer == "attack":
        print("\nYou attack the mystical creature, but it retaliates with powerful magic. Do you want to DEFEND with your frying pan or RETREAT?\n")
        adventure_gamer = input().lower()

        if adventure_gamer == "defend":
            print("\nYour magical frying pan absorbs the creature's magic, and you emerge victorious. You and your magical horse continue your journey.\n")
        elif adventure_gamer == "retreat":
            print("\nYou retreat from the battle, but the mystical creature curses you. Your magical horse becomes temporarily weaker.\n")
        else:
            print("\nInvalid choice. The mystical creature overwhelms you with magic, and you barely escape with your life.\n")
    else:
        print("\nInvalid choice. The mystical creature vanishes, leaving you with a sense of unease.\n")
else:
    print("\nInvalid choice. Your indecision attracts the attention of a giant spider, and you barely escape with your life.\n")

#End
