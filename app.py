from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

import os
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

projects = [
    {'title': '📝 To-Do App', 'desc': 'A Flask app to manage daily tasks (To-Do App)', 'link': 'https://github.com/ritesh-nagtilak/todo-app'},
    {'title': '📰 Blog Website', 'desc': 'A personal blog site built with Python and Flask', 'link': 'https://github.com/ritesh-nagtilak/blog'},
    {'title': '🌐 Portfolio Site', 'desc': 'A personal portfolio site using Flask and Bootstrap', 'link': 'https://github.com/ritesh-nagtilak/portfolio'},
    {'title': '🌦️ Weather App', 'desc': 'Weather forecast app using Flask and OpenWeatherMap API', 'link': 'https://github.com/ritesh-nagtilak/weather-app'},
    {'title': '💬 Chat Application', 'desc': 'A real-time chat app using Flask and Socket.IO', 'link': 'https://github.com/ritesh-nagtilak/chat-app'},
    {'title': '🔗 URL Shortener', 'desc': 'A simple URL shortening service with Flask and SQLite', 'link': 'https://github.com/ritesh-nagtilak/url-shortener'},
]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"Message from {name}",
                      sender=email,
                      recipients=['nagtilakritesh@gmail.com'],
                      body=message)
        mail.send(msg)
        flash("Message sent successfully!")
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
