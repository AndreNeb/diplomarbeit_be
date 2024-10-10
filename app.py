from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Startseite mit Button
@app.route('/')
def home():
    return render_template('index.html')

# Route, die aufgerufen wird, wenn der Button geklickt wird
@app.route('/button-click')
def button_click():
    return "Der Button wurde geklickt!"

if __name__ == '__main__':
    app.run(debug=True)
