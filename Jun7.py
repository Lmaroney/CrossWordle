
#Use the random library to pick random answers from a library
import random
answered = open("Dictionary.py")


#Uses read() and splitlines() instead of readlines()
ans = answered.read().lower()

answers = ans.splitlines()


#This allows 2 random variables (a and b) to be read from random lines in the answer
a = random.choice(answers)

#Still reads the answer as a list, but now there is no \n since splitlines was used. Therefore, no pop() is required.
answer = list(a)



#Placeholder variable to control the creation loop
place = 0

#Prints asnwer for testing
print(answer)


while place < 1:
    
    
    #A list of possible locations to connect the crossword
    rand = [0,1,2,3,4]
    
    #Another placeholder
    placehold = 0
    
    while placehold < 1:
        
        
        #Creates another random second answer
        b = random.choice(answers)
        
        #Reads it as a list
        answer2 = list(b)
       
        #Pick a random location to be the spot the first and second word meet
        rando = random.choice(rand)
        
        
        #If the first letter of the second word is the same as the letter in the randomly selected spot, continue through the code. Otherwise, the code loops until 2 words line up in a randomly selected place.  
        if answer2[0] == answer[rando]:
            
            
            print(rando) 
            
            #Adds 1 to the palceholders to end the while loops
            placehold += 1
            place += 1
            
            #printsanswer for testing
            print(answer2)
            answered.close()
            place2 = rando


    
    
#Everything else is the same as Jun6, just that now the word generated is random

#Number of attempted guesses
g = 0


while g < 6:
    
    guess = input("What is your guess?: ")
    guessed = list(guess)   
    
    if guess == "exit":
        quit()
        
    elif len(guessed) == 5:
    
        g += 1
    
        hint = []
        final = []

        for i in range(0,5):
        
      
            if guessed[i] == answer[i]:
            
                correct = guessed[i]
                hint.append(correct.upper())
                final.append(correct)
                
            
            elif guessed[i] in answer:
            
                close = guessed[i]
            
                hint.append(close)
                
            
            else:
            
                hint.append("_")
                
        if answer == final:
            print("Correct! Good job!")
            
            
            
            quit()
            
        print(hint)
    

