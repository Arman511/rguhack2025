from player import Player
class menus:
    def main_actions(action):
        if action == "status":
            input(f"Player health: {player.health} - PRESS ENTER TO CONTINUE")
        elif action == "quit":
            print("Goodbye!")
            sys.exit()
        elif action == "inventory":
            input(player.got_items(), "- PRESS ENTER TO CONTINUE")
        elif action == "look":
            input(current_room.description, "- PRESS ENTER TO CONTINUE")
        elif action == "help":
            print("You can do the following actions: go, look, inventory, quit, help")
        elif action == "suicide":
            print("you punch through the wall and the pressure of the water blasts you and your crew. sadge")
            Player.player_minus_health(9999)
        else:
            print("How are you seeing this?")