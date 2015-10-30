from sys import argv
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    work = "search"
    return render_template('home.html', work=work)

@app.route('/db/', methods=["GET","POST"])
def footer():
    return render_template('footer.html')

@app.route('/search/', methods=["GET","POST"])
def search():
    html = ""
    bus = []
    memoriZe=[]
    myFile = open("static/db.txt", "r")
    text = myFile.readline()
    while text:
        text = myFile.readline()
        bus = text.split("*")
        bear = bus[0]
        div = '''<div class="Entity">''' + bear + '''</div>'''
        html = div + html
    myFile.close()
    print html
    print html + div
    info = html
    return render_template('search.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
