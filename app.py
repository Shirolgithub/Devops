from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How can I assist you?",
    "devops": "DevOps combines development and operations.",
    "docker": "Docker is used for containerization.",
    "kubernetes": "Kubernetes manages containers.",
    "bye": "Bye.Have nice day",
    "python": "Python is used in AI and DevOps."
    
}

responses = { "hello": "Hello! How can I help you?", "hi": "Hi there! ", "devops": "DevOps combines development and operations.", "docker": "Docker is used for containerization.", "kubernetes": "Kubernetes manages containers.", "bye": "Bye.Have great day", "Good morning":"Very Good Morning", "hi": "Hi there!How can i assist you", "devops": "DevOps combines development and operations.", "docker": "Docker is used for containerization.", "kubernetes": "Kubernetes manages containers.", "bye": "Bye.bye.Updated by Manoj", "Good morning":"Very Good Morning", "python": "Python is used in AI and DevOps." }
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

