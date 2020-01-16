from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# map commands to cardinal directions
#
# Main
#

game_started = True

# Make a new player object that is currently in the 'outside' room.
player = Player("Chris", "outside")
print(f"Room: {player.current_room}")
print(f"Description: {room[player.current_room].description}")

# Write a loop that:
#
# * Prints the current room name
while game_started:
    cmd = input(
        """[w] Move North [a] Move West [s] Move South [d] Move East [q] Quit \n Enter Direction: """)

    cmd_list = ['w', 'a', 's', 'd']
    cmd_selected = False

    if cmd in cmd_list and cmd == 'w':
        try:
            cmd_selected = True
            player.current_room = room[player.current_room].n_to.name
        except:
            print("Error: can't continue in that direction")

    elif cmd in cmd_list and cmd == 'a':
        try:
            cmd_selected = True
            player.current_room = room[player.current_room].w_to.name
        except:
            print("Error: can't continue in that direction")

    elif cmd in cmd_list and cmd == 's':
        try:
            cmd_selected = True
            player.current_room = room[player.current_room].s_to.name
        except:
            print("Error: can't continue in that direction")

    elif cmd in cmd_list and cmd == 'd':
        try:
            cmd_selected = True
            player.current_room = room[player.current_room].e_to.name
        except:
            print("Error: can't continue in that direction")

    elif cmd == 'q':
        print("Thanks for playing!")
        game_started = False

    if cmd_selected == True:
        if player.current_room == 'Outside Cave Entrance':
            player.current_room = 'outside'

        elif player.current_room == 'Foyer':
            player.current_room == 'foyer'

        elif player.current_room == 'Grand Overlook':
            player.current_room = 'overlook'

        elif player.current_room == 'Narrow Passage':
            player.current_room = 'narrow'

        elif player.current_room == 'Treasure Chamber':
            player.current_room = 'treasure'

        player.current_room = player.current_room.lower()

        description = room[player.current_room].description
        print(
            f"""\n Current Room: {player.current_room} \n Description: {description}\n""")
        cmd_selected = False

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
