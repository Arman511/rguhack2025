import sys


class menus:
    def main_actions(action, player, current_room):
        if action == "status":
            input(f"Player health: {player.health} - PRESS ENTER TO CONTINUE")
        elif action == "quit":
            print("Goodbye!")
            sys.exit()
        elif action == "inventory":
            items = player.got_items()
            if items:
                print("You have the following items:")
                for item in items:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")
            input("PRESS ENTER TO CONTINUE")
        # elif action == "look":
        #     input(f"{current_room.description} - PRESS ENTER TO CONTINUE")
        #     # TODO do something with depth, romm manager
        elif action == "help" or action == "?":
            input(
                "You can do the following actions: go, status, inventory, quit, help -- PRESS ENTER TO CONTINUE"
            )
        elif action == "suicide":
            print(
                "you punch through the wall and the pressure of the water blasts you and your crew. sadge"
            )
            player.player_minus_health(9999)
        else:
            print("How are you seeing this?")
