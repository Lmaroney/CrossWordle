#Use the random library to pick random answers from a library
import random

#Uses an online library of common 5 letter words
answered = open("Dictionary.py")


#This test was to find out how to generate multiple random words from the file. Oriignally, I had trouble with readlines(), but this was solved by switching to read() and then splitlines(), as seen below
ans = answered.read().lower()

answers = ans.splitlines()

answered.close()

a = random.choice(answers)

answer = list(a)
place = 0

print(answer)

while place < 1:
    
    rand = [0,1,2,3,4]
    
 
    placehold = 0
    
    while placehold < 1:
        
        b = random.choice(answers)
        answer2 = list(b)
       
        
        rando = random.choice(rand)
        
        
           
        if answer2[0] == answer[rando]:
            
            
            print(rando) 
            placehold += 1
            place += 1
            print(answer2)
            

   
     


