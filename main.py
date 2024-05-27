from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import wikipedia
import importlib

# Function to load datasets
def load_dataset(module_name):
    module = importlib.import_module(module_name)
    return getattr(module, module_name.split('.')[-1])

# Function to search Wikipedia for a topic and learn from it
def search_and_learn(topic):
    try:
        # Search Wikipedia for the topic
        search_results = wikipedia.search(topic)
        if search_results:
            # Get the summary of the first search result
            summary = wikipedia.summary(search_results[0])
            # Train the chatbot with the summary
            chatbot.set_trainer(ListTrainer)
            chatbot.train([summary])
            return summary
        else:
            return "Sorry, I couldn't find information on that topic."
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        return f"Can you please clarify which {topic} you are referring to?"
    except wikipedia.exceptions.PageError as e:
        # Handle page not found errors
        return "Sorry, I couldn't find information on that topic."

# Function to get response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    
    # Check if the confidence level of the response is below a certain threshold
    if response.confidence < 0.5:
        new_info = search_and_learn(user_input)
        return new_info if new_info else "I don't know"
    else:
        return response

# Function to initialize chatbot
def initialize_chatbot():
    # Initialize chatbot
    chatbot = ChatBot("Robert")
    datasets = [
        "linux_conversations",
        "xfce_conversations",
        "general_knowledge_conversations",
        "politics_conversations"
    ]

    all_conversations = []

    for dataset in datasets:
        conversations = load_dataset(dataset)
        all_conversations.extend(conversations)

    # Train chatbot with conversations
    chatbot.set_trainer(ListTrainer)
    chatbot.train(all_conversations)

    return chatbot

# Main function
def main():
    global chatbot
    chatbot = initialize_chatbot()

    print("Robert: Hi, I'm Robert. How can I assist you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Robert: Goodbye!")
            break
        response = get_response(user_input)
        print("Robert:", response)

if __name__ == "__main__":
    main()

