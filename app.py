from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "devops": "DevOps combines development and operations.",
    "docker": "Docker is used for containerization.",
    "kubernetes": "Kubernetes manages containers.",
    "bye": "Goodbye!",
    "python": "Python is a programming language."
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

