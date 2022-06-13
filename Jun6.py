#Use the random library to simulate random selection
import random

#Uses an online library of common 5 letter words
answers = open("Dictionary.py","r")

#Create a temporary variable to randomly generate a line number in the list of words
a = random.choice(range(1,534))


#Create the first asnwer by reading the line of the randomly generated number, in all lowercase
answer = answers.readlines()[a].lower()


#Printing answer for testing
print(answer)


#Seperate the answer into a list of characters
answered = list(answer)


#Since the strings have \n after all of them, pop that last element out
answered.pop()

#Printing answer for testing
print(answered)

#Number of attempted guesses
g = 0

#Close the file
answers.close()


#6 guessed to get the answer
while g < 6:
    
    
    #User inputs a guess
    guess = input("What is your guess?: ")
    guessed = list(guess)   
    
    
    #Exits the program if the guess is exactly the word "exit"
    if guess == "exit":
        quit()
    
    #Else, if the guess is 5 charecters long...    
    elif len(guessed) == 5:
    
        #Adds a guess
        g += 1
        
        #Creates empty lists for the hint and final
        hint = []
        final = []
        
        #For each charecter in the answer...
        for i in range(len(answered)):
        
            #If a charecter in the guess is in the same spot as the same charecter in the correcter answer, appends a capital charecter in that spot for the hint, appends a normal charecter into the final answer
            if guessed[i] == answered[i]:
            
                correct = guessed[i]
                hint.append(correct.upper())
                final.append(correct)
                
            #If a charecer is in the answer but is not in the right spot, append the charecter as a lowercase into the hint
            elif guessed[i] in answered and guessed[i] not in final:
            
                close = guessed[i]
                hint.append(close)
                
            
            #Else, if the charecter isnt in the answer, appends a blank space
            else:
            
                hint.append("_")
                
                
        #If the final guessed answer is the same as the orriginal answer, the game ends and the user wins        
        if final == answered:
            print("Correct! Good job!")
            quit()
        
            
        #If the final answer is not the same as the original, print the hint (with uppercases for correct placements)    
        print(hint)
    

