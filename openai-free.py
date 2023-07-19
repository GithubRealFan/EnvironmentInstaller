from pyChatGPT import ChatGPT

api = ChatGPT(auth_type='google', email='daviddibella79@gmail.com', password='Zara1235')

resp = api.send_message('Hello, world!')
print(resp['message'])

api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page