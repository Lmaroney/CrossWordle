# CrossWordle
A python program to play a combination of common word games. The user plays 3 games of wordle combined in a 5x5 crossword.


First, the user is presented with instructions on how to play the game. Specifically, " Welcome to CrossWordle! The 5x5 crossword puzzle below connects 3 random 5 letter words in the blank boxes. Start by trying to guess the first word like a normal game of wordle, where capital letters in the hint mean that that letter is in the right spot, while a lowercase letter means it is somewhere else in the word. Once you solve a word, use the information gained to guess the other words. Good luck! ." 

Then, the user tries to guess the first word. Initial, I considered only allowing recognized words to be accepted as guesses, but this did not prove to work as intended. Since my list of about 500 of the most common words was not an exhaustive list of all the 5 letter words, many plausible guesses would get denied. I decided that I would rather the user be able to "waste" guesses on fake words with no chance of success instead of deny them when trying a perfectly normal guess.

After guessing, the program will give you hints about the answer. If a letter in your word is in the same place as the same letter in the answer, it will represent that with a capital letter in the hint. If it is somewhere else in the answer it will be lowercase. If it is not in the word, it will leave a blank space. 

Along with the hint about the word you are guessing, the program also remembers letters that appear in the other answers. It keeps these in a tally which is presented to you after a guess on any previous word.

Whenever a word is guessed correctly, it is filled into the crossword puzzle. 

The program ends if the user doesn't guess the answers in time, or gets all of them correctly, or types the command "exit"
