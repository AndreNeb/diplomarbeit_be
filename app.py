from flask import Flask, render_template, url_for

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route, die aufgerufen wird, wenn der Button gedrückt wird
@app.route('/button_clicked')
def button_clicked():
    return render_template('button_clicked.html')

if __name__ == '__main__':
    app.run(debug=True)
