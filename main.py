# Import libraries for random number generation and timing effects
import random
import time

# Function to display text with a typewriter effect, one character at a time
def type_slowly(text, delay=0.05):
    """
    Prints text character by character with a delay between each character.
    Creates a slow typewriter effect for better storytelling experience.
    
    Args:
        text (str): The text to display
        delay (float): Time in seconds to pause between each character (default: 0.05 seconds)
    """
    for char in text:
        print(char, end="", flush=True)  # Print one char without newline, flush immediately
        time.sleep(delay)  # Pause before printing next character

print("")

# Function to create visual separation between story sections
def line_break():
    """Prints two blank lines to create spacing between story segments."""
    print("")
    print("")


# ===== COMBAT FUNCTION =====
def combat(enemy_type, enemy_hp, player_str, player_hp, character_name):
    """
    Handles combat between the player and an enemy.
    
    Args:
        enemy_type (str): Type of enemy (bats, goblins, or bull)
        enemy_hp (int): Enemy's starting health points
        player_str (int): Player's strength score (affects damage)
        player_hp (int): Player's current health points
        character_name (str): Player's character name
    
    Returns:
        tuple: (player_hp_after_combat, enemy_defeated) where enemy_defeated is True if enemy dies
    """
    type_slowly("COMBAT START!")
    line_break()
    
    # Combat loop continues until either player or enemy dies
    while True:
        # Calculate player damage based on strength (strength/3 + random 1-5 bonus)
        player_damage = (player_str // 2) + random.randint(1, 5)

        # Display player attack
        type_slowly(f"{character_name} attacks the {enemy_type}!")
        print("")
        type_slowly(f"You deal {player_damage} damage!")
        print("")
        
        # Reduce enemy HP
        enemy_hp -= player_damage
        type_slowly(f"{enemy_type.capitalize()} health: {max(0, enemy_hp)}")
        line_break()
        
        # Check if enemy is defeated
        if enemy_hp <= 0:
            type_slowly(f"You defeated the {enemy_type}!")
            line_break()
            return player_hp, True
        
        # Enemy attacks back
        # Determine damage range based on enemy type
        if "fire elemental" in enemy_type.lower():
            # Mini-boss does more damage: 4-12
            enemy_damage = random.randint(4, 12)
        elif "giant spider" in enemy_type.lower():
            # Final boss does even more damage: 5-15
            enemy_damage = random.randint(5, 15)
        else:
            # Normal enemies do 2-8 damage
            enemy_damage = random.randint(2, 8)
        
        type_slowly(f"The {enemy_type} attacks you!")
        print("")
        type_slowly(f"You take {enemy_damage} damage!")
        print("")
        
        # Reduce player HP
        player_hp -= enemy_damage
        type_slowly(f"{character_name}'s health: {max(0, player_hp)}")
        line_break()
        
        # Check if player is defeated
        if player_hp <= 0:
            type_slowly(f"You have been defeated by the {enemy_type}!")
            line_break()
            return 0, False


# ===== CHARACTER CREATION SECTION =====
# Prompt the player to name their character
type_slowly("What would you like to name your character? ")
print("")
character_name = input()  # Store the player's chosen character name
print("")

time.sleep(1)

# Lambda function to roll for D&D ability scores (sum of three 6-sided dice rolls)
# This simulates the standard D&D method for generating ability scores
random_num = lambda: random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

# Generate and display character's six core ability scores (using D&D 5e attributes)
c_str = random_num()  # Strength: affects combat and physical power
type_slowly(f"{character_name}'s strength: {c_str}", delay=0.03)
print("")

c_dex = random_num()  # Dexterity: affects agility and reflexes
type_slowly(f"{character_name}'s dexterity: {c_dex}", delay=0.03)
print("")

c_cons = random_num()  # Constitution: affects health and endurance
type_slowly(f"{character_name}'s constitution: {c_cons}", delay=0.03)
print("")

c_int = random_num()  # Intelligence: affects reasoning and knowledge
type_slowly(f"{character_name}'s intelligence: {c_int}", delay=0.03)
print("")

c_wis = random_num()  # Wisdom: affects perception and insight
type_slowly(f"{character_name}'s wisdom: {c_wis}", delay=0.03)
print("")

c_char = random_num()  # Charisma: affects persuasion and force of personality
type_slowly(f"{character_name}'s charisma: {c_char}", delay=0.03)
print("")

# Generate character level (sum of four d5 rolls, creating a range of 4-20)
c_lvl = random.randint(1,5) + random.randint(1,5) + random.randint(1,5) + random.randint(1,5)
type_slowly(f"{character_name}'s level: {c_lvl}")
print("")

# Calculate health based on constitution modifier and level
# (More constitution and higher level = more health)
o_c_hp = c_cons + c_lvl*2
n_c_hp = o_c_hp
type_slowly(f"{character_name}'s health: {o_c_hp}")
line_break()


# ===== STORY SETUP SECTION =====
# Establish the game's opening narrative and context
type_slowly("You lost your party on the way to the capital. Your bag was running low on supplies, so you decided to go into the woods to scavenge for food and water")
line_break()

time.sleep(1)
# Introduce the mysterious mushroom that leads to the dungeon
type_slowly("While in the woods you found a mushroom and decided to eat it because you were starving.")
line_break()

time.sleep(1)
# Explain how the player ends up trapped
type_slowly("After eating the mushroom you start feeling strange and something hits you on your head and you black out.")
line_break()

time.sleep(1)
# Describe waking up in the dungeon, trapped in a cocoon
type_slowly("As you wake up you find yourself webbed in a silk cocoon, you start scratching at the cocoon until it finally breaks.")
line_break()

time.sleep(1)
type_slowly("You fall out onto the hard and cold stone floor.")
line_break()

# Set the stage for the dungeon adventure
type_slowly("You are now in a dungeon, the dungeon is a 5x5 box, your goal is to find and kill the creature that attacked you and escape the dungeon")
line_break()
type_slowly("You start in the bottom middle of the dungeon.")
print("")
type_slowly("Type West, East, North, or South to move.")
print("")


# ===== DUNGEON NAVIGATION SECTION =====
# Initialize starting position (row 4, column 2 - bottom middle of 5x5 dungeon)
row, col = 4, 2
key = False  # Track whether player has obtained the key from the final boss
visited_rooms = set()  # Track which rooms have been visited to prevent re-triggering events
beat_game = False  # Track whether the player has completed the game

# ===== ROOM DESCRIPTIONS =====
# Collections of random descriptions for different room types

# Empty/safe rooms - peaceful encounters with no enemies
empty_room_options = []
empty_room_options.append("You find yourself in an empty room with cobwebs all around.")
empty_room_options.append("You find yourself in a dark empty room with the chill of evil all around.")
empty_room_options.append("You find yourself in a cold room and you start shivering.")

# Combat rooms - encounters with hostile creatures
fight_room_options = []
fight_room_options.append("You find Yourself in a room filled with bats.")  
fight_room_options.append("As you open the door you discover goblins that are hiding along the walls.")  
fight_room_options.append("As you enter the room you find a bull that is charging at you.")  

# Healing rooms - places where the player can recover health
heal_room_options = []
heal_room_options.append("You find yourself in a room with a glorious fountain in the middle with a gold liquid in it. You decide to drink from the fountain.")
heal_room_options.append("You find a fountain that looks like the mother of all fountains, the fountain of youth, and you decide to drink from it.")

# ===== SPECIAL ROOM LOCATIONS =====
# Define which grid coordinates contain special encounters/events
room_options = [
    (0,0), (0,1), (0,2), (0,3), (0,4),
    (1,0), (1,1), (1,2), (1,3), (1,4),
    (2,0), (2,1), (2,2), (2,3), (2,4),
    (3,0), (3,1), (3,2), (3,3), (3,4),
    (4,0), (4,1),        (4,3), (4,4),
]

# Randomly select special rooms once so the dungeon layout stays fixed
available_rooms = room_options.copy()

boss_room = random.choice(available_rooms)
available_rooms.remove(boss_room)

exit_room = random.choice(available_rooms)
available_rooms.remove(exit_room)

chest_room1 = random.choice(available_rooms)
available_rooms.remove(chest_room1)

chest_room2 = random.choice(available_rooms)
available_rooms.remove(chest_room2)

chest_room3 = random.choice(available_rooms)
available_rooms.remove(chest_room3)

chest_room4 = random.choice(available_rooms)
available_rooms.remove(chest_room4)

mini_boss_room = random.choice(available_rooms)
available_rooms.remove(mini_boss_room)

num_fight_rooms = min(6, len(available_rooms))
fight_room_locations = set(random.sample(available_rooms, num_fight_rooms))
for room in fight_room_locations:
    available_rooms.remove(room)

num_heal_rooms = min(4, len(available_rooms))
heal_room_locations = set(random.sample(available_rooms, num_heal_rooms))
for room in heal_room_locations:
    available_rooms.remove(room)

empty_room_locations = set(available_rooms)

# Main game loop - continues until player reaches exit or dies
while beat_game != True:
    # Build list of valid directions player can move from current position
    direction_options = []
    if row > 0:  # Can move forward (north) if not at top row
        direction_options.append("North")
    if row < 4:  # Can move backwards (south) if not at bottom row
        direction_options.append("South")
    if col > 0:  # Can move left (west) if not at left column
        direction_options.append("West")
    if col < 4:  # Can move right (east) if not at right column
        direction_options.append("East")
    
    # Check if player is trapped (no valid moves)
    if len(direction_options) == 0:
        type_slowly("No moves left.")
        break
    
    # Display available movement options and prompt for player input
    type_slowly(f"You can go: {', '.join(direction_options)}. Your current room is: {row, col}")
    print("")
    type_slowly("Which way? ")
    print("")
    direction = input().strip().lower()  # Get player input and normalize it
    print("")

    # Initialize new position with current position (will be updated based on input)
    new_row = row
    new_col = col

    # Process player movement input and validate against available options
    if direction == "north" and "North" in direction_options:
        new_row = row - 1  # Move up (decrease row number)
    elif direction == "south":  # Accept both spellings
        if "South" in direction_options:
            new_row = row + 1  # Move down (increase row number)
        else:
            type_slowly("That way is a wall.")
    elif direction == "west" and "West" in direction_options:
        new_col = col - 1  # Move left (decrease column number)
    elif direction == "east" and "East" in direction_options:
        new_col = col + 1  # Move right (increase column number)
    else:
        type_slowly("That is not an option from here.")
        line_break()
        continue  # Skip to next iteration without updating position

    # ===== ROOM ENCOUNTERS =====
    # Create a unique identifier for the current room
    current_room = (new_row, new_col)

    #Check if player has been in a room before
    if current_room in visited_rooms:
        type_slowly("You have already been here before, you find nothing of interest.")
        line_break()

    #Check if current room is the start again
    if current_room == (4, 2) and current_room not in visited_rooms:
        visited_rooms.add(current_room)
        type_slowly("You find yourself back in the room you started in.")
        line_break()
        
    
    if current_room in empty_room_locations and current_room not in visited_rooms:
        visited_rooms.add(current_room)
        type_slowly(random.choice(empty_room_options))
        line_break()
    
    # Check if player entered a combat room
    # Uses weighted random choice (bats: 3, goblins: 5, bull: 2) to vary encounter frequency
    if current_room in fight_room_locations and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        fight_choice = random.choices(fight_room_options, weights=[3, 5, 2], k=1)[0]
        type_slowly(fight_choice)
        line_break()
        
        # ===== DETERMINE ENEMY TYPE AND STATS =====
        # Identify which enemy was selected and set appropriate HP
        if "bats" in fight_choice.lower():
            enemy_type = "bats"
            enemy_hp = 10
        elif "goblins" in fight_choice.lower():
            enemy_type = "goblins"
            enemy_hp = 15
        elif "bull" in fight_choice.lower():
            enemy_type = "bull"
            enemy_hp = 20
        
        # Start combat and update player HP based on combat outcome
        n_c_hp, enemy_defeated = combat(enemy_type, enemy_hp, c_str, n_c_hp, character_name)
        
        # If player was defeated, end the game
        if not enemy_defeated:
            type_slowly("Game Over!")
            break

    # Check if player entered a healing room and display random description
    if current_room in heal_room_locations and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly(random.choice(heal_room_options))
        n_c_hp = o_c_hp  # Restore 20 health from drinking the healing fountain
        print("")
        type_slowly("Your health has been restored!")
        print("")
        type_slowly(f"{character_name}'s new health: {n_c_hp}")
        line_break()

    # Check if player entered a treasure chest room and display message
    if current_room in {chest_room1} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find a treasure chest in the corner of the room. You open it and find a potion of healing.")
        n_c_hp += 5  # Update current health as well
        o_c_hp += 5  # Increase health by 5 for finding a healing potion
        print("")
        type_slowly("Your health has increased by 5.")
        print("")
        type_slowly(f"{character_name}'s new health: {n_c_hp}")
        line_break()
    elif current_room in {chest_room2} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find a giant treasure chest in the middle of the room. You open it and find a giant halbard.")
        c_str += 5  # Increase strength by 5 for finding a weapon
        print("")
        type_slowly("Your strength has increased by 5.")
        print("")
        type_slowly(f"{character_name}'s new strength: {c_str}")
        line_break()
    elif current_room in {chest_room3} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find a small treasure chest in the corner of the room. You open it and find magical boots that increase your dexterity.")
        c_dex += 5  # Increase dexterity by 5 for finding magical boots
        print("")
        type_slowly("Your dexterity has increased by 5.")
        print("")
        type_slowly(f"{character_name}'s new dexterity: {c_dex}")
        line_break()
    elif current_room in {chest_room4} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find a treasure chest in the corner of the room. You open it and find a magical mirror that increases your charisma.")
        c_char += 5  # Increase charisma by 5 for finding a magical mirror
        print("")
        type_slowly("Your charisma has increased by 5.")
        print("")
        type_slowly(f"{character_name}'s new charisma: {c_char}")
        line_break()


    # Check if player entered the mini-boss room and initiate combat
    if current_room in {mini_boss_room} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find yourself in a room with a Fire elemental. The Fire elemental attacks you!")
        line_break()
        enemy_type = "Fire elemental"  # Mini-boss enemy type
        enemy_hp = 25  # Mini-boss has higher HP than regular enemies
        n_c_hp, enemy_defeated = combat(enemy_type, enemy_hp, c_str, n_c_hp, character_name)
        
        # If player was defeated by mini-boss, end the game
        if enemy_defeated:
            type_slowly("You defeated the Fire elemental! You decide to search the room and find a shield that increases your health by 5.")
            n_c_hp += 5  # Increase health by 5 for finding a shield
            o_c_hp += 5  # Update original health as well
            type_slowly(f"{character_name}'s new health: {n_c_hp}")
            line_break()
        else:
            type_slowly("Game Over!")
            break

    # Check if player entered the final boss room and initiate combat
    if current_room in {boss_room} and current_room not in visited_rooms:
        visited_rooms.add(current_room)  # Mark this room as visited
        type_slowly("You find yourself in a room with the Giant spider. The Giant spider attacks you!")
        line_break()
        enemy_type = "Giant spider"  # Final boss enemy type
        enemy_hp = 30  # Final boss has the highest HP
        n_c_hp, enemy_defeated = combat(enemy_type, enemy_hp, c_str, n_c_hp, character_name)
        
        # If player was defeated by final boss, end the game
        if enemy_defeated:
            key = True  # Player defeated final boss and obtained key
            type_slowly("In the corner of the room you find a glowing key that will help you escape the dungeon.")
            line_break()
        else:
            type_slowly("Game Over!")
            break

    #Check if player entered the exit room and has the key to escape
    if current_room in {exit_room}:
        if key:
            type_slowly("You find yourself in a room with a locked door. You use the key you obtained from the Giant spider to unlock the door and escape the dungeon!")
            print("")
            type_slowly("Congratulations! You have escaped the dungeon and completed your adventure!")
            beat_game = True  # Player has completed the game
            break
        else:
            type_slowly("You find yourself in a room with a locked door. You need to defeat the Giant spider to obtain the key to escape.")
            line_break()

    
    # Update current position to new position
    row = new_row
    col = new_col

