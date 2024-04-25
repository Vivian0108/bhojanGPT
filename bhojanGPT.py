#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import openai
from openai import OpenAI

client = OpenAI()
# In[4]:


def chat_with_gpt(prompt, client):
    
    completion = client.chat.completions.create(
        model = "gpt-4-turbo-2024-04-09",
        messages = [
            {"role": "system", "content": "You are a helpful Indian recipe generating assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


# In[12]:


# Streamlit app
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #00008B;
#             color: #483d8b;
#             font-family: 'Georgia', serif;
#         }

#         h1 {
#             color: #800000;
#             font-family: 'Raleway', sans-serif;
#             margin-bottom: 20px;
#         }

#         input, select {
#             border: 1px solid #ccc;
#             border-radius: 4px;
#         }

#         button {
#             background-color: #483d8b;
#             color: #e6e6fa;
#             border: none;
#             border-radius: 4px;
#             font-family: 'Raleway', sans-serif;
#             padding: 8px 16px;
#             text-decoration: none;
#             cursor: pointer;
#         }

#         button:hover {
#             background-color: #e64a19;
#         }

#         .widget-box {
#             background-color: #ffffff;
#             border-radius: 4px;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#             margin-bottom: 16px;
#             padding: 30px;

#         }

#         .reportview-container {
#             background: #fff8e1;
#         }
#         .main {
#             background: #fff8e1;
#         }
#         .block-container {
#             background: #fff8e1;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

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
    </style>
    """,
    unsafe_allow_html=True,
)

# In[5]:

st.title("Khaana khazana")


# In[ ]:

# Choose input type
with st.sidebar:
    st.header("Instructions")
    input_type = st.selectbox("", ["Ingredients"])


# In[11]:


# Get user input
prompt = "You are a helpful assistant that creates Indian recipes from a list of ingredients."
if input_type == "Ingredients":
    ingredients = st.text_input("Enter ingredients separated by commas")
    prompt = f"Create a recipe using the following ingredients: {ingredients}. Provide a recipe name, ingredients and detailed steps. Add calories for the recipe as well"


# In[7]:
recipe_name = ""
ingredients_and_steps = ""
if st.button("Cook me a meal!"):
    recipe_response = chat_with_gpt(prompt, client)
    # Split the response into lines and find the recipe name
    if not recipe_response:
        recipe_response = "Recipe name"

    lines = recipe_response.split('\n')

    for line in lines:
        if "recipe name" in line.lower():
            recipe_name = line.strip()
        else:
            ingredients_and_steps += line.strip() + "\n"


# In[10]:
with st.container():
    st.markdown("""
    <style>
        .recipe-style {
            color: #2a2a2a;  /* Darker text color for better readability */
            background-color: #e6e6fa;  /* Light lavender background */
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f"## {recipe_name}")
    st.markdown(f'<div class="recipe-style">{ingredients_and_steps}</div>', unsafe_allow_html=True)

    # st.markdown(recipe_response)

