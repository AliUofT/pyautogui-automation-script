# back ground runner.py
from pygui import background_image_finder
from VSC_open_and_create_pro import start_recording, stop_recording ,highlight_lines_based_on_dict ,new_anaconda_terminal, new_WSL_terminal, open_vscode, maximize_vscode, create_project_folder, create_new_file, advancedMoveTo, image_exists 
import pyautogui
from screen_recorder import ScreenRecorder
def load_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file = file.read()
            return file
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None

def convert_code_to_escaped_string(code):
    escaped_string = ""
    prev_space = 0
    for line in code.splitlines():
        if line == "":
            continue

        stripped_line = line.lstrip()
        leading_spaces = len(line) - len(stripped_line)
        stripped_line = stripped_line.rstrip()
        
        if leading_spaces >= prev_space:
            escaped_string += '\n' + stripped_line
        
        elif (prev_space > leading_spaces ):
            # print(f"we will be doing {(prev_space- leading_spaces)//4} back spaces")
            escaped_string += '\n' + ('\b' * ((prev_space- leading_spaces)//4)) + stripped_line

        print("")
        prev_space = leading_spaces
            
    return escaped_string

import os
import time
import shutil

# Define the source directory in WSL-compatible format
source_dir = "/mnt/c/Users/aliah/Videos/UNSORTED_RECORDINGS"
destination_dir = os.getcwd()  # The directory where the script is run in WSL

# Function to get the most recent file in the source directory
def get_most_recent_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        return None
    
    most_recent_file = max(files, key=os.path.getmtime)
    return most_recent_file

# Main function to move the most recent file
def move_most_recent_file():
    # Get the most recent file in the source directory
    recent_file = get_most_recent_file(source_dir)

    if recent_file is None:
        print("No files found in the source directory.")
        return

    print(f"Most recent file detected: {recent_file}")

    # Wait for 5-6 seconds to ensure OBS has finished saving the file
    time.sleep(6)

    # Determine the destination path in the WSL format
    file_name = os.path.basename(recent_file)
    destination_path = os.path.join(destination_dir, file_name)

    # Move the file to the destination directory
    shutil.move(recent_file, destination_path)
    print(f"File moved to: {destination_path}")


import json
import os
def open_json_file(file_path):
    """
    Opens a JSON file and returns its contents as a dictionary.
    
    Parameters:
    - file_path (str): The path to the JSON file.
    
    Returns:
    - dict: The contents of the JSON file as a dictionary.
    
    Raises:
    - FileNotFoundError: If the file does not exist.
    - json.JSONDecodeError: If there is an error decoding the JSON.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            print(f"Successfully loaded JSON file: {file_path}")
            return data

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return {}

    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON file {file_path}: {json_error}")
        return {}

    except Exception as e:
        print(f"An unexpected error occurred while opening {file_path}: {e}")
        return {}

# type in your windows conda env name:
env_name = "ytbot"
# testing if it can see mouse
# while True:
#     print(pyautogui.position())
# print('''
#            ."`".
#        .-./ _=_ \.-.
#       {  (,(oYo),) }}
#       {{ |   "   |} }
#       { { \(---)/  }}
#       {{  }'-=-'{ } }
#       { { }._:_.{  }}
#       {{  } -:- { } }
#       {_{ }`===`{  _}
#      ((((\)     (/))))''')


import time
# first, we wait for caesor to appear
# recorder = ScreenRecorder("test1.avi", fps=30, zoom_factor=1, follow_duration=1)
time.sleep(1)
# start_recording()
highlight_dict = {"Here's a quick overview: we define a depth-first search function that takes a graph and a starting vertex as input. ": ([1], 0.95), 'Then, we initialize a set to keep track of visited vertices and a stack with the starting vertex. ': ([2, 3], 15.384), "Next, we iterate through the stack, popping vertices and marking them as visited if they haven't been visited before. ": ([4, 5, 6, 7], 28.057), 'Finally, we explore the graph by adding unvisited neighbors to the stack.': ([8, 9], 37.366)}
print(highlight_dict)
highlight_lines_based_on_dict(highlight_dict=highlight_dict)
# stop_recording()




# if background_image_finder('monke2.png'):
#     open_vscode()
#     maximize_vscode()
#     params = open_json_file("recent_params.json")
#     time.sleep(2)
#     create_project_folder(str(params["concept"]))
#     time.sleep(2)
#     create_new_file(params["concept"])
#     code_path = params["code"]
#     code = load_from_file(code_path)
#     pyautogui.typewrite(convert_code_to_escaped_string(code), interval = .1)
#     print("DONE")

























# make an evnironment called ytbot in anaconda prompt

# activate conda environment
# pip install pyautogui
# pip install opencv-python
# in keybinds.json, have this:
    # {
    #     "key": "Ctrl+Alt+A",  // Choose your preferred key combination
    #     "command": "workbench.action.terminal.newWithProfile",
    #     "args": {
    #         "profileName": "Anaconda Prompt"
    #     }
    # },
    # {
    #     "key": "Ctrl+Alt+W",  // Choose your preferred key combination
    #     "command": "workbench.action.terminal.newWithProfile",
    #     "args": {
    #         "profileName": "Ubuntu (WSL)"
    #     }
    # }

# in generate.py, after the main method, print this:
# print('''
#            ."`".
#        .-./ _=_ \.-.
#       {  (,(oYo),) }}
#       {{ |   "   |} }
#       { { \(---)/  }}
#       {{  }'-=-'{ } }
#       { { }._:_.{  }}
#       {{  } -:- { } }
#       {_{ }`===`{  _}
#      ((((\)     (/))))''')
