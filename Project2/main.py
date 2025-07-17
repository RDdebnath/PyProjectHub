import random
r = random.randint(1, 100)
guesses = 1
a = -1
while(a != r):
    a = int(input("Guess the number: "))
    if(a > r):
        print("Lower Number Please")
    else:
        print("Higher Number Please")
    guesses +=1

print(f"You have guessed the number {r} correctly in {guesses} attempt.")