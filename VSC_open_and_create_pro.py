
import subprocess
import pyautogui
import time
# Given a list of images, loops till it finds the image and clicks on it
def advancedMoveTo(list_Images, confidence=0.8):
    '''
    What it does + params:
    list_Images: list of images is sequentially looped. When one image is not found, goes to the next one
                 When it finds the image, moves to it at a speed of .5 second and single left clicks it
    
    condifence: Confidence when finding and clicking an image.
    '''
    for image_path in list_Images:
        try:
            res = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if res:
                print(f"Image found at: {res}")
                pyautogui.click(res.x, res.y, duration= .5)
                return True  # Exit the function once an image is found
            else:
                print(f"Image not found on the screen: {image_path}")
        except pyautogui.ImageNotFoundException:
            print(f"Image could not be found: {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    print("None of the images were found.")
    return False  # Return False if no image was found

def image_exists(image_path, confidence = .8):
    try:
        res = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if res:
            return True  # Exit the function once an image is found
        else:
            return False
    except pyautogui.ImageNotFoundException:
        print(f"Image could not be found: {image_path}")

# Opens vs code by doing ctrl+shift+n given you ran the code in terminal
def open_vscode():
    '''
    Opens vs code by doing ctrl+shift+n given you ran the code in terminal
    '''
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(4)  # Wait for VSCode to open
    # pyautogui.press('enter', interval=0.1)

def maximize_vscode():
    """
    maximizes the vs_code window
    """
    # Simulate pressing just F11 to enter full screen
    # pyautogui.click(pyautogui.locateCenterOnScreen("vs_pics/maximize.png"), duration = .4)
    pyautogui.hotkey('f11')
    time.sleep(2)  # Wait for the action to complete

def create_project_folder(folder_name):
    
    pyautogui.hotkey('ctrl', 'k', 'o')
    time.sleep(2)
    # pyautogui.click(pyautogui.locateCenterOnScreen("vs_pics/folder_window.png", confidence=0.8), duration = 1)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.typewrite(folder_name, interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    if image_exists("vs_pics/confirm_folder_replace.png"):
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        # pyautogui.click(pyautogui.locateCenterOnScreen("vs_pics/folder_window.png", confidence=.5), duration=.5)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite(folder_name, interval=0.1)
        pyautogui.press('enter')
        pyautogui.press('enter')

    else:
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        # pyautogui.click(pyautogui.locateCenterOnScreen("vs_pics/select_folder.png", confidence=.6), duration=.5)

    time.sleep(1)

def create_new_file(file_name):
    pyautogui.hotkey('ctrl', 'shift', 'p')
    time.sleep(1)
    pyautogui.typewrite('new file', interval=0.1)
    pyautogui.press('enter', interval=.1)
    time.sleep(1)
    pyautogui.typewrite(f"{file_name}.py", interval=0.1)
    time.sleep(1)
    pyautogui.press('enter', interval=.1)
    time.sleep(1)
    pyautogui.press('enter', interval=.1)
    time.sleep(1)

def test_typing():
    pyautogui.typewrite('Hello, World!', interval=0.1)

def new_WSL_terminal():
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)
    pyautogui.typewrite('New Terminal', interval=0.1)
    pyautogui.press('enter')

def new_anaconda_terminal():
    pyautogui.hotkey('ctrl', 'alt', 'a')
    time.sleep(1)
    pyautogui.typewrite('New Terminal', interval=0.1)
    pyautogui.press('enter')

def activate_env(name):
    pyautogui.typewrite(f"conda activate {name}", interval=0.1)

import pyautogui
import time

def highlight_lines_based_on_dict(highlight_dict):
    """
    Automates highlighting lines in a text editor based on the specified highlight dictionary, with timing control.

    Parameters:
    highlight_dict (dict): A dictionary where keys are text descriptions and values are tuples.
    Each tuple contains a list of line numbers to highlight and a start time in seconds.
    """

    # Start at the beginning of the document
    pyautogui.hotkey('ctrl', 'g')  # Open "Go to line" dialog
    pyautogui.typewrite('1')  # Type line number 1
    pyautogui.press('enter')  # Go to line 1
    time.sleep(0.5)  # Wait for the cursor to move

    start_time = time.time()  # Record the start time of the script

    # Get all highlight start times in order
    highlight_times = list(highlight_dict.values())

    for i, (key, (lines_to_highlight, highlight_start_time)) in enumerate(highlight_dict.items()):
        # Determine the time to highlight until based on the next start time
        if i < len(highlight_times) - 1:
            next_highlight_start_time = highlight_times[i + 1][1] - 1  # 1 second before the next highlight
        else:
            next_highlight_start_time = float('inf')  # Last highlight, no end time

        # Wait until the desired highlight start time
        while (time.time() - start_time) < highlight_start_time:
            time.sleep(0.1)  # Wait in short intervals until the desired time

        # Calculate total available time for highlighting
        available_time = next_highlight_start_time - highlight_start_time

        # Ensure available_time is not negative or extremely large
        if available_time < 0 or available_time > 3600:  # Example check: ensure it's not longer than 1 hour
            available_time = 0.1  # Set to a reasonable default

        # Calculate delay between each line highlight to fill the available time
        if len(lines_to_highlight) > 0:
            highlight_delay = max(available_time / len(lines_to_highlight), 0.1)  # Ensure a minimum delay of 0.1
        else:
            highlight_delay = 0.1  # Default delay if there are no lines

        # Highlight the lines specified in the highlight_dict within the available time
        for _ in range(len(lines_to_highlight)):
            pyautogui.keyDown('shift')  # Hold down the shift key
            pyautogui.press('down')  # Press down arrow to highlight the line
            pyautogui.keyUp('shift')  # Release the shift key
            time.sleep(highlight_delay)  # Delay to simulate natural highlighting speed

        # Keep the last highlight visible for 3 seconds
        if i == len(highlight_times) - 1:
            time.sleep(3)
        else:
            # Wait until 1 second before the next highlight start time
            while (time.time() - start_time) < next_highlight_start_time:
                time.sleep(0.1)

            # Move cursor to the end of the highlighted text
            pyautogui.press('right')  # Press right arrow to move to the end of the highlight

        time.sleep(0.5)  # Short delay between operations to ensure accuracy


def start_recording():
    print("Starting recording")
    pyautogui.hotkey('ctrl', 'shift', '8', interval=0.5)


def stop_recording():
    print("Stopping recording")
    pyautogui.hotkey('ctrl', 'shift', '9', interval=0.5)
    



