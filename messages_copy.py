def messages (send_messages, sent_messages): 

	while send_messages:
		completed_message=send_messages.pop()
		print(f"messages to be sent: {completed_message}")
		sent_messages.append(completed_message)

def completed_messages (sent_messages):
	print("\n The following messages have been sent:")
	for sent_message in sent_messages: 
		print(sent_messages)
		
send_messages=['how are you?', 'good morning']
sent_messages=[]

messages(send_messages, sent_messages)
completed_messages(sent_messages)

