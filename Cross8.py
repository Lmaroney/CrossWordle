#This code is not a game to be played, I  wanted a fresh program to test out the crossword aspect of the game before I added it to the main code.

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
            
            #Solves for a random third word in the same fashion as the second word was generated. If the last letter in the second word is the same as a random letter in the 3rd word, then it ends the loop with those words as answers. 
            while placeholder < 1:
                
                c = random.choice(answers)
                answer3 = list(c)
                
                
                if answer3[placed] == answer2[4]:
                
                    
                    placeholder += 1
            
            

#Here is the purpose of the cross test. Most of these are placeholder variables, with the empty lists being the locations of the spaces and           

build = 0
solve = 0
row2 = []

row3 = []

row4 = []

row5 = []


end = 0




while build < 1:
    
    #The first row is always just the first answer
    row1 = answer
    
    
    #Uses the placed value, or where the connection is, and makes as many empty spaces as there is spots before the connection
    while placed > 0:
        row2.append(" ")
        row3.append(" ")
        row4.append(" ")
        row5.append(" ")
        placed -= 1
        
    #Increases the build placeholder to end this loop
    build += 1

#More placeholders for while loops
while solve < 1:
    
    #Appends the correct charecter in the correct spot once the blanks have been added
    row2.append(answer2[1])
    row3.append(answer2[2])
    row4.append(answer2[3])
    row5.append(answer2[4])       
    
    #Once the correct letter is in place, it finishes the grid with more empty spaces   
    while rando < 4:
        
        row2.append(" ")
        row3.append(" ")
        row4.append(" ")
        row5.append(" ")
        rando += 1
            
    solve += 1
            
#The fifth row is always just the 3rd word           
row5 = answer3
print(row1)   
print(row2)
print(row3)
print(row4)     
print(row5)
    
    