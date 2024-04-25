import streamlit as st
import os
from openai import OpenAI
from prompts import *
import pandas as pd

os.environ["OPENAI_API_KEY"] = (
    ""
)
client = OpenAI()
recipe_csv_filepath = "Cleaned_Indian_Food_Dataset.csv"
df = pd.read_csv(recipe_csv_filepath)
LIST_DISH_SYSTEM_PROMPT = f"{LIST_DISH_SYSTEM_PROMPT}"

# Initialize the session state variables if they don't exist.
if "dish_suggested" not in st.session_state:
    st.session_state.dish_suggested = False
if "ingredients" not in st.session_state:
    st.session_state.ingredients = ""
if "list_of_dishes" not in st.session_state:
    st.session_state.list_of_dishes = ""


def chat_with_gpt(prompt, client, system_prompt):

    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content

st.markdown(
    """
    <style>
        body {
            background-color: #fff8e1;
            color: #4f4f4f;
            font-family: sans-serif;
        }

        h1 {
            color: #795548;
            font-family: 'Raleway', sans-serif;
        }

        input, select {
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #ff5722;
            border: none;
            border-radius: 4px;
            color: white;
            font-family: 'Raleway', sans-serif;
            padding: 8px 16px;
            text-decoration: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #e64a19;
        }

        .widget-box {
            background-color: #ffffff;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin-bottom: 16px;
        }
        .recipe-container {
            background-color: #f5f5f5;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }

    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Khaana khazana")

# Choose input type
with st.sidebar:
    st.header("Instructions")
    input_type = st.selectbox("", ["Ingredients"])


# Get user input
prompt = "You are a helpful assistant that creates Indian recipes from a list of ingredients."
ingredients = ""

if input_type == "Ingredients":
    ingredients = st.text_input("Enter ingredients separated by commas")
    prompt = (
        f"Generate a list of dishes using the following ingredients: {ingredients}."
    )

st.session_state.ingredients = ingredients

recipe_name = ""
list_of_dishes = ""
if st.button("Give me meal suggestions!"):
    recipe_response = chat_with_gpt(prompt, client, LIST_DISH_SYSTEM_PROMPT)
    # Split the response into lines and find the recipe name
    if not recipe_response:
        recipe_response = "Recipe name"

    lines = recipe_response.split("\n")

    for line in lines:
        if "recipe name" in line.lower():
            recipe_name = line.strip()
        else:
            list_of_dishes += line.strip() + "\n"

    st.session_state.list_of_dishes = list_of_dishes

    if "list_of_dishes" in st.session_state and st.session_state.list_of_dishes:
        with st.container() as recipe_container:
            # Add your recipe content here using st.markdown and st.write
            st.markdown(f"{recipe_name}")
            # ... rest of the recipe content ...
            st.markdown(
                f'<div class="recipe-style">{st.session_state.list_of_dishes}</div>',
                unsafe_allow_html=True,
            )
            st.session_state.dish_suggested = True

if st.session_state.dish_suggested:

    dish_name = st.text_input("Enter dish name")
    dish_prompt = f"""Generate recipe with detailed instructions and steps for the following dish: {dish_name}
                        based on all or most of the main ingredients mentioned here: {ingredients}."""

    if st.button("Cook me a meal!"):
        recipe_steps_response = chat_with_gpt(
            dish_prompt, client, DISH_RECIPE_SYSTEM_PROMPT
        )

        if not recipe_steps_response:
            recipe_steps_response = "Recipe Steps"

        st.markdown(
            f'<div class="recipe-style">{st.session_state.list_of_dishes}</div>',
            unsafe_allow_html=True,
        )

        with st.container() as recipe_steps_container:
            st.markdown(f"{dish_name}")
            st.markdown(
                f'<div class="recipe-style">{recipe_steps_response}</div>',
                unsafe_allow_html=True,
            )
