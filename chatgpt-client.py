import requests

def send_request_to_vps(user_input):
    vps_url = "http://188.43.14.13:443/chat"
    data = {"user_input": user_input}
    response = requests.post(vps_url, json=data)
    return response.json()["response"]

# Example usage:
print("ChatGPT is ready. Type 'exit' to end the conversation.")
user_input = input("You: ")
while user_input.lower() not in ['exit', 'quit']:
    response = send_request_to_vps(user_input)
    print("ChatGPT:", response)
    user_input = input("You: ")