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
    bus = []
    bear = []
    html = ''
    empty = ''
    memoriZe = []
    myFile = open("static/db.txt", "r")
    text = myFile.readline()
    while text:
        text = myFile.readline()
        if text != empty:
           bus = text.split("*")
           bear = bus[2]
           div = '''<div class="Entity">''' + bear + '''</div>'''
           html = div + html
    myFile.close()
    print html
    html = escape(html)
    info = html
    print info
    #return info
    return render_template('search.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
