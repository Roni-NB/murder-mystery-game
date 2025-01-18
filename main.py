import random

def jumble_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + "".join(middle) + word[-1]
    return word

def distort_clue(clue):
    words = clue.split()
    distorted = [jumble_word(word) for word in words]
    return " ".join(distorted)

def game_setup():
    # Pools of possible clues
    causes_of_death = ["poison", "stab wound", "drowning", "blunt force trauma"]
    killers = ["his mother", "the butler", "his best friend", "a stranger"]
    locations = ["his house", "the library", "the garden", "an abandoned warehouse"]
    
    # Randomly pick one clue from each category
    ghost_clues = {
        "cause_of_death": random.choice(causes_of_death),
        "killer": random.choice(killers),
        "location": random.choice(locations)
    }
    return ghost_clues

def player_2_guess():
    guess = {
        "cause_of_death": input("How do you think the ghost died? "),
        "killer": input("Who do you think the killer is? "),
        "location": input("Where do you think it happened? ")
    }
    return guess

def play_game():
    print("Welcome to the AI Murder Mystery Game! 🕵️‍♀️👻")
    ghost_clues = game_setup()
    print("\nGhost, give your clues... (shh, Detective can’t see this!)")
    
    distorted_clues = {k: distort_clue(v) for k, v in ghost_clues.items()}
    print("\nDetective, here are your clues:")
    for clue in distorted_clues.values():
        print(f"- {clue}")
    
    guesses = player_2_guess()
    
    score = sum(1 for k in ghost_clues if ghost_clues[k].lower() == guesses[k].lower())
    print(f"\nDetective’s score: {score}/3")
    return score

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()

