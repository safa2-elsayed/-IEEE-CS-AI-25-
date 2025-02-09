import random  

secret_number = random.randint(1, 100)  
attempts = 5  

print("Welcome to the Number Guessing Game!")  
print("I have chosen a number between 1 and 100. You have 5 tries to guess it.")  

for i in range(attempts):  
    guess = int(input(f"Attempt {i+1}: Enter your guess: "))  

    if guess == secret_number:  
        print("🎉 Congratulations! You guessed the correct number!")  
        break  
    elif guess < secret_number:  
        print("Too low! Try a higher number.")  
    else:  
        print("Too high! Try a lower number.")  

    if i == attempts - 1:  
        print(f"Game over! The correct number was {secret_number}.")  
