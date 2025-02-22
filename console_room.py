from challenge import console_challenge
from colours import ANSI_BLUE, wrap_colour
from player import Player


def console_room(player: Player):
    print("You enter a room echoing with the sound of beeps and boops, you smell oil and copper")

    print("A robot is sat determinedly at a console like homer the simpson at the nuclear power plant")
    print("HELLO HUMAN, ITS BEEN YEARS SINCE I HAVE SEEN A HUMOID (⸝｡˃ ᵕ ˂ )⸝♡, CAN YOU HELP ME FIX MY LOONIX CONSOLE")
    print("I WILL GIVE YOU A REWARD IF YOU DO :D")
    enter = input("Do you want to help the robot? (y/n) ")
    if enter == "y":
        print("THANK YOU HUMAN, I NEED YOU TO HELP ME WITH THIS MATH PROBLEM (⸝⸝⸝ᵒ̴̶̷ ⌑ ᵒ̴̶̷⸝⸝⸝)")
        print("IF YOU GET IT WRONG I WILL HAVE TO TAKE A PIECE OF YOUR BODY (˶˃ ᵕ ˂˶)")
        answer = input("What is 0 / 0?")
        
        if win:
            input("WONDERFUL!")
        else:
            input("I AM SORRY HUMAN, I MUST TAKE A PIECE OF YOUR FLESH (˶˃ ᵕ ˂˶)")
            player.health -= 1
    else:
        print("OK BYEEE ☃️")

          
    