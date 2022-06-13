#Use the random library to pick random answers from a library
import random

#Uses an online library of common 5 letter words
answered = open("Dictionary.py")

ans = answered.read().lower()

answers = ans.splitlines()

answered.close()

a = random.choice(answers)

answer = list(a)

place = 0


#Selects 3 words in the same fasion as Jun7, but connects a third word to the last letter in the second word
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
            
            #If the first letter in the second word lines up with a random letter in the first word, it progresses the loop with that answer selected as answer2. If the last letter of answer2 is the same as a random letter in answer3, it remembers answer3 as the last word and ends the loop. 
            while placeholder < 1:
                
                c = random.choice(answers)
                answer3 = list(c)
                
                
                if answer3[placed] == answer2[4]:
                
                    
                    placeholder += 1
            
            
#Builds the crossword like in Cross8, but also builds a hidden "blank box" crossword to present to the user before they solve the words         

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
    

#Hide is pretty much the exact same as build, but instead of appending the correct letter after some spaces, it appends an underscore to represent an empty box in a crossword. It also will fill up the rest of the box with empty spaces after the second word is represented. 
hide = 0


while hide < 1:
    
    #The first row is always 5 spaces
    r1 = ['_', '_', '_', '_', '_',]

    
    
    while placedH > 0:
        r2.append(" ")
        r3.append(" ")
        r4.append(" ")
        r5.append(" ")
        placedH -= 1
    hide += 1


#This is the only difference in the hidden box. The letter is left out and an empty box fills the area that the second word is located at.
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
            

#The hidden fifth row appears the same as the hidden first row, 5 spaces          
r5 = r1

row5 = answer3

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


#Tallys of letters in the other words will be kept, like the oppposite of hangman
tally2 = []
tally3 = []
  
#Number of attempted guesses, increased to 10 in this version
g = 0


while g < 10:
    
    guess = input("What is your guess?: ")
    guessed = list(guess)   
    
    if guess == "exit":
        quit()
        
    elif len(guessed) == 5:
    
        g += 1
    
        hint = []
        final = []

        for i in range(0,5):
            
            
            
            #Appends a letter to the tally for a word if that word has the same letter as your guess for a previous word.    
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
        
                
        
        #If there are letters in the tallys for other words, print them                
        if len(tally2) > 0:
                print(tally2)
                
        if len(tally3) > 0:
                print(tally3)    
                
        #If the guess and answer dont match, print the hint
        if answer != final:
        
            print(hint)
                
        #If they do, move on from this while loop.
        elif answer == final:
            print("Correct! Good job!")
            
            
            #Prints all known information, filling in the spaces of the first word
            print(row1)
            print(r2)
            print(r3)
            print(r4)
            print(r5)
            
            #Now the user has up to 15 guesses for the first 2 words.
            while g < 15:
                
                #Most of this is the exact same as guessing the first word, with some minor changes
                guess = input("What is your guess?: ")
                guessed = list(guess)   
    
                if guess == "exit":
                    quit()
        
                elif len(guessed) == 5:
    
                    g += 1
                    #Since hint and final are reset everytime the while loop runs, I just used the same variable names for ease of replication
                    hint = []
                    final = []

                    for i in range(0,5):
                        
                        #Checks if each letter in the second guess is in the right spot for the second answer. Similar to the first guess, it will append a capital for being in the right spot, and a alowercase for appearing somewhere else in the word.
                        if guessed[i] == answer2[i]:
            
                            correct = guessed[i]
                            hint.append(correct.upper())
                            final.append(correct)
                
            
                        elif guessed[i] in answer2:
            
                            close = guessed[i]
                    
                            hint.append(close)
                
            
                        else:
            
                            hint.append("_")
                        
                        #Still keeps a tally, only now just for the third word.
                        if guessed[i] in answer3 and guessed[i] not in tally3:
                            
                            tally3.append(guessed[i])
                    
                           
                     #I realized that I needed to create a second hidden fifth row for after the user finds the second word. This would show up after guessing correctly, containing only the last letter of the second word in the 5th row. The rest should be blank since the user hasnt guessed it yet.       
                    if guessed[4] == answer3[randy]:
                        r52 = []
                        #More random and placeholder variables
                        solver = 0
                        
                        random2 = randy
                        
                        #Appends underscores to represent boxes until the connection is met
                        while randy > 0:
                            r52.append("_")
                            randy -= 1
    
                        #Then appends just the last letter of the second word into the connecting spot, and fills the rest with more boxes
                        while solver < 1:
                            r52.append(guessed[4])      
        
                            while random2 < 4:
        
                                r52.append("_")
                                random2 += 1
            
                            solver += 1
            
                            
                            
                            
                    #After checking every letter of the second word, it prints the hint and the tally, and checks if your answer is correct. If it is, it moves on to the last step of guessing the third word.
                    print(hint)
                                     
                    if len(tally3) > 0:
                            
                        print(tally3)
                            
                            
                    if answer2 == final:
                        print("Correct! Good job!")
                        print(row1)   
                        print(row2)
                        print(row3)
                        print(row4)     
                        print(r52)
  
                        
                        
                        step += 1
                        
            
                    
                    #No guess limit when I was originally coding the third word. Everything is almost the exact same as above, except that no more tallys need to be kept since we are on the last word.
                    while step > 0:
                        guess = input("What is your guess?: ")
                        guessed = list(guess)   
    
                        if guess == "exit":
                            quit()
        
                        elif len(guessed) == 5:
    
                            g += 1
    
                            hint = []
                            final = []

                            for i in range(0,5):
        
                                #Checks if letters match answer3 instead of answer2, and appends letters to the hint accordingly
                                if guessed[i] == answer3[i]:
            
                                    correct = guessed[i]
                                    hint.append(correct.upper())
                                    final.append(correct)
                
            
                                elif guessed[i] in answer3:
            
                                    close = guessed[i]
            
                                    hint.append(close)
                
            
                                else:
            
                                    hint.append("_")
                                    
                            #If the answer matches the guess, the code ends and the user is congradulated
                            if answer3 == final:
                                print("Correct! Good job!")
                                
                                print(row1)
                                print(row2)
                                print(row3)
                                print(row4)
                                print(row5)
                                step = 0
                                exit()
                            else:
                                print(hint)
                  