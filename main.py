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


# file = "new_file_select.png"
file = "image.png"
res = pyautogui.locateCenterOnScreen(file, confidence=.5)
if advancedMoveTo([file]):
    # this is where we add the code
    code = '''
    def binary_search(arr, target):
        """Performs binary search on a sorted array to find the target value."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = arr[mid]
            
            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

    # Example usage:
    if __name__ == "__main__":
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 7
        result = binary_search(arr, target)
        
        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the array.")
            '''
    


    recorder = ScreenRecorder("output_with_cursor_follow.avi", fps=30, zoom_factor=2, follow_duration=0.1)
    print("Starting recording...")
    recorder.start_recording()

    pyautogui.typewrite(convert_code_to_escaped_string(code), interval = .1)



    circle(res.x, res.y)
    circle(res.x, res.y)
    circle(res.x, res.y)
    circle(res.x, res.y)

    # Stop recording
    print("Stopping recording...")
    recorder.stop_recording()
    print("Recording saved to output.avi")





































































