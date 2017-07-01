import random #import random, enables you to use its modules

guessesTaken = 0 #assigns 0 to guessesTaken variable

print('Hello! What is your name?') #prints out whats inside the ()
myName = input() # assigns input to myName variable

number = random.randint(1, 20) #assigns random intiger between 1(lowest value it can be) and 19(highest value it van be) to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #prints out "well, (the value of myName variable) , I am thinking..."

while guessesTaken < 6: #repeats syntaxes inside the loop until guessesTaken value is lower than 6.
    print('Take a guess.') #prints...
    guess = input() # assigns input to guess variable
    guess = int(guess) #transforms guess variable to an intiger variable

    guessesTaken += 1 # assaigns guessesTaken +1 to guessesTaken variable

    if guess < number: # runs syntaxes inside, in case guess is lower than number
        print('Your guess is too low.') # prints ...

    if guess > number: # runs syntaxes inside, in case guess is higher than number
        print('Your guess is too high.') # prints

    if guess == number: # runs syntaxes inside, in case guess is equal to number
        break #quits the loop, lines after this in the loop wont be "played"

if guess == number: # runs syntaxes inside in case guess equal to number
    guessesTaken = str(guessesTaken) # transforms guessesTaken to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # prints...

if guess != number: # runs syntaxes inside in case guess is not equal to number
    number = str(number) # transforms number to string
    print('Nope. The number I was thinking of was ' + number) # prints...
