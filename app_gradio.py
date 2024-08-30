import gradio as gr
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
    with gr.Blocks() as demo:
        gr.Markdown("# Mental Health Companion")

        with gr.Tab("Track Symptoms"):
            api_key = gr.Textbox(label="Enter your OpenAI API Key", type="password")
            mood = gr.Textbox(label="Mood")
            symptoms = gr.Textbox(label="Symptoms")
            behaviors = gr.Textbox(label="Behaviors")
            recommendation_output = gr.Textbox(label="Recommendation", interactive=False)
            gr.Button("Get Recommendation").click(
                fn=generate_recommendation,
                inputs=[mood, symptoms, api_key],
                outputs=recommendation_output
            )

        with gr.Tab("Chat with Bot"):
            user_message = gr.Textbox(label="Your Message")
            bot_response = gr.Textbox(label="Bot Response", interactive=False)
            gr.Button("Send").click(
                fn=chat_with_bot,
                inputs=[user_message, api_key],
                outputs=bot_response
            )

    demo.launch()

if __name__ == '__main__':
    main()
