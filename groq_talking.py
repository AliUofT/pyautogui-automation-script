
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
            # print(f"Successfully loaded JSON file: {file_path}")
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
def add_line_numbers(code):
    # Split the input code into lines
    lines = code.split('\n')
    
    # Initialize a list to store the lines with numbers
    numbered_lines = []
    
    # Iterate over the lines and add line numbers
    for i, line in enumerate(lines, start=1):
        # Format the line with its number and add it to the list
        numbered_lines.append(f"{i}: {line}")
    
    # Join the numbered lines back into a single string
    return '\n'.join(numbered_lines)

def highlight_code_lines(text_lines, highlight_mapping):
    """
    Function to map text lines to corresponding code lines to be highlighted.

    Parameters:
    text_lines (list of str): List of text descriptions for the code.
    highlight_mapping (list of list): List of lists where each sublist contains the code line numbers to highlight.

    Returns:
    dict: A dictionary mapping each text line to the corresponding code lines to highlight.
    """
    text_lines = text_lines.splitlines()
    # Check if the lengths of text_lines and highlight_mapping match
    print(f"this is the length of text_lines: {len(text_lines)}")
    print(f"this is the length of highlight_mapping: {len(highlight_mapping)}")
    if len(text_lines) != len(highlight_mapping):
        raise ValueError("The length of text_lines and highlight_mapping must be the same.")

    # Create a dictionary to store the mapping
    highlight_dict = {}

    # Iterate through the text lines and the corresponding highlight ranges
    for text_line, code_lines in zip(text_lines, highlight_mapping):
        highlight_dict[text_line] = code_lines

    return highlight_dict



load_dotenv(".env")
Groq_api_key  = os.getenv("GROQ_APIKEY")
# import ipdb; ipdb.set_trace()
hf_token = os.getenv("HF_TOKEN")
client = Groq(api_key = Groq_api_key,)
user_text = "hellow"
params = open_json_file("recent_params.json")
code_path = params["code"]
code = load_from_file(code_path)
code = add_line_numbers(code)





# user_text = input("PLease add in the user text, press 0 to quit: ")
if user_text != '0':
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"""
                            You are part of a pipeline designed to create YouTube Shorts videos on coding. You come at the very end of the process, where we are CONCLUDING the video. Your role is to receive a string of code and break it down into 3 or 4 key points that highlight important parts of the code.

                            Instructions:

                            Key Points: Provide 3 to 4, (5 if really necessary to include everything)  key points that summarize the important elements of the code. Use concise language that reflects extensive coding experience.

                            Concise Explanations: For each key point, provide a short explanation (a few words each) of what that segment of code does. Be direct and straightforward.

                            Avoid Introductory Phrases: Start immediately with the first point. Do not use filler sentences or phrases like "Here is the breakdown of the code." or "The key points are."
                            Your first output sentence should be Point 1
                            Code Highlight List: At the end of your response, include a list of lists. Each inner list should correspond to the lines of code to be highlighted for each key point mentioned. This list should be the very last part of your response to ensure the rest of the pipeline functions correctly.

                            Maintain Conversational Tone: Use natural and conversational language, avoiding any technical jargon that isn't necessary for understanding the code snippet.

                            Output Format Example:

                            Point 1: [Brief summary of what this segment of code does]
                            Point 2: [Brief summary of what this segment of code does]
                            Point 3: [Brief summary of what this segment of code does]
                            Point 4: [Brief summary of what this segment of code does]
                            [List of lines to highlight for each point in the format [[lines for point 1], [lines for point 2], [lines for point 3], [lines for point 4]]]

                            Example Output:
                            Point 1: Initializes the list with sample data.
                            Point 2: Iterates through each element to check for a condition.
                            Point 3: Filters and collects the items that meet the criteria.
                            [[1], [2,3,4], [5,6,7]]
                            """
            },
            {
                "role": "user",
                "content": code,
            }
        ],
        model="llama3-70b-8192", temperature=0.00,
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
                            Try to include the last line of the code, or final return values
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
                            [[1], [2,3,4], [5,6,7]]
                            """
            },
            {
                "role": "user",
                "content": f"""input response{chat_completion.choices[0].message.content}
                             This is the code:
                             {code}""" ,
            }
        ],
        model="llama3-70b-8192", temperature=0.00,
    )

    informal_summary = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"""
                            You are tasked with converting technical descriptions of code into natural, conversational explanations suitable for YouTube Shorts. Given a structured, step-by-step breakdown of a code snippet, your role is to rewrite the explanation in a way that sounds natural, engaging, and easy to understand.

                            The output should provide a quick overview of the code's functionality in a clear and friendly tone, as if you were speaking directly to someone with moderate coding experience. Avoid overly formal or technical language and instead use a more informal, conversational style. Make sure to maintain the correct order of operations but convey the information in a way that feels less rigid and more like everyday speech.
                            DO NOT USE Introductory Phrases: Start IMMEDIATELY with the first point. Do not use filler sentences or phrases like "Here's a rewritten explanation in a natural, conversational tone:" or "The key points are." or "Here's how the code works: "
                            you should begin with the output right away.
                            Make sure the each point is on a seperate line.
                            For example, the input you will get would describe the steps like this:

                            Point 1: Sets up the initial boundaries for the search.
                            Point 2: Calculates the midpoint and checks if it's the target.
                            Point 3: Adjusts the boundaries based on the comparison result.
                            Point 4: Returns the index if found, or -1 if not found.
                            [[1,2,3], [6,7], [9,10,11,12], [13]]

                            Your output should looks something like this:

                            "To give you a quick overview, we start by setting up the initial boundaries for the search. 
                            Then, we calculate the midpoint and check if it's the target. 
                            If it's not, we adjust the boundaries based on the comparison result. 
                            Finally, we return the index if the target is found; otherwise, we return -1."

                            Your output should follow this structure, summarizing the key points in a natural flow without listing them as numbered steps.
                            you should start immediatly by an informal opening, a variation of something like: "To give you a quick overview," or " To start off" or "we start by first" or " Here we begin by"
                            Avoid Introductory Phrases: Start immediately with the informal opening. Do not use filler sentences or phrases
                            Make sure that the points start with the same exact words, and all you do is add some prefix words to make the transitions between the points smoother.



                            """
            },
            {
                "role": "user",
                "content": chat_completion2.choices[0].message.content,
            }
        ],
        model="llama3-70b-8192", temperature=1,
    )



    
# print("this was the first ones response:")
# print(chat_completion.choices[0].message.content)
    
# print("##############################################################")
# print("Second Revised response:")
full_summary = chat_completion2.choices[0].message.content
# print(full_summary)

highlighting_lines = full_summary.splitlines()[-1]
import ast # to convert python literals into actual python types like list strings into actual strings.
highlighting_lines = ast.literal_eval((highlighting_lines))
print(f"this is the type of highlighting_lines: {type(highlighting_lines)}")
print(highlighting_lines)


print("\n")
print(informal_summary.choices[0].message.content)

overview = informal_summary.choices[0].message.content

# highlight_dict = highlight_code_lines(overview, highlighting_lines)
# print(highlight_dict)

# print("#####################################")
# print("\n\n")
# print(f"This is the code: ")
# print(code)