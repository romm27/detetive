import pandas as pd
import time as t
import os
import defines
import random
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    t.sleep(0.01)


def display_scii_static(figure_name, typewriter = False):
    with open("art/" + figure_name + ".txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    df = ''.join(lines)
    if typewriter:
        typewriter_print(df, defines.typewriter_scii_speed)
    else:
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


def typewriter_print(text, speed = 0):
    if speed == 0:
        speed = defines.typewriter_speed
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        if defines.jump_spaces and l == ' ':
            continue
        t.sleep(random.random()*10.0/speed)
    print('')
