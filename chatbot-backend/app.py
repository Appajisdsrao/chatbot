from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Predefined responses
predefined_answers = {
    "devops": {
        "what is devops?": "DevOps is a set of practices that combines software development and IT operations to shorten the development lifecycle.",
        "what are the benefits of devops?": "DevOps improves deployment frequency, reduces failure rates, and enables faster time-to-market.",
        "what is ci/cd?": "CI/CD stands for Continuous Integration and Continuous Deployment, ensuring automated testing and deployment.",
        "what is docker?": "Docker is a platform that allows developers to build, deploy, and run applications in containers.",
        "what is kubernetes?": "Kubernetes is an open-source container orchestration system for automating application deployment, scaling, and management."
    },
    "technical": {
        "what is cloud computing?": "Cloud computing is the delivery of computing services over the internet, allowing on-demand access to resources.",
        "what is an api?": "An API (Application Programming Interface) is a set of rules that allows applications to communicate with each other.",
        "what is machine learning?": "Machine Learning is a branch of AI that enables computers to learn and make decisions from data.",
        "what is artificial intelligence?": "Artificial Intelligence (AI) is the simulation of human intelligence in machines that can perform tasks requiring human-like decision-making.",
        "what is cybersecurity?": "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks."
    },
    "general": {
        "what is your name?": "I am an AI chatbot.",
        "how are you?": "I'm just a bot, but thanks for asking! How can I help you today?",
        "who created you?": "I was created by developers using Python and Flask.",
        "what is the capital of france?": "The capital of France is Paris.",
        "how old are you?": "I am just a program and do not have an age."
    },
    "jokes": {
        "tell me a joke": "Why don’t programmers like nature? It has too many bugs!",
        "another joke": "Why do Java developers wear glasses? Because they don’t C#.",
        "one more joke": "Why was the computer cold? It left its Windows open!"
    },
    "introduction": {
        "introduce yourself": "Hello! I am a chatbot. I can answer questions about DevOps, technology, and general topics, and I can even tell jokes!",
        "what can you do?": "I can answer DevOps, technical, and general questions. I can also tell jokes!"
    },
    "human_interaction": {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm here to help!",
        "who are you": "I'm a chatbot designed to assist you.",
        "what is your name": "You can call me Chatbot!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Happy to help.",
        "what can you do": "I can answer your questions and provide assistance!"
    }
}

def get_predefined_response(user_message):
    user_message = user_message.lower().strip()
    for category, qa_pairs in predefined_answers.items():
        if user_message in qa_pairs:
            return qa_pairs[user_message]
    return "I don't understand that question. Try asking something else!"

@app.route('/ask', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400
    response = get_predefined_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

