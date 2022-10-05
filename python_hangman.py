from random import choice





words = [ "tree", "basket", "chair", "paper", "python", "blizzard", "nightclub", "pizza", "league", "glyph", "Darth Vader", "responsibiility", "Christmas", "basketball" ]
word = choice(words)     # randomly chooses a word from words list
guessed, lives, game_over = [], 6, False   #multi variable assignment

# create a list of underscores to the length of the word
guesses = ["_"] * len(word)

#create a main loop
while not game_over:
    hidden_word = "".join(guesses)
    print("Your guessed letters: {}".format(guessed))
    print( "Word to guess: {}".format(hidden_word) )
    print( "Lives: {}".format(lives) )
    ans = input("Type quit or guess a letter: ").lower()
    
    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
    elif ans in word and ans not in guessed:
        print("You guessed correctly!")
        for i in range(len(word)):
            if word[ i ] == ans:
                guesses[ i ] = ans
    elif ans in guessed:
        print("You already guessed that. Try again")
    else:
        lives = -1
        print("Incorrect, you lost a life")
    if ans not in guessed:
        guessed.append(ans)
    elif lives <= 0:
        print("You lost all your lives! The word was " + word)
        game_over = True
    elif word == "".join(guesses):
        print("Congratulations, you guessed it correctly!")
        game_over = True