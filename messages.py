def show_messages(messages):
	for message in messages:
		msg=f"{message.title()}."
		print(msg)

shown_messages = ['how are you?', 'where do you live?', 'what is your name?']
show_messages(shown_messages)