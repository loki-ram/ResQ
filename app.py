from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('homepage.html')

# Chatbot Page
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Disaster Updates Page
@app.route('/disaster')
def disaster():
    return render_template('alert.html')

# Preparedness Tools Page
@app.route('/preparedness')
def preparedness():
    return render_template('preparedness.html')

# Community Forum Page
@app.route('/forum')
def forum():
    return render_template('forum.html')

if __name__ == "__main__":
    app.run(debug=True)
