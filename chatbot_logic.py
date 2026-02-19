def get_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hello! How can I assist you today?"
    elif "price" in message:
        return "Please contact our sales team for pricing details."
    elif "services" in message:
        return "We provide IT support, software solutions, and automation services."
    elif "contact" in message:
        return "You can contact us at support@example.com"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"
