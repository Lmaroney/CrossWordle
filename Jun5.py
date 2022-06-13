
#Used today's wordle as a test answer for the first day of coding
answer = "depth"
#Seperate the answer into a list of characters
answered = list(answer)

#Number of attempted guesses
g = 0

#6 guesses
while g < 6:
    
    
    #Takes your guess and reads it as a list
    guess = input("What is your guess?: ")
    guessed = list(guess)   
    
    #If the guess is 5 charecters long...
    if len(guessed) == 5:
    
    
        #Consider it a guess
        g += 1
        
        #Create empty lists for the final answer and the hint
        hint = []
        final = []
        
        #For each charecter in the answer
        for i in range(len(answered)):
        
            #Check if a charecter in the guess is in the same spot as in answered. If the letter is in the right spot, append a capital to the hint and a lowercase to the final answer
            if guessed[i] == answered[i]:
            
                correct = guessed[i]
                hint.append(correct.upper())
                final.append(correct)
                
            
            #Else, if the letter is in answered but not the right spot, append a lowercase to the hint
            elif guessed[i] in answered:
            
                close = guessed[i]
            
                hint.append(close)
                
            #Else, if the letter isnt in the answer, append a blank space to the hint
            else:
            
                hint.append("X")
        #If the final guess is the same as the original answer complete the game and congradulate the user    
        if final == answered:
            print("Correct! Good job!")
            quit()
            
        #Otherwise, if the guess wasn't correc, print the hint    
        print(hint)


