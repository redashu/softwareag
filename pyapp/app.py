from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
