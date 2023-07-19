from pyChatGPT import ChatGPT

api = ChatGPT(auth_type='openai', email='topdevstarsup@gmail.com', password='Kutengine227$$$')

resp = api.send_message('Hello, world!')
print(resp['message'])

api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page