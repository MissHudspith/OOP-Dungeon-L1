# game.py  —  Dungeon Explorer starter
# Lesson 1: Classes & Objects
 
 
class Room:
    """A location in the dungeon."""
 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}   # e.g. {'north': another_room}
 
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
 
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
 
    def show_status(self):
        """Print the player's current name and health."""
        print(f"\n{self.name}  |  Health: {self.health}")
 
    def is_alive(self):
        """Return True if the player has health above zero."""
        return self.health > 0
 
 
# ── Set up the world ─────────────────────────────────────────────────
 
entrance = Room(
    "Dungeon Entrance",
    "A cold stone corridor. Torches flicker on the walls."
)
 
library = Room(
    "Ancient Library",
    "Dusty shelves line every wall. The air smells of old paper."
)
 
entrance.add_exit('north', library)
library.add_exit('south', entrance)
 
player1 = Player("Asha")
 
# ── Run the game ──────────────────────────────────────────────────────
 
entrance.describe()
player1.show_status()
 
# Move north
current_room = entrance.exits['north']
current_room.describe()

