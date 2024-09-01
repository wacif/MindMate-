import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq, APITimeoutError
import time

# Load environment variables from a .env file
load_dotenv()

# Create a Groq client using the API key from environment variables
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_recommendation(mood, symptoms):
    if mood.lower() == 'sad':
        return 'Consider talking to a mental health professional or practicing mindfulness.'
    elif 'headache' in symptoms.lower():
        return 'Ensure you are hydrated and well-rested. If symptoms persist, consult a doctor.'
    else:
        return 'Keep monitoring your symptoms. If you need support, reach out to a mental health professional.'

def chat_with_bot(user_message):
    retries = 3  # Number of times to retry the request
    delay = 5    # Delay in seconds between retries
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_message}
                ],
                model="llama3-8b-8192"  # Replace with the appropriate model
            )
            return chat_completion.choices[0].message.content
        except APITimeoutError:
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                return "Request timed out. Please try again later."

# Streamlit UI
st.title("Mental Health Companion")

tab1, tab2 = st.tabs(["Track Symptoms", "Chat with Bot"])

with tab1:
    st.subheader("Track Symptoms")
    mood = st.text_input("Mood")
    symptoms = st.text_input("Symptoms")
    behaviors = st.text_input("Behaviors")
    
    if st.button("Get Recommendation"):
        recommendation = generate_recommendation(mood, symptoms)
        st.text_area("Recommendation", recommendation, height=100)

with tab2:
    st.subheader("Chat with Bot")
    user_message = st.text_input("Your Message")
    
    if st.button("Send"):
        bot_response = chat_with_bot(user_message)
        st.text_area("Bot Response", bot_response, height=100)
