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
FINAL_LIST_DISH_SYSTEM_PROMPT = LIST_DISH_SYSTEM_PROMPT.format(recipe_df = str(df))

# Initialize the session state variables if they don't exist.
if "ingredients" not in st.session_state:
    st.session_state.ingredients = ""
if "list_of_dishes" not in st.session_state:
    st.session_state.list_of_dishes = ""
if "dish_name" not in st.session_state:
    st.session_state.dish_name = ""


def chat_with_gpt(prompt, client, system_prompt):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content


# Styles
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

# First input and button to get list of dishes
ingredients = st.text_input("Enter ingredients separated by commas", key="list_ingredients")
st.session_state.ingredients = ingredients  # Store the ingredients in session state


if st.button("Give me meal suggestions!", key="suggest_meal"):
    prompt = (
        f"Generate a list of dishes using the following ingredients: {ingredients}."
    )
    recipe_response = chat_with_gpt(prompt, client, FINAL_LIST_DISH_SYSTEM_PROMPT)
    st.session_state.list_of_dishes = (
        recipe_response  # Store the list of dishes response in session state
    )

# Always display the list of dishes if it's available
if st.session_state.list_of_dishes:
    st.markdown(
        f"<div class='recipe-style'>{st.session_state.list_of_dishes}</div>",
        unsafe_allow_html=True,
    )

# Second input and button only appear after the first button has been clicked
if st.session_state.list_of_dishes:
    st.session_state.dish_name = st.text_input("Enter dish name", key="user_dish_name")

    if st.button("Cook me a meal!", key="cook_meal"):
        dish_prompt = f"""Generate recipe with detailed instructions and steps for the following dish: {st.session_state.dish_name}
                          based on all or most of the main ingredients mentioned here: {st.session_state.ingredients}."""
        FINAL_DISH_RECIPE_SYSTEM_PROMPT = DISH_RECIPE_SYSTEM_PROMPT.format(user_list_ingredients=st.session_state.ingredients)
        recipe_steps_response = chat_with_gpt(
            dish_prompt, client, FINAL_DISH_RECIPE_SYSTEM_PROMPT
        )
        st.session_state.recipe_steps_response = (
            recipe_steps_response  # Store the recipe steps response in session state
        )

        # Display the recipe steps response
        st.markdown(
            f"<div class='recipe-style'>{st.session_state.recipe_steps_response}</div>",
            unsafe_allow_html=True,
        )
