import openai

# Replace 'your_api_key_here' with your actual OpenAI API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

# Define a function to interact with the chatbot
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can use "davinci-codex" for code-related tasks
        prompt=prompt,
        max_tokens=50,  # Adjust this as needed
        n=1,
        stop=None,
        temperature=0.7,  # Adjust the temperature for response randomness
    )
    return response.choices[0].text

# Start a conversation with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    prompt = f"You: {user_input}\nBot:"
    bot_response = chat_with_bot(prompt)
    print("Bot:", bot_response)
