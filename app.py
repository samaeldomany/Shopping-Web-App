from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        return "Error: All fields are required.", 400
    
    return f"Welcome, {email}. You have logged in successfully."

if __name__ == '__main__':
    app.run(debug=True)
