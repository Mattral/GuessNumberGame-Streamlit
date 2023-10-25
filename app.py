import streamlit as st
import random

# Generate a random secret number when the game starts
secret_number = random.randint(1, 100)

st.title("Guess the Number Game")

st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

attempts = 0

# Main game loop
while True:
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, key="guess")
    
    attempts += 1
    
    if user_guess == secret_number:
        st.write(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        break
    elif user_guess < secret_number:
        st.write("Try a higher number.")
    else:
        st.write("Try a lower number")

st.write("Thanks for playing!")
