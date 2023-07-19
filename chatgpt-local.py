import openai

# Set your OpenAI API key here
api_key = "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"
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Example usage:
print("ChatGPT is ready. Type 'exit' to end the conversation.")
user_input = input("You: ")
while user_input.lower() not in ['exit', 'quit']:
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
    user_input = input("You: ")