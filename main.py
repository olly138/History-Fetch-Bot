import requests
import json

# Replace with your own Telegram Bot Token
bot_token = '5883905958:AAH-qdIgdhioUrsU-vxAjBMh40zIAR6lXKw'

# Replace with the chat ID of the conversation you want to export
chat_id = '1001602012943'

# Get the number of messages in the chat
url = f'https://api.telegram.org/bot{bot_token}/getChatMembersCount?chat_id={chat_id}'
response = requests.get(url)
data = json.loads(response.text)
message_count = data['result']

# Export the messages
messages = []
for i in range(message_count):
    url = f'https://api.telegram.org/bot{bot_token}/getChatMessage?chat_id={chat_id}&message_id={i}'
    response = requests.get(url)
    data = json.loads(response.text)
    messages.append(data['result'])

# Write the messages to a file
with open('chat_history.txt', 'w') as f:
    for message in messages:
        f.write(message['text'] + '\n')

print('Chat history exported successfully!')