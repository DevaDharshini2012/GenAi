import streamlit as st
import cohere

# Set up Cohere client
co = cohere.Client('qjgBfmYonpwhjFsICmNvdVCL4idkxCaSJvt7qYMJ')  # Replace with your actual API key

st.set_page_config(page_title="AI Recipe Generator", layout="centered")
st.title("🍽️ AI Recipe Generator")
st.write("Enter a few ingredients and get a recipe suggestion using Cohere!")

# Input from user
ingredients = st.text_input("Enter ingredients (e.g., chicken, garlic, tomatoes):")

if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Generating your recipe..."):
            try:
                response = co.chat(
                    model='command-r-plus',
                    message=ingredients
                )
                st.subheader("🍲 Recipe:")
                st.write(response.text.strip())
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some ingredients first.")