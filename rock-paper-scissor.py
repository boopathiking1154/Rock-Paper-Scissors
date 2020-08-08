# Write your code here
import random
# open rating.txt file and read the name and rating into a dictionary
fil = open('rating.txt', 'r')
rating_dict = {}

for line in fil:
    a = line.split()
    rating_dict[a[0]] = int(a[1])

# get user name and set starting point of rating
name = input("Enter your name:")
print('Hello', name)
if name in rating_dict:
    rating = rating_dict[name]
else:
    rating = 0

# get playable options from user
play_option = input()
default_option = ['!exit', '!rating']
if play_option == '':
    play_option = ['rock', 'paper', 'scissors']
else:
    play_option = play_option.split(",")

print("Okay, let's start")

# game begins
while True:
    user_in = input()

    option = random.choice(play_option)
    if user_in not in play_option + default_option:
        print("Invalid input")
        continue
    if user_in == '!exit':
        print("Bye!")
        break
    elif user_in == '!rating':
        print(rating)
        continue
    else:
        ind = play_option.index(user_in)

        ord_option = play_option[(ind + 1):] + play_option[:ind]
        split = len(ord_option) // 2
        lose_option = ord_option[:split]
        win_option = ord_option[split:]
        if option in lose_option:
            print("Sorry, but computer chose {}".format(option))
        elif option == user_in:
            rating += 50
            print("There is a draw ({})".format(user_in))
        elif option in win_option:
            rating += 100
            print("Well done. Computer chose {} and failed".format(option))
