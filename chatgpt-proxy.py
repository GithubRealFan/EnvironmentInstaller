from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
api_key = "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"
openai.api_key = api_key

@app.route('/chat', methods=['POST'])
def chat_with_gpt():
    user_input = request.json.get('user_input')
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=150
    )
    
    return jsonify({"response": response['choices'][0]['text'].strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
