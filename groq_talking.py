
# getting the API keys and setting up the inference models not stored locally:

import os
from groq import Groq
from dotenv import load_dotenv
import json
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
def load_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file = file.read()
            return file
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None



load_dotenv(".env")
Groq_api_key  = os.getenv("GROQ_APIKEY")
# import ipdb; ipdb.set_trace()
hf_token = os.getenv("HF_TOKEN")
client = Groq(api_key = Groq_api_key,)
user_text = "hellow"
params = open_json_file("recent_params.json")
code_path = params["code"]
code = load_from_file(code_path)


# user_text = input("PLease add in the user text, press 0 to quit: ")
if user_text != '0':
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"""
                            You are part of a pipeline designed to create YouTube Shorts videos on coding. You come at the very end of the process, where we are CONCLUDING the video. Your role is to receive a string of code and break it down into 3 or 4 key points that highlight important parts of the code.

                            Instructions:

                            Key Points: Provide 3 to 4 key points that summarize the important elements of the code. Use concise language that reflects extensive coding experience.

                            Concise Explanations: For each key point, provide a short explanation (a few words each) of what that segment of code does. Be direct and straightforward.

                            Avoid Introductory Phrases: Start immediately with the first point. Do not use filler sentences or phrases like "Here is the breakdown of the code." or "The key points are."

                            Code Highlight List: At the end of your response, include a list of lists. Each inner list should correspond to the lines of code to be highlighted for each key point mentioned. This list should be the very last part of your response to ensure the rest of the pipeline functions correctly.

                            Maintain Conversational Tone: Use natural and conversational language, avoiding any technical jargon that isn't necessary for understanding the code snippet.

                            Output Format Example:

                            Point 1: [Brief summary of what this segment of code does]
                            Point 2: [Brief summary of what this segment of code does]
                            Point 3: [Brief summary of what this segment of code does]
                            (Optional) Point 4: [Brief summary of what this segment of code does]
                            [List of lines to highlight for each point in the format [[lines for point 1], [lines for point 2], [lines for point 3], [lines for point 4]]]

                            Example Output:
                            Point 1: Initializes the list with sample data.
                            Point 2: Iterates through each element to check for a condition.
                            Point 3: Filters and collects the items that meet the criteria.
                            [[1], [2-4], [5-7]]
                            """
            },
            {
                "role": "user",
                "content": """
                              def binary_search(arr, target):
                                low = 0
                                high = len(arr) - 1
                              
                                while low <= high:
                                    mid = (low + high) // 2
                                    if arr[mid] == target:
                                        return mid
                                    elif arr[mid] < target:
                                        low = mid + 1
                                    else:
                                        high = mid - 1
                                return -1""",
            }
        ],
        model="llama3-70b-8192", temperature=0.05,
    )

    chat_completion2 = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"""
                            Role Name: Output Validator

                            Description: Validates if the input correctly matches the provided code sections and their corresponding line ranges. each point should correctly respond to its line range.

                            Instructions:

                            Input:

                            Output of the first prompt with explanations ("points") and a "list of lists" indicating line ranges.
                            Code with line numbers.

                            Code

                            Output:
                            Parse the input to extract code lines and output points.
                            For each point, verify it aligns with the correct line ranges from the list of lists.
                            Confirm the number of points matches the number of sublists.
                            After logic checking if the points indeed match logically with the lines, if all is correct, return the same response
                            Otherwise, correct the mistakes and output the correct version.
                            Do not add in any additional lines or phrases apart from mentioned above.
                            Your Output Format Example:

                            Point 1: [Brief summary of what this segment of code does]
                            Point 2: [Brief summary of what this segment of code does]
                            Point 3: [Brief summary of what this segment of code does]
                            (Optional) Point 4: [Brief summary of what this segment of code does]
                            [List of lines to highlight for each point in the format [[lines for point 1], [lines for point 2], [lines for point 3], [lines for point 4]]]

                            Example Output YOU SHOULD GIVE:
                            Point 1: Initializes the list with sample data.
                            Point 2: Iterates through each element to check for a condition.
                            Point 3: Filters and collects the items that meet the criteria.
                            [[1], [2-4], [5-7]]
                            """
            },
            {
                "role": "user",
                "content": f"""input response{chat_completion.choices[0].message.content}
                             This is the code:
                             1: def binary_search(arr, target):
                             2:    low = 0
                             3:    high = len(arr) - 1
                             4:    while low <= high:
                             5:        mid = (low + high) // 2
                             6:        if arr[mid] == target:
                             7:            return mid
                             8:        elif arr[mid] < target:
                             9:            low = mid + 1
                             10:        else:
                             11:            high = mid - 1
                             12:    return -1""" ,
            }
        ],
        model="llama3-70b-8192", temperature=0.05,
    )

    
print("this was the first ones response:")
print(chat_completion.choices[0].message.content)
    
print("##############################################################")
print("Second Revised response:")
print(chat_completion2.choices[0].message.content)