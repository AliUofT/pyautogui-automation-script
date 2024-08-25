from pygui import type_code_naturally, circle
from VSC_open_and_create_pro import advancedMoveTo,open_vscode,maximize_vscode,create_project_folder, create_new_file
import time
import pyautogui
from screen_recorder import ScreenRecorder


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
            print(f"we will be doing {(prev_space- leading_spaces)//4} back spaces")
            escaped_string += '\n' + ('\b' * ((prev_space- leading_spaces)//4)) + stripped_line

        print("")
        prev_space = leading_spaces
            
    return escaped_string

def start_typing(code):
    # file = "new_file_select.png"
    file = "image.png"
    # res = pyautogui.locateCenterOnScreen(file, confidence=.5)
    if advancedMoveTo([file]):
        # this is where we add the code
        code = code
        


        recorder = ScreenRecorder("output_with_cursor_follow.avi", fps=30, zoom_factor=2, follow_duration=0.1)
        print("Starting recording...")
        recorder.start_recording()

        pyautogui.typewrite(convert_code_to_escaped_string(code), interval = .1)

        # Stop recording
        print("Stopping recording...")
        recorder.stop_recording()
        print("Recording saved to output.avi")


# TEMPORARY:
def load_code_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            return code
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None

# open_vscode()
# maximize_vscode()
# create_project_folder(folder_name)
# create_new_file(file_name)
# 




code = load_code_from_file("binary search_code.txt")
print(code)

# a method, that runs in the background, and everytime a specific thing shows up, it opens a command prompt or anaconda prompt, 
# and is able to run the code there





































































