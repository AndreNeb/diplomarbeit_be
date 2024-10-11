from flask import Flask, render_template, url_for, request
import conDB_Codes as DB
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/search', methods=['POST'])
def search():
    task = request.form['task']
    result = DB.searchKap(task)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


print("Hello World")