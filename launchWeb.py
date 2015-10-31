from sys import argv
from flask import Flask, render_template, escape, Markup, request
app = Flask(__name__)

def openFile( version, wID, wTYPE, wNAME ):
    #Initializing values
    bus = []
    bear = []
    memoriZe = []
    html = '''<div id="organize">'''
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
               pass
           elif (wTYPE != TYPE and version == 3):
               pass
           elif (wNAME != NAME and version == 1):
               pass
           else:
               #Creating html for image + name
               #Decided to add a number to the class so I have more css control
               # over different pages even though this does mean repetition in
               # the css. More code could alow an addition class to be placed
               # though.
               div  = '''<div class="entity"><a href="http://localhost:5000/specific/?ID=''' + ID + '''">''' + NAME + '''</a>'''
               div  = div + '''<a href="http://localhost:5000/specific/?ID=''' + ID + '''"><img src="''' + IMAG + '''" align="left"></a>'''
               #Creating html for Type and Description
               if (wID == ID and version == 2):
                   div = div + '''<p></p><b>Type: </b>''' + TYPE + '''<p></p><b>Description: </b>''' + DESC + '''</div><div class="seperate"></div>'''
               html = html + div
    myFile.close()
    html = html + '''</div>'''
    info = Markup(html)
    return info

@app.route('/')
def home():
    return render_template('home.html')

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = TYPE HERE
@app.route('/type/<TYPE>', methods=['GET','POST'])
def type(TYPE):
    version = 3
    wNAME = ""
    wTYPE = TYPE.replace('_', ' ')
    wID = ""
    print wTYPE
    info = openFile( version, wID, wTYPE, wNAME )
    return render_template('type.html', info=info)


@app.route('/specific/', methods=['GET','POST'])
def specific():
    ID = request.args.get('ID')
    version = 2
    wNAME = ""
    wTYPE = ""
    wID = ID
    print wID
    info = openFile( version, wID, wTYPE, wNAME )
    print info
    return render_template('specific.html', info=info)


@app.route('/search/', methods=["GET","POST"])
def search():
    SEARCH = request.args.get('key')
    print "working? :: %s" % SEARCH
    version = 1
    wNAME = SEARCH
    wTYPE = ""
    wID = ""
    info = openFile( version, wID, wTYPE, wNAME )
    return render_template('search.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
