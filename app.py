import streamlit as st
import random

# Set a dark theme for the Streamlit app
st.markdown(
    """
    <style>
    .stApp {
        background: #121212;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background: #121212;
        color: #ffffff;
    }
    .stTextInput > div > label {
        color: #ffffff;
    }
    .stButton > button {
        background: #009688;
        color: #ffffff;
    }
    .stButton > button:hover {
        background: #007a6b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Guess the Number Game")

st.markdown("I'm thinking of a number between 1 and 100. Can you guess what it is?", unsafe_allow_html=True)

# Generate a random secret number when the game starts
secret_number = random.randint(1, 100)

attempts = 0

user_guess = st.number_input(f"Enter your guess ({attempts} attempts):", min_value=1, max_value=100)

if st.button("Guess"):
    attempts += 1

    if user_guess == secret_number:
        st.markdown(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.", unsafe_allow_html=True)
    elif user_guess < secret_number:
        st.markdown("Try a higher number.", unsafe_allow_html=True)
    else:
        st.markdown("Try a lower number.", unsafe_allow_html=True)
