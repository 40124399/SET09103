from sys import argv
from flask import Flask, render_template
app = Flask(__name__)
filename = "static/db.txt"
myFile = open("static/db.txt", "r")

@app.route('/')
def home():
    work = "search"
    return render_template('home.html', work=work)

@app.route('/db/', methods=["GET","POST"])
def footer():
    return render_template('footer.html')

@app.route('/search/', methods=["GET","POST"])
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
