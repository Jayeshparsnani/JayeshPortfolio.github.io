from flask import Flask, render_template, request, url_for, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'parsnani72@gmail.com'
app.config['MAIL_PASSWORD'] = '..'
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # code to process the form data and send the email
    msg = Message('New Contact Form Submission', sender='parsnani72@gmail.com', recipients=[email])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    # mail.send(msg)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)