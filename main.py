import os
import importlib

def load_dataset(module_name):
    module = importlib.import_module(module_name)
    return getattr(module, module_name.split('.')[-1])

def main():
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

    for i in range(0, len(all_conversations), 2):
        question = all_conversations[i]
        answer = all_conversations[i + 1]
        print(f"Q: {question}\nA: {answer}\n")

if __name__ == "__main__":
    main()
