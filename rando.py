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
# client = Groq()
from typing import List, Optional
import json
from pydantic import BaseModel

# Data model for LLM to generate
class Ingredient(BaseModel):
    name: str
    quantity: str
    quantity_unit: Optional[str]


class Recipe(BaseModel):
    recipe_name: str
    ingredients: List[Ingredient]
    directions: List[str]


def get_recipe(recipe_name: str) -> Recipe:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a recipe database that outputs recipes in JSON.\n"
                # Pass the json schema to the model. Pretty printing improves results.
                f" The JSON object must use the schema: {json.dumps(Recipe.model_json_schema(), indent=2)}",
            },
            {
                "role": "user",
                "content": f"Fetch a recipe for {recipe_name}",
            },
        ],
        model="llama3-8b-8192",
        temperature=0,
        # Streaming is not supported in JSON mode
        stream=False,
        # Enable JSON mode by setting the response format
        response_format={"type": "json_object"},
    )
    return Recipe.model_validate_json(chat_completion.choices[0].message.content)


def print_recipe(recipe: Recipe):
    print("Recipe:", recipe.recipe_name)

    print("\nIngredients:")
    for ingredient in recipe.ingredients:
        print(
            f"- {ingredient.name}: {ingredient.quantity} {ingredient.quantity_unit or ''}"
        )
    print("\nDirections:")
    for step, direction in enumerate(recipe.directions, start=1):
        print(f"{step}. {direction}")


recipe = get_recipe("apple pie")
print_recipe(recipe)
