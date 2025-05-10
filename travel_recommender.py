import streamlit as st
import cohere

# Set up Cohere client
co = cohere.Client('your_cohere_api_key')  # Replace with your actual API key

st.set_page_config(page_title="AI Travel Recommender", layout="centered")
st.title("🌍 AI Travel Destination Recommender")
st.write("Tell me what you're in the mood for, and I'll recommend a travel destination!")

# User input
mood = st.text_input("What are you in the mood for? (e.g., beach relaxation, mountain hiking, cultural exploration):")

if st.button("Suggest Destination"):
    if mood:
        with st.spinner("Finding the perfect destination..."):
            try:
                response = co.chat(
                    model='command-r-plus',
                    message=f"Suggest a travel destination based on this mood: {mood}. Include why it's a good fit."
                )
                st.subheader("✈️ Suggested Destination:")
                st.write(response.text.strip())
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter your mood or interest.")
