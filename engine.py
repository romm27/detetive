import pandas as pd
import time as t
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_scii_static(figure_name):
    with open("art/" + figure_name + ".txt", 'r') as file:
        lines = file.readlines()
    df = ''.join(lines)
    print(df)


def display_scii_animation(animation_name, time, frames, cls=True):
    total_frames = 0
    current_frame = 0
    for path in os.listdir('art/' + animation_name):
        total_frames += 1

    for i in range(0, frames):
        if cls:
            clear_screen()
        display_scii_static(animation_name + "/" + str(current_frame))
        t.sleep(time)  # Assuming you have a function or import for sleep, adjust as needed
        if current_frame + 1 == total_frames:
            current_frame = 0
        else:
            current_frame += 1


def create_user_input(prompt, force_arrow = False):
    if force_arrow:
        temp_prompt = prompt + '\n>'
    else:
        temp_prompt = prompt
    temp = input(temp_prompt)
    temp = temp.lower()
    return temp