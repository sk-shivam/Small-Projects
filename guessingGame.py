
import random 

def computerguess(lowval,highval,randnum,count=0):
    if highval >= lowval: #to stay within range
        guess = lowval + (highval-lowval)//2
        if guess == randnum:
            return count
        elif guess > randnum:
            count = count+1
            return computerguess(lowval, guess-1,randnum, count)
        else:
            count = count+1
            return computerguess(guess+1, highval, randnum, count)
    else:
        return -1


#Generating the random number
randnum = random.randint(1,100)



count = 0
guess = -99

while (guess!= randnum):

#Decision contruct to check if guess if higher or lower than randnum
    guess = int(input("Enter Your guess between 1 and 100: "))
    if guess<randnum:
        print(randnum)
        print("Higher")
    elif guess>randnum:
        print(randnum)
        print("Lower")
    else:
        print(randnum)
        print("Voila You guessed correct")
        break
    count = count+1
#end of while loop
print("You took "+str(count)+" steps to guess the number")
print("Computer took "+ str(computerguess(0,100,randnum))+" steps!")