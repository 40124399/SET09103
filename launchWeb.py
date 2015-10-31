from sys import argv
from flask import Flask, render_template, escape, Markup
app = Flask(__name__)

def openFile( version, wID, wTYPE, wNAME ):
    print "function running..."
    #Initializing values
    bus = []
    bear = []
    memoriZe = []
    html = ''
    empty = ''
    #All vlues initialized

    #Opening File
    myFile = open("static/db.txt", "r")
    text = myFile.readline()
    while text:
        text = myFile.readline()
        if text != empty:
           bus = text.split("*")
           #Creating custom links
           ID   = bus[0]
           NAME = bus[1]
           TYPE = bus[2]
           DESC = bus[3]
           IMAG = bus[4]
           if (wID != ID and version == 2 and wID != ""):
               print "passing"
               pass
           elif (wTYPE != TYPE and version == 3):
               print "passing"
               pass
           elif (wNAME != NAME and version == 1):
               print "passing"
               pass
           else:
               #Creating html for image + name
               div  = '''<div class="entity"><a href="http://localhost:5000/specific/?ID=''' + ID + '''">''' + NAME + '''</a>'''
               div  = div + '''<a href="http://localhost:5000/specific/?ID=''' + ID + '''"><img src="''' + IMAG + '''" align="left"></a>'''
               #Creating html for Type and Description
               if (wID == ID and version == 2):
                   div  = div + '''<p></p><b>Type: </b>''' + TYPE + '''<p></p><b>Description: </b>''' + DESC + '''</div><div class="seperate"></div>'''
               html = div + html
    myFile.close()
    info = Markup(html)
    print "function ran."
    return info

@app.route('/')
def home():
    work = "search"
    return render_template('home.html', work=work)

@app.route('/specific/<ID>', methods=['GET','POST'])
def specific(ID):
    version = 2
    wNAME = ""
    wTYPE = ""
    wID = ID
    print wID
    info = openFile( version, wID, wTYPE, wNAME )
    print info
    return render_template('specific.html', info=info)


@app.route('/search/<SEARCH>', methods=["GET","POST"])
def search(SEARCH):
    version = 1
    wNAME = SEARCH
    wTYPE = ""
    wID = ""
    info = openFile( version, wID, wTYPE, wNAME )
    return render_template('search.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
