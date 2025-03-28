# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKDh1nsjS5ibEfgEfpLNFle5dFVfmSpw
"""

import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY") # or replace with your key as a string.

def generate_response(prompt, model="gpt-3.5-turbo"): # or "gpt-4" if you have access
    """Generates a response using OpenAI's API."""
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7,  # Adjust temperature for creativity
            max_tokens=150,    # Adjust max_tokens for response length
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """Main Streamlit application."""
    st.title("My Local LLM App")

    user_input = st.text_area("Enter your prompt:", height=150)

    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Generating..."):
                response = generate_response(user_input)
            st.write("Response:", response)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()