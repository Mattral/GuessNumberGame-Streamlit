import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="Guess the Number", page_icon="🔍")

# Page title and description
st.title("Guess the Number Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Input field for the user's guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100)

# Initialize game state
attempts = 0
feedback = ""

if st.button("Check"):
    attempts += 1
    if user_guess < secret_number:
        feedback = "Try a higher number."
    elif user_guess > secret_number:
        feedback = "Try a lower number."
    else:
        feedback = f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
        secret_number = random.randint(1, 100)  # Reset the secret number
        attempts = 0

# Display feedback
st.write(feedback)

# Display attempts
st.write(f"Attempts: {attempts}")

# Hint for a new game
st.write("Can you guess the new number?")

