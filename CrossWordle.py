#This is the final itteration of the Crosswordle game. If code isnt specifically described in this section, it is built the same in q previous itteration and is fully explained in the respective order of creation.
import random

answered = open("Dictionary.py")

ans = answered.read().lower()

answers = ans.splitlines()

answered.close()

a = random.choice(answers)

answer = list(a)

place = 0

#Welcomes the user and explains how to play the game.

print("Welcome to CrossWordle! The 5x5 crossword puzzle below connects 3 random words in \n the blank boxes. Start by trying to guess the first word like a normal game of \n wordle, where capital letters in the hint mean that that letter is in the right \n spot, while a lowercase letter means it is somewhere else in the word. Once you \n solve a word, use the information gained to guess the other words. Good luck! \n \n")


#Selects 3 random words the same was as in Jun8
while place < 1:
    
    rand = [0,1,2,3,4]
    
 
    placehold = 0
    placeholder = 0
    
    while placehold < 1:
        
        b = random.choice(answers)
        answer2 = list(b)
       
        
        rando = random.choice(rand)
        
        
           
        if answer2[0] == answer[rando]:
            
            
            
            placehold += 1
            place += 1
            
            placed = rando
            placedH = rando
            randoH = rando
            randy = rando
            
            
            while placeholder < 1:
                
                c = random.choice(answers)
                answer3 = list(c)
                
                
                if answer3[placed] == answer2[4]:
                
                    
                    placeholder += 1
            
            
            

build = 0
solve = 0
solveH = 0
row2 = []
r2 = []
row3 = []
r3 = []
row4 = []
r4 = []
row5 = []
r5 = []

end = 0

step = 0

#Builds the crossword and the hidden crossword identically to Jun8/Cross8

while build < 1:
    
    row1 = answer
    
    
    while placed > 0:
        row2.append(" ")
        row3.append(" ")
        row4.append(" ")
        row5.append(" ")
        placed -= 1
    build += 1

while solve < 1:
    row2.append(answer2[1])
    row3.append(answer2[2])
    row4.append(answer2[3])
    row5.append(answer2[4])       
        
    while rando < 4:
        
        row2.append(" ")
        row3.append(" ")
        row4.append(" ")
        row5.append(" ")
        rando += 1
            
    solve += 1
    

hide = 0


while hide < 1:
    
    r1 = ['_', '_', '_', '_', '_',]

    
    
    while placedH > 0:
        r2.append(" ")
        r3.append(" ")
        r4.append(" ")
        r5.append(" ")
        placedH -= 1
    hide += 1

while solveH < 1:
    r2.append("_")
    r3.append('_')
    r4.append("_")
    r5.append('_')       
        
    while randoH < 4:
        
        r2.append(" ")
        r3.append(" ")
        r4.append(" ")
        r5.append(" ")
        randoH += 1
            
    solveH += 1
            
            
r5 = r1

row5 = answer3

#Print these rows to see what and where the answers are
#print(row1)
#print(row2)
#print(row3)
#print(row4)
#print(row5)

print(r1)   
print(r2)
print(r3)
print(r4)     
print(r5)

tally2 = []
tally3 = []
 
 

g = 0


#Plays the game very similarily to Jun8, with some key differences for aesthetics.

while g < 9:
    print("\n")
    guess = input("What is your guess?: ")
    guessed = list(guess)   
    
    if guess == "exit":
        quit()
        
    elif len(guessed) == 5:
    
        g += 1
    
        hint = []
        final = []

        for i in range(0,5):
            
            
            
                
            if guessed[i] in answer2 and guessed[i] not in tally2:
                tally2.append(guessed[i])
                
            if guessed[i] in answer3 and guessed[i] not in tally3:
                tally3.append(guessed[i])
                
            if guessed[i] == answer[i]:
            
                correct = guessed[i]
                hint.append(correct.upper())
                final.append(correct)
                
        
            elif guessed[i] in answer:
            
                close = guessed[i]
            
                hint.append(close)
                
            
            else:
            
                hint.append("_")
        
                
        
        #Cleaned up how information is presented. Now, each prompt tells you exactly what it is. Starting with tallys and then the hint, when neccessary.                
        if len(tally2) > 0:
                print("The second word has...")
                print(tally2)
                
        if len(tally3) > 0:
                print("The third word has...")
                print(tally3)    
        
        #Now it prints the hints only when the user has not guessed correctly        
        if answer != final:
            print("The hint for the first word is...")
            print(hint)
                
        elif answer == final:
            print("Correct! Good job!")
            
            print(row1)
            print(r2)
            print(r3)
            print(r4)
            print(r5)
            
            
            #Code runs almost the exact same as Jun8, with some visual stuff cleaned up.
            while g < 12:
                print("\n")
                guess = input("What is your guess?: ")
                guessed = list(guess)   
    
                if guess == "exit":
                    quit()
        
                elif len(guessed) == 5:
    
                    g += 1
    
                    hint = []
                    final = []

                    for i in range(0,5):
        
      
                        if guessed[i] == answer2[i]:
            
                            correct = guessed[i]
                            hint.append(correct.upper())
                            final.append(correct)
                
            
                        elif guessed[i] in answer2:
            
                            close = guessed[i]
                    
                            hint.append(close)
                
            
                        else:
            
                            hint.append("_")
                    
                        if guessed[i] in answer3 and guessed[i] not in tally3:
                            
                            tally3.append(guessed[i])
                    
                            
                    #Uses the "second" 5th row feature seen in Jun8.        
                    if guessed[4] == answer3[randy]:
                        r52 = []
                        solver = 0
                        random2 = randy
                        
                        
                        while randy > 0:
                            r52.append("_")
                            randy -= 1
    

                        while solver < 1:
                            r52.append(guessed[4])      
        
                            while random2 < 4:
        
                                r52.append("_")
                                random2 += 1
            
                            solver += 1
            
                            
                            
                            
                
                    
                    #Presents information neatly and descriptively                
                    if len(tally3) > 0:
                         
                        print("The third word has...")   
                        print(tally3)
                        
                    if answer2 != final:
                        print("The hint for the second word is...") 
                        print(hint)       
                            
                    if answer2 == final:
                        print("Correct! Good job!")
                        print(row1)   
                        print(row2)
                        print(row3)
                        print(row4)     
                        print(r52)
  
                        
                        #Step variable to keep the next while loop from actiavting without having it indented all the way to one side
                        step += 1
                        
            
                    
                    #I finally decided on 9, 12, then 15 guesses for all words in order
                    while g < 15 and step > 0:
                        print("\n")
                        guess = input("What is your guess?: ")
                        guessed = list(guess)   
    
                        if guess == "exit":
                            quit()
        
                        elif len(guessed) == 5:
    
                            g += 1
    
                            hint = []
                            final = []

                            for i in range(0,5):
        
      
                                if guessed[i] == answer3[i]:
            
                                    correct = guessed[i]
                                    hint.append(correct.upper())
                                    final.append(correct)
                
            
                                elif guessed[i] in answer3:
            
                                    close = guessed[i]
            
                                    hint.append(close)
                
            
                                else:
            
                                    hint.append("_")
                
                            if answer3 == final:
                                print("\n Wow! You won CrossWordle! \n \n ")
                                
                                print(row1)
                                print(row2)
                                print(row3)
                                print(row4)
                                print(row5)
                                step = 0
                                exit()
                            else:
                                print("The hint for the third word is...")
                                print(hint)

#Added a faiiling case for when the while loop breaks without victory                                
if g > 8:
    print("\n  You have ran out of guesses! Try again.")
                  