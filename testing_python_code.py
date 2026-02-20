import random
print ("This is a calculator and a rng game")
while True:
    coq = input ("1. Game 2. Calc 3. Quit : ")
    if coq == "1":
        break
    else:        print ("Invalid input, try again")
    if coq == "2":
        quit()
    elif coq == "3":
        
        x = int(input ("Enter your first number here WHOLE NUMBERS ONLY!!! : "))
        y = input ("Enter one of the following to add '+' to mult '*' to divide '/' to subtract '-' : ")
        z = int(input ("Enter your second number here WHOLE NUMBERS ONLY!!! : "))
        if y == "+":
            result1= x + z
            print(result1)
            continue
        elif y == "-":
            result2= x - z 
            print(result2)
            continue
        elif y == "/":
            result3= x / z 
            print(result3)
            continue
        elif y == "*":
            result4= x * z 
            print(result4)
            continue
        
print ("Welcome to the dice rolling game! You will be rolling a 25 sided die and guessing the number. If you guess the number you win if you dont you lose")
while True:
     rng = input ("Enter '1' to roll the dice or enter '2' to quit : ")
     if rng == "2":
         quit()
     elif rng == "1":
        rn = (random.randint(1,25))
        grn = input ("Enter your guess 1-25 or enter 'Quit' to quit : ")
     if grn == "Quit":
         quit()
     elif int(grn) == rn:
           print ("You Win!")
           continue
     elif int(grn) != rn:
         print ("You Lose! The number was", rn)