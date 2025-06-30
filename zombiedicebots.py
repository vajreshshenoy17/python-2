print("\t \t \t NAME: VAJRESH SHENOY\n\t \t \t USN: 1AY24AI034 \n\t \t \t SEC:'M'")
import random

# Dice definition
dice_pool = (
    ['green'] * 6 +
    ['yellow'] * 4 +
    ['red'] * 3
)

dice_faces = {
    'green': ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red': ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun'],
}

def roll_die(color):
    return random.choice(dice_faces[color])

def roll_dice(num, pool):
    return random.sample(pool, min(num, len(pool)))

# Base bot logic
def zombie_turn(bot_name, strategy_func):
    brains = 0
    shotguns = 0
    dice_remaining = list(dice_pool)

    print(f"\n{bot_name}'s turn begins.")

    while True:
        if shotguns >= 3:
            print(f"{bot_name} got 3 shotguns and lost all brains this turn.")
            return 0

        hand = roll_dice(3, dice_remaining)
        dice_remaining = [d for d in dice_remaining if d not in hand]

        print(f"Rolling: {hand}")
        outcomes = [roll_die(color) for color in hand]
        print(f"Results: {outcomes}")

        for i, outcome in enumerate(outcomes):
            if outcome == 'brain':
                brains += 1
            elif outcome == 'shotgun':
                shotguns += 1
            else:  # footsteps
                # Put the die back into pool
                dice_remaining.append(hand[i])

        print(f"Brains: {brains}, Shotguns: {shotguns}")

        if not strategy_func(brains, shotguns):
            print(f"{bot_name} stops with {brains} brains.")
            return brains

# Strategy functions
def cautious_strategy(brains, shotguns):
    return shotguns < 1

def risky_strategy(brains, shotguns):
    return shotguns < 2

def brains_first_strategy(brains, shotguns):
    return brains < 4 and shotguns < 3

# Simulate game
zombie_turn("CautiousBot", cautious_strategy)
zombie_turn("RiskyBot", risky_strategy)
zombie_turn("BrainsFirstBot", brains_first_strategy)
