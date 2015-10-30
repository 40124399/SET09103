from sys import argv
from flask import Flask, render_template, escape, Markup
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

    #Initializing values
    bus = []
    bear = []
    memoriZe = []
    html = ''
    empty = ''

    myFile = open("static/db.txt", "r")
    text = myFile.readline()
    while text:
        text = myFile.readline()
        if text != empty:
           bus = text.split("*")
           #Creating image with custom link
           ID   = bus[0]
           NAME = bus[1]
           TYPE = bus[2]
           DESC = bus[3]
           IMAG = bus[4]
           div  = '''<div class="entity"><a href="specific/?ID=''' + ID + '''">''' + NAME + '''</a>'''
           div  = div + '''<a href="specific/?ID=''' + ID + '''"><img src="''' + IMAG + '''" align="left"></a>'''
           div  = div + '''<p></p><b>Type: </b>''' + TYPE + '''<p></p><b>Description: </b>''' + DESC + '''</div><div class="seperate"></div>'''
           html = div + html
    myFile.close()
    print html
    info = Markup(html)
    print info
    #return info
    return render_template('search.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
