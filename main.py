import engine
import defines
import game
import os

def menu():
  choice = int(engine.create_user_input(""))
  while choice != 1 and choice != 2:
    choice = int(engine.create_user_input("Invalid input. Try again: ", True))
  return choice


def started_game():
  # Your implementation for the started_game function goes here
  pass


engine.settings_prompt()
engine.display_scii_animation("anim_scout", 0.2, 60, True)
print("\nWelcome to Detective Game!\n1. Start\n2. Quit")
print(os.name)

while True:
  game_select = menu()
  engine.clear_screen()

  if game_select == 1:
    running_game = started_game()
    engine.display_scii_animation("anim_demo", 1.2, 5, True)
    break
  else:
    print("Closing application...")
    break