
# getting the API keys and setting up the inference models not stored locally:

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(".env")
Groq_api_key  = os.getenv("GROQ_APIKEY")
# import ipdb; ipdb.set_trace()
hf_token = os.getenv("HF_TOKEN")
client = Groq(api_key = Groq_api_key,)
user_text = "hellow"


# user_text = input("PLease add in the user text, press 0 to quit: ")
if user_text != '0':
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"""
                            You are part of a pipeline designed to create YouTube Shorts videos on coding. 
                            Your role is to receive a string of code and break it down into 3 or 4 key points that highlight important parts of the code. 
                            Then, provide a concise explanation of what each segment of code does.

                            Your explanations should be as if you are explaining the code snippet to someone directly, using natural language that reflects extensive coding experience.
                            The goal is to provide a brief summary of the main elements of the code without any filler sentences or introductory phrases like "Here is the breakdown of the code."

                            The output should include two parts:

                            A brief summary that quickly explains the key elements of the code.
                            A list of lists, where each inner list corresponds to the lines of code to be highlighted for each point mentioned in the summary.
                            This list should be at the end of your response to ensure the rest of the pipeline functions correctly.
                            Avoid using phrases like "steps" in your output to maintain a natural and conversational tone.
                            """
            },
            {
                "role": "user",
                "content": """line 1 :def binary_search(arr, target):
                              line 2 :  low = 0
                              line 3 :  high = len(arr) - 1
                              line 4 :
                              line 5 :  while low <= high:
                              line 6 :      mid = (low + high) // 2
                              line 7 :      if arr[mid] == target:
                              line 8 :          return mid
                              line 9 :      elif arr[mid] < target:
                              line 10 :          low = mid + 1
                              line 11 :      else:
                              line 12 :          high = mid - 1
                              line 13 :  return -1""",
            }
        ],
        model="llama3-8b-8192",
    )

print(chat_completion.choices[0].message.content)