"""
    A choose-your-own adventure game that allows the user to
    pick the next room or area they will enter.

    Tyler
    5/19/24
"""


# Annotate the variables.
moat_choice: str
fence_choice: str
room_choice: str

# Display an ASCII art watchtower to the user.
print('''
                    o___.-' /
                    |      _\_
                    |___.-'   `
                    |
                    |
            _   _   j   _   _
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
  _   _   _  [_j__j__j__j__]  _   _   _   _
_[_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
  _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
     j  j  j [  j  j  j  j ] j  j  j  j    \|
     ''')

# Display a welcome message to the user.
print("You and your band of travelers see an island in the distance and approach a")
print("watchtower...")

# Insert a line break.
print()

# Obtain the user's choice for the moat choice.
print("As you land on the island, you notice a large fenced moat blocking your path...")
moat_choice = input("...do you turn to the left or right side of the moat? ")

# Display a message to the user advancing the story.
if moat_choice.lower() == "left":
    print()
    print("You notice an opening in the fence...")

    # Obtain the user's choice for the opening in the fence choice.
    fence_choice = input("Do you swim or wait? ")

    # Display a message to the user advancing the story.
    if fence_choice.lower() == "wait":
        print()
        print("Your friend notices a button hidden in the bushes...")
        print("...as she presses the button, a drawbridge lowers.")
        print("Your party crosses the bridge, and notice hostile fish")
        print("jumping out of the water.")
        print()
        print("You open the front door, walk through, and notice a brown door,")
        print("a black door, a grey door, and a spiral staircase.")

        # Obtain the user's choice for the main room.
        room_choice = input("Where do you go? (Type brown, black, gray, or stairs:) ")

        # Display a message to the user saying they won.
        if room_choice.lower() == "black":
            print()
            print("You find an evil wizard sleeping in his bedroom...")
            print("...your rogue takes him out. Your team finds a chest full of")
            print("gold, gemstones, magic scrolls, potions, and treasure maps!")
            print("Congratulations! You won!")

        # Display game over message to the user if they chose 'brown'.
        elif room_choice.lower() == "brown":
            print()
            print("As you open the brown door, a pack of hobgoblins turn around.")
            print("They rush and attack your party.")
            print("Game over!")

        # Display a game over message to the user if they chose 'gray'.
        elif room_choice.lower() == "gray":
            print()
            print("You open the gray door and enter the room. Magically the door slams shut.")
            print("Within seconds, a horrid-smelling gray smoke floods the room and suffocates")
            print("you and your party.")
            print("Game over!")

        # Display a game over message to the user if they chose 'stairs'.    
        elif room_choice.lower() == "stairs":
            print()
            print("You climb the spiral staircase and enter a laboratory.")
            print("The barbarian in your party picks up a vial and swirls its contents.")
            print("Within a second, the room blows up and bursts into flames.")
            print("Game over!")

        # Display a game over message to the user if they chose something else.   
        else:
            print()
            print("Someone heard your team being noisy. A gray-haired wizard looks furious")
            print("and points his staff at your party. Out of the tip of the staff, a stream")
            print("of caustic acid envelops you and your party. You feel a strong burning and")
            print("are unable to move.")
            print("Game over!")
        

    # Display a game over message to the user if they chose 'swim'.
    elif fence_choice.lower() == "swim":
        print()
        print("Your party dives into the water, but when you do, a school of")
        print("flesh-eating trout attack!")
        print("Game over!")

    # Display a game over message to the user if they chose to do something else.
    else:
        print()
        print("You fall into the water. In the moat, a school of flesh-eating")
        print("trout attack you!")
        print("Game over!")

    
# Display a game over message to the user if they chose 'right' or something else.
else:
    print()
    print("Your team did not notice a covered pit fall trap. You all fall in...")
    print("Game over!")
