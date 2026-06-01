from flask import Flask, render_template, request

app = Flask(__name__)

responses.update({

# General
"what is ai": "AI stands for Artificial Intelligence, which enables machines to simulate human intelligence.",
"what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
"what is cloud computing": "Cloud computing provides computing resources over the internet.",
"what is automation": "Automation reduces manual effort by using software and scripts.",
"what is software development": "Software development is the process of designing, building, testing, and maintaining software.",

# DevOps
"why devops": "DevOps improves collaboration between development and operations teams.",
"advantages of devops": "DevOps enables faster delivery, improved quality, and better collaboration.",
"devops lifecycle": "The DevOps lifecycle includes planning, coding, building, testing, releasing, deploying, operating, and monitoring.",
"continuous integration": "Continuous Integration automatically integrates code changes into a shared repository.",
"continuous deployment": "Continuous Deployment automatically deploys code changes to production.",
"continuous delivery": "Continuous Delivery ensures software is always ready for deployment.",

# Git
"what is version control": "Version control tracks changes to code over time.",
"git init": "Git init creates a new Git repository.",
"git add": "Git add stages files for commit.",
"git commit": "Git commit saves staged changes to the repository.",
"git merge": "Git merge combines changes from different branches.",
"git checkout": "Git checkout switches branches or restores files.",
"git status": "Git status shows the current repository state.",
"git log": "Git log displays commit history.",
"what is branching": "Branching allows independent development of features.",
"merge conflict": "A merge conflict occurs when Git cannot automatically combine changes.",

# GitHub
"what is repository": "A repository stores project files and their version history.",
"fork": "Forking creates a copy of another repository in your account.",
"github": "GitHub is a platform for code hosting and collaboration.",
"what is open source": "Open source software allows users to inspect, modify, and distribute source code.",

# Docker
"why docker": "Docker provides consistency across development, testing, and production environments.",
"docker compose": "Docker Compose manages multi-container applications.",
"docker volume": "Docker volumes store persistent data outside containers.",
"docker network": "Docker networks enable communication between containers.",
"containerization": "Containerization packages applications and dependencies together.",
"difference between vm and container": "Containers share the host OS kernel while VMs run separate operating systems.",
"docker hub": "Docker Hub is a cloud-based repository for Docker images.",

# Kubernetes
"what is pod": "A Pod is the smallest deployable unit in Kubernetes.",
"what is deployment": "A Deployment manages application updates and scaling.",
"what is service": "A Service exposes Pods within or outside the cluster.",
"what is ingress": "Ingress manages external access to services in Kubernetes.",
"what is replica set": "A ReplicaSet ensures a specified number of Pod replicas are running.",
"what is cluster": "A Kubernetes cluster consists of control plane and worker nodes.",
"kubectl": "Kubectl is the command-line tool for Kubernetes.",
"scaling": "Scaling increases or decreases application instances based on demand.",

# Jenkins
"what is ci cd pipeline": "A CI/CD pipeline automates build, test, and deployment processes.",
"jenkins": "Jenkins is an open-source automation server.",
"why jenkins": "Jenkins automates repetitive software delivery tasks.",
"pipeline": "A pipeline defines automated software delivery stages.",
"build": "A build compiles and packages source code.",
"testing": "Testing verifies software functionality and quality.",

# AWS
"what is ec2": "EC2 provides scalable virtual servers in AWS.",
"what is s3": "S3 is a highly durable object storage service.",
"what is lambda": "AWS Lambda executes code without managing servers.",
"what is cloudwatch": "CloudWatch monitors AWS resources and applications.",
"what is rds": "Amazon RDS provides managed relational databases.",
"what is iam": "IAM manages AWS users, roles, and permissions.",
"what is elastic beanstalk": "Elastic Beanstalk simplifies application deployment on AWS.",
"what is load balancer": "A load balancer distributes traffic across multiple servers.",

# Linux
"linux commands": "Common Linux commands include ls, pwd, cd, mkdir, rm, and chmod.",
"what is shell": "A shell is a command-line interface for interacting with the operating system.",
"chmod": "chmod changes file permissions.",
"grep": "grep searches for patterns in files.",
"cat": "cat displays file contents.",
"top": "top shows running processes and resource usage.",
"ps": "ps displays process information.",
"sudo": "sudo executes commands with administrative privileges.",

# Python
"what is flask": "Flask is a lightweight web framework for Python.",
"what is django": "Django is a powerful Python web framework.",
"what is api": "An API allows communication between software systems.",
"what is json": "JSON is a lightweight data interchange format.",
"what is pip": "pip is Python's package manager.",
"virtual environment": "A virtual environment isolates Python dependencies.",
"python advantages": "Python is simple, readable, and widely used in AI and automation.",

# Databases
"what is mysql": "MySQL is a relational database management system.",
"what is mongodb": "MongoDB is a NoSQL document-oriented database.",
"what is sql": "SQL is used to query and manage relational databases.",
"primary key": "A primary key uniquely identifies each record in a table.",
"foreign key": "A foreign key links records between tables.",

# Networking
"what is ip": "An IP address uniquely identifies a device on a network.",
"what is dns": "DNS converts domain names into IP addresses.",
"what is http": "HTTP is the protocol used for web communication.",
"what is https": "HTTPS is the secure version of HTTP.",
"what is firewall": "A firewall controls incoming and outgoing network traffic.",
"what is port": "A port identifies a specific service running on a device.",
"what is tcp": "TCP provides reliable communication between devices.",
"what is udp": "UDP provides fast but connectionless communication.",

# Monitoring
"what is prometheus": "Prometheus collects and stores monitoring metrics.",
"what is grafana": "Grafana visualizes monitoring data using dashboards.",
"what is monitoring": "Monitoring tracks system performance and health.",
"what is logging": "Logging records application and system events.",
"alerting": "Alerting notifies administrators about system issues.",

# Security
"what is cybersecurity": "Cybersecurity protects systems, networks, and data from attacks.",
"what is encryption": "Encryption converts data into a secure format.",
"what is ssl": "SSL/TLS secures communication over networks.",
"authentication": "Authentication verifies user identity.",
"authorization": "Authorization determines user permissions.",

# Project Questions
"tell me about your project": "This project demonstrates an AI chatbot deployed using DevOps practices including GitHub, Docker, AWS EC2, and CI/CD.",
"which tools did you use": "The project uses Python, Flask, GitHub, Docker, AWS EC2, and Linux.",
"why did you choose docker": "Docker simplifies deployment by packaging the application and dependencies together.",
"why aws": "AWS provides scalable and reliable cloud infrastructure.",
"future scope": "Future enhancements include NLP integration, voice support, and Kubernetes deployment.",
"team members": "The project was developed collaboratively using GitHub branches and pull requests.",
"project objective": "The objective is to demonstrate chatbot deployment using DevOps principles."
})


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

