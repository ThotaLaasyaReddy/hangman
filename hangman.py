import random
import time

# Initial Steps to invite to the game:
print("\nWelcome to Hangman Game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
print("The game is about to start!\nLet's play Hangman")
time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess =["unanimous", "persuade", "feracious", "similar", "comment", "student", 
                      "encourage", "rhyme", "damage", "plants","abruptly","absurd","affix",
                      "avenue","awkward","azure","beekeeper","blizzard","bookworm","boxcar",
                      "boxful","buffalo","buzzing","buzzwords","croquet","cycle","equip",
                      "fixable","fluffiness","funny","galaxy","gossip","hyphen","icebox",
                      "injury","ivory","jackpot","jaundice","jawbreaker","jigsaw","jogging",
                      "joking","keyhole","kilobyte","kiwifruit","larynx","lengths","lucky",
                      "luxury","matrix","megahertz","microwave","mystify","oxidize","oxygen",
                      "pajama","pixel","pneumonia","puppy","puzzling","quartz","queue","quizzes",
                      "quorum","rickshaw","scratch","strength","syndrome","transcript","voyeurism",
                      "xylophone","yachtsman","youthful","yummy","zigzag","zodiac","zombie"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    hangman()

def play_loop():
    play_game = input("Do you want to play again? y=yes n=no\n").lower()
    while play_game not in ["y", "n"]:
        play_game = input("Invalid input. Do you want to play again? y=yes n=no\n").lower()
    if play_game == "y":
        main()
    else:
        print("Thanks for playing! We expect you back again!")
        exit(0)

def hangman():
    global count, display, already_guessed
    limit = 8

    while True:
        guess = input("This is the Hangman Word: " + display + "\nEnter your guess: ").strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input, Try a letter.\n")
            continue

        if guess in already_guessed:
            print("You already guessed that letter. Try another.\n")
            continue

        already_guessed.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display = display[:index] + guess + display[index + 1:]
            print("Correct guess!\n")
        else:
            count += 1
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
            if count == 1:
                print("   __ \n"
                      "  |   |\n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "__|__\n")
            elif count == 2:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "__|__\n")
            elif count == 3:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |    \n"
                      "  |    \n"
                      "  |    \n"
                      "__|__\n")
            elif count == 4:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   O\n"
                      "  |    \n"
                      "  |    \n"
                      "__|__\n")
            elif count == 5:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   O\n"
                      "  |   |\n"
                      "  |    \n"
                      "__|__\n")
            elif count == 6:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   O\n"
                      "  |  /|\\\n"
                      "  |    \n"
                      "__|__\n")
            elif count == 7:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   O\n"
                      "  |  /|\\\n"
                      "  |  / \n"
                      "__|__\n")
                print("Last guess remaining!\n")
            elif count == 8:
                print("   __ \n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   |\n"
                      "  |   O\n"
                      "  |  /|\\\n"
                      "  |  / \\\n"
                      "__|__\n")
                print("Wrong guess. You are hanged!\n")
                print("The word was:", word)
                play_loop()

        if display == word:
            print("Congrats! You have guessed the word correctly!")
            play_loop()

main()
