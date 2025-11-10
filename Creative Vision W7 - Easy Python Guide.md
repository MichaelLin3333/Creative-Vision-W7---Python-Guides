# Beginner Python Project Pack

Below is a list of Python mini-projects.  
Click on any project name to jump directly to its instructions.

## 📎 Project List
1. [Coin Flip / Dice Roller](#1-coin-flip--dice-roller)
2. [Compliment / Joke Generator](#2-compliment--joke-generator)
3. [Number Guessing Game](#3-number-guessing-game)
4. [Story Maker (Mad-Libs)](#4-story-maker-mad-libs)
5. [Password Generator](#5-password-generator)
6. [Math Quiz Game](#6-math-quiz-game)
7. [Virtual Pet (Simple)](#7-virtual-pet-simple)


---

## 1. Coin Flip / Dice Roller
### ✅ What this program does
The computer will randomly pick a result — like flipping a coin (“Heads” or “Tails”) or rolling a dice (1–6).  
This shows how computers can generate random events.

### ✅ Logic behind the program
- The program asks Python to “randomly choose”
- You print the result on the screen

### ✅ New things used
| Function | Meaning |
|----------|---------|
| `import random` | allows Python to generate random numbers |
| `random.choice(list)` | picks one item from a list |
| `random.randint(a,b)` | picks a random number between a and b |

### ✅ Code Example (Coin Flip)
```python
import random

result = random.choice(["Heads", "Tails"])
print("You flipped:", result)
```

### ✅ Code Example (Dice Roller)
```python
import random

roll = random.randint(1, 6)
print("You rolled a:", roll)
```

⭐ Challenge Extension

- Roll two dice and show the total
- Add a rare bonus event: if both dice are 6 → “JACKPOT!”


## 2. Compliment / Joke Generator
### ✅ What this program does

When the program runs, it randomly chooses a funny compliment or joke to show the user.

### ✅ Logic behind the program
- Store a list of funny lines
- Randomly pick one
- Print it

### ✅ New things used
| Concept | Meaning |
|----------|---------|
| Lists | A group of items stored in one variable |

### ✅ Code Example
```python
import random

compliments = [
    "You are amazing!",
    "Great job today!",
    "Your brain is 10/10!"
]

print(random.choice(compliments))
```


⭐ Challenge Extension
- Let the user choose: 1 for compliment, 2 for joke
- Add 20+ jokes and make it a `daily motivation machine`


## 3. Number Guessing Game
### ✅ What this program does

The computer picks a secret number.
You try to guess it.
The program tells you if you're correct.

### ✅ Logic behind the program

- Random number is created
- User inputs a guess
- Program compares numbers using if and else

### ✅ New things used
| Function | Meaning |
|----------|---------|
| `input()` | lets the user type a response |
| `int()` | converts input text into a number |
| if/else | allows the computer to make decisions |

### ✅ Code Example
```python
import random

secret = random.randint(1, 10)
guess = int(input("Guess a number 1-10: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong! The number was", secret)

```

### ⭐ Challenge Extension
- Add 3 chances
- Score system (“+1 point if correct”)
- Difficulty levels (1–10, 1–50, 1–100)


## 4. Story Maker (Mad-Libs)
### ✅ What this program does

It asks the user for words (name, animal, place…)
Then it creates a funny story using their answers.

### ✅ Logic behind the program
- Use input() to collect words
- Store them in variables
- Print a story using those variables

### ✅ Code Example
```python
name = input("Enter a name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")

print(f"{name} took a {animal} on a trip to {place}. It was wild!")
```
(You may also use `+` instead of `f""`)

### ⭐ Challenge Extension
- Add multiple endings depending on choices
- Make a “Horror version”, “Space version”, or “Fairy Tale version”


## 5. Password Generator
### ✅ What this program does

Creates a random password with letters, numbers, and symbols.

### ✅ Logic behind the program
- Store characters in a list
- Randomly pick many characters
- Put them together into a password

### ✅ New things used
| Function | Meaning |
|----------|---------|
| loop `for i in range(x):` | repeats code x times |

### ✅ Code Example
```python
import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
password = ""

for i in range(8):
    password += random.choice(chars)

print("Your password is:", password)
```

### ⭐ Challenge Extension
- Ask user how long the password should be
- Generate 5 passwords at once


## 6. Math Quiz Game
### ✅ What this program does

Asks simple math questions.
User answers.
Program checks if correct and keeps score.

### ✅ Logic behind the program
- Generate random numbers
- Generate a question
- Compare answer

### ✅ Code Example
```python
import random

score = 0
for i in range(5):
    a = random.randint(1,10)
    b = random.randint(1,10)
    answer = int(input(f"What is {a} + {b}? "))

    if answer == a + b:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your score:", score)
```

### ⭐ Challenge Extension
- Add subtraction, multiplication, division
- `Final grade` based on score
- Timer (optional for advanced students)


## 7. Virtual Pet (Simple)
### ✅ What this program does

You can feed, play, or put the pet to sleep.
Pet’s mood changes based on what you do.

### ✅ Logic behind the program
- Use variables to store hunger, happiness, energy
- Change values based on actions

### ✅ Code Example
```python
hunger = 5
energy = 5

print("1 = Feed, 2 = Sleep")
choice = int(input("What do you do? "))

if choice == 1:
    hunger -= 2
    print("Your pet is less hungry!")
elif choice == 2:
    energy += 2
    print("Your pet is rested!")

```

⭐ Challenge Extension
- Add a loop so the game continues
- Add new actions (play, vet, bath)
- Different pets with unique stats