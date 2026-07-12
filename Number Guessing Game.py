import random
def compare(n):
    while n > 0:
        print(f"You have {n} attempts to guess the number")
        user_number = int(input("please enter your guess: "))
        if user_number == number:
            print("CONGRATS !! You guessed the number")
            return
        elif user_number > number:
            print("You guessed it high!")
        else:
            print("You guessed it low!")
        n -= 1
        if n == 0:
            print("OUT OF ATTEMPTS. YOU LOST")
number = random.randint(1, 100)
print("welcome to the game. Guess the number , I thought b/w 1 to 100")
difficulty = input("Select difficulty: easy, hard \n").lower()
if difficulty == "easy":
    compare(10)
elif difficulty == "hard":
   compare(5)