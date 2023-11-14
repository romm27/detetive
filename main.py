import engine
import defines

def menu():
  choice = int(engine.create_user_input("", True))
  while choice != 1 and choice != 2:
    choice = int(engine.create_user_input("Invalid input. Try again: ", True))
  return choice


def started_game():
  # Your implementation for the started_game function goes here
  pass


engine.display_scii_static('walt', True)
print("\nWelcome to Detective Game!\n1. Start\n2. Quit")

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