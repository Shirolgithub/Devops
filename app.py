from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How can I assist you?",
    "good morning": "Very Good Morning!",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "bye": "Bye! Have a great day.",
    "python": "Python is used in AI and DevOps.",
    "devops": "DevOps combines development and operations.",
    "docker": "Docker is used for containerization.",
    "kubernetes": "Kubernetes manages containers.",
    "jenkins": "Jenkins automates CI/CD pipelines.",
    "aws": "AWS is a cloud computing platform.",
    "git": "Git is a version control system.",
    "github": "GitHub hosts Git repositories.",
    "linux": "Linux is a popular operating system.",
    "flask": "Flask is a lightweight Python web framework.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning enables systems to learn from data.",
    "what is cloud computing": "Cloud computing provides computing services over the internet.",
    "what is ci cd": "CI/CD stands for Continuous Integration and Continuous Deployment.",
    "what is docker": "Docker packages applications into containers.",
    "what is kubernetes": "Kubernetes orchestrates and manages containers.",
    "what is jenkins": "Jenkins is an automation server used for CI/CD.",
    "what is aws": "AWS provides cloud infrastructure services.",
    "what is git": "Git tracks changes in source code.",
    "what is github": "GitHub is a platform for code collaboration.",
    "what is linux": "Linux is an open-source operating system.",
    "tell me about your project": "This project demonstrates DevOps practices using GitHub, Docker, AWS and Flask.",
    "future scope": "Future scope includes AI integration, NLP and Kubernetes deployment.",
    "team members": "The project was developed collaboratively using GitHub branching and pull requests."
}
@app.route('/', methods=['GET', 'POST'])
def home():
    user_message = ""
    bot_reply = ""

    if request.method == 'POST':
        user_message = request.form['message'].lower()
        bot_reply = responses.get(user_message, "I am still learning.")

    return render_template(
        'index.html',
        user_message=user_message,
        bot_reply=bot_reply
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

