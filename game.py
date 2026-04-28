# game.py  —  Dungeon Explorer starter
# Lesson 1: Classes & Objects
 
 
class Room:
    """A location in the dungeon."""
    
    # Constructor
    def __init__(self, name, description):
        # Attributes
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}   # e.g. {'north': another_room}

    #Methods

    def add_exit(self, direction, room):
        """Connect this room to another in a given direction."""
        self.exits[direction] = room
 
    def describe(self):
        """Print the room name, description, and available exits."""
        print(f"\n=== {self.name} ===")
        print(self.description)
        if self.exits:
            print(f"Exits: {list(self.exits.keys())}")
        else:
            print("There are no obvious exits.")
 
 
class Player:
    """The player character."""
     # Constructor
    def __init__(self, name):
        # Attributes
        self.name = name
        self.health = 100
        self.inventory = []
 
    #Methods
    
    def show_status(self):
        """Print the player's current name and health."""
        print(f"\n{self.name}  |  Health: {self.health}")
 
    def is_alive(self):
        """Return True if the player has health above zero."""
        return self.health > 0
 
 
# ── Set up the world ─────────────────────────────────────────────────

# Instantiation - using a class to create an object (uses the constructor method)
entrance = Room("Dungeon Entrance", "A cold stone corridor. Torches flicker on the walls.")
library = Room("Ancient Library", "Dusty shelves line every wall. The air smells of old paper.")

entrance.add_exit('north', library)
library.add_exit('south', entrance)

# Instantiation - using a class to create an object (uses the constructor method)
player1 = Player("Amy")
 
# ── Run the game ──────────────────────────────────────────────────────
 
entrance.describe()
player1.show_status()
 
# Move north
current_room = entrance.exits['north']
current_room.describe()

