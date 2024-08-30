import streamlit as st
import openai

def generate_recommendation(mood, symptoms, api_key):
    openai.api_key = api_key
    if mood == 'sad':
        return 'Consider talking to a mental health professional or practicing mindfulness.'
    elif 'headache' in symptoms:
        return 'Ensure you are hydrated and well-rested. If symptoms persist, consult a doctor.'
    else:
        return 'Keep monitoring your symptoms. If you need support, reach out to a mental health professional.'

def chat_with_bot(user_message, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message['content']

def main():
    st.title('Mental Health Companion')

    # API Key Input
    st.sidebar.header('API Key')
    api_key = st.sidebar.text_input('Enter your OpenAI API Key', type='password')

    if not api_key:
        st.warning('Please enter your OpenAI API Key to use the app.')
        return

    # Symptom Tracking
    st.header('Track Symptoms')
    mood = st.text_input('Mood', '')
    symptoms = st.text_input('Symptoms', '')
    behaviors = st.text_input('Behaviors', '')

    if st.button('Get Recommendation'):
        recommendation = generate_recommendation(mood, symptoms, api_key)
        st.write('Recommendation:', recommendation)

    # Chatbot Interaction
    st.header('Chat with Bot')
    user_message = st.text_area('Your Message')
    
    if st.button('Send'):
        bot_response = chat_with_bot(user_message, api_key)
        st.write('Bot Response:', bot_response)

if __name__ == '__main__':
    main()
