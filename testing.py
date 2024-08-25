# back ground runner.py
from pygui import background_image_finder
from VSC_open_and_create_pro import new_anaconda_terminal, new_WSL_terminal, open_vscode, maximize_vscode, create_project_folder, create_new_file, advancedMoveTo, image_exists 
import pyautogui

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
print('''
           ."`".
       .-./ _=_ \.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
      {_{ }`===`{  _}
     ((((\)     (/))))''')
# first, we wait for caesor to appear
if background_image_finder('monke2.png'):
    open_vscode()
    maximize_vscode()
    params = open_json_file("recent_params.json")
    
    create_project_folder(str(params["concept"]))
    create_new_file(params["concept"])
    code_path = params["code"]
    code = load_from_file(code_path)
    pyautogui.typewrite(convert_code_to_escaped_string(code), interval = .1)
    print("DONE")

    
    
























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
