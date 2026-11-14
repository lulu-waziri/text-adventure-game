from cmath import pi
import sys
import time

def slow_print(text,delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print()

class Room:
 def __init__(self,name,description):
    self.name=name
    self.description=description
    self.exits={}
    self.item=[]

 def add_exit(self,direction,room):
    self.exits[direction]=room

def build_world():
   entrance=Room(
         "Cave Entrance",
         "You stand at the mouth of a dark cave.Cold air drifts out from within.",
      )
   tunnel=Room(
      "Narrow tunnel",
      "The passage is tight and damp. water drips somewhere in the darkness",
   )
   chamber=Room(
         "Glittering chamber",
         "A vast chamber open up, walls sparkling with embeded crystals.",
      )
   pit=Room(
         "Bottomless pit",
         "The floor vanishes to the pit that seems to have no bottom",
      )
   treasure_room=Room(
         "Treasure vault",
         "Gold coins and ancient artifacts are piled high in this hidden vault.",
      )
   dead_end=Room(
      "Collapsed passages",
      "Rubble blocks any further path. This is a dead end"
      )
   entrance.add_exit("north",tunnel)
   tunnel.add_exit("south",entrance)
   tunnel.add_exit("north",chamber)
   tunnel.add_exit("east",dead_end)
   chamber.add_exit("south",tunnel)
   chamber.add_exit("west",pit)
   chamber.add_exit("north",treasure_room)
   pit.add_exit("east",chamber)
   dead_end.add_exit("west",tunnel)

   torch="torch"
   key="rusty key"
   tunnel.item.append(torch)
   chamber.item.append(key)

   return entrance,pit,treasure_room

def show_status(room,inventory):
   print("\n"+"="*50)
   print(f"You are in:{room.name}")
   print(room.description)
   if room.item:
      print(f"You see here:{','.join(room.item)}")
   if room.exits:
      slow_print(f"Exits:{','.join(room.exits.keys())}")
   print("="*50)


def print_help():
   print("\nCommands:")
   print("go <direction> -move(north,south,east,west)")
   print("take <item>    -pick up an item")
   print("inventory      -show what you're carrying")
   print("look           -describe the room again")
   print("help           -show this help message")
   print("quit           -exit the game\n")

def main():
   print("=== THE CAVE OF SHADOWS ===")
   print("You've entered a mysterious cave rumored to hold ancient treasure.")
   print("\nExplore carefully. Some paths are safer than others...")
   print_help()

   entrance,pit,treasure_room=build_world()
   current_room=entrance
   inventory=[]
   game_over=False

   while not game_over:
      show_status(current_room,inventory)

      if current_room is pit:
         print("\nYou step forward into the dark... and the floor gives way⬇️!")
         print("You fall into the endless pit.GAME OVER...")
         game_over=True
         break
      if current_room is treasure_room:
         if "rusty key" in inventory:
            print("\nUsing the key, you unlock an ancient chest.")
            print("Inside: a hoard of gold and jewels beyond your wildest dream!")
            print("🎉YOU WIN🎉")
         else:
            print("\nThere's a locked chest, but you have no key.")
            print("You leave empty-handed. Maybe explore more next time.")
         game_over=True
         break

      command = input("\n>").lower().strip()
      part = command.split(maxsplit=1)


      if not part:
         print("Please enter a command.")
         continue

      action = part[0]

      if action == "quit":
         print("Thanks for playing. goodbye!")
         game_over=True

      elif action == "help":
         print_help()

      elif action == "look":
         continue
      
      elif action == "inventory":
         if inventory:
            print(f"You are carrying:{','.join(inventory)}")
         else:
            print("You aren't carrying anything.")

      elif action == "go":
         if len(part)<2:
            print("Go where? Try 'go north'.")
            continue
         direction = part[1]
         if direction in current_room.exits:
            current_room=current_room.exits[direction]
         else:
            print("You can't go that way.")

      elif action == "take":
         if len(part)<2:
            print("Take what?")
            continue
         item = part[1]
         matched= next((i for i in current_room.item if i.lower()==item),None)
         if matched:
            inventory.append(matched)
            current_room.items.remove(matched)
            print(f"You picked up the {matched}.")
         else:
            print("That item isn't here.")

      else:
         print("Unknown command. Type 'help' for a list of commands.") 


if __name__ == "__main__":
   main()
                     
