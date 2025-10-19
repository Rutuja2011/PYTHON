
#slip1_2
#Write a program to implement Simple Chatbot
responses = {
    "hello": "hello",
    "hii": "how are you",
    "bye": "byee"
}

def get_response(msg):
    msg = msg.lower()
    if msg in responses:
        return responses[msg]
    else:
        return "I didn't understand"

while True:
    user_input = input("You: ")  
    if user_input.lower() == "bye":  
        print("Chatbot:", responses["bye"])
        break
    response = get_response(user_input)  
    print("Chatbot:", response) 
