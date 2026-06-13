import random 

number=random.randint(1, 100)

attempt=0

 print("wlecome to guessing game!")
while True:

 guess=int(input("guess number from 1 to 100:"))
 attempt+=1
 
 print(guess)


 if guess==number :
    print("congraulations,you have won!")
    print("attempts",attempt)
 
    break
 
 elif guess > number:
    print("too high")
 else:
    print("too low")
