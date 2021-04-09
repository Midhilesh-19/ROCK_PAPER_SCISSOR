import random2

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random2.choice(['r', 'p', 's'])

    if user == computer:

        return 'YOU WON!'

    return 'YOU LOST!'

print(play())