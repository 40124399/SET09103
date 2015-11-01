from sys import argv
from flask import Flask, render_template, escape, Markup, \
     request, redirect, url_for
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
           bus  = text.split("*")
           #Creating custom links
           ID   = bus[0]
           NAME = bus[1]
           TYPE = bus[2]
           DESC = bus[3]
           IMAG = bus[4]
           NAME = NAME.lower()
           wNAME = wNAME.lower()
           if (wNAME in NAME and version == 1):
               bool = 1
           else:
               bool = 0
           if (wID != ID and version == 2 and wID != ""):
               pass
           elif (wTYPE != TYPE and version == 3):
               pass
           elif (wNAME != NAME and version == 1 and bool == 0):
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


@app.route('/test/', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
      bus = []
      empty = ""
      biggest = int(1)
      wNAME = request.form['wNAME']
      wDESC = request.form['wDESC']
      wIMAG = request.form['wIMAG']
      wTYPE = request.form['wTYPE']
      print wNAME
      if not all((wNAME, wDESC)):
          print "empty"
      else:
          book = open("static/db.txt", "r+")
          line = book.readline()
          while line:
              line = book.readline()
              bus = line.split('*')
              if not all((bus)):
                  print "empty"
              else:
                  ID = bus[0]
                  ID = int(ID)
                  if ID >= biggest:
                      biggest = int(ID) + 1

          biggest = str(biggest)
          newEntry = biggest + "*" + wNAME + "*" + wTYPE + "*" + wDESC + "*" + wIMAG + "\n"
          book.write(newEntry)
          book.close()
    action = ""
    methodType = "POST"
    return render_template('dbAdd.html', action=action, methodType=methodType)



@app.route('/dbAdd/')
def newDB():
    bus = []
    empty = ""
    biggest = int(1)
    wNAME = request.args.get('wNAME')
    wDESC = request.args.get('wDESC')
    wIMAG = request.args.get('wIMAG')
    wTYPE = request.args.get('wTYPE')
    if not all((wNAME, wDESC)):
        print "empty"
    else:
        book = open("static/db.txt", "r+")
        line = book.readline()
        while line:
            line = book.readline()
            bus = line.split('*')
            if not all((bus)):
                print "empty"
            else:
                ID = bus[0]
                ID = int(ID)
                if ID >= biggest:
                    biggest = int(ID) + 1

        biggest = str(biggest)
        newEntry = biggest + "*" + wNAME + "*" + wTYPE + "*" + wDESC + "*" + wIMAG + "\n"
        book.write(newEntry)
        book.close()
        return redirect(url_for('newDB'), 301)
    print "lol"
    action = "http://localhost:5000/dbAdd/"
    methodType = ""
    return render_template('dbAdd.html', action=action, methodType=methodType)

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
    version = 1
    wNAME = SEARCH
    wTYPE = ""
    wID = ""
    info = openFile( version, wID, wTYPE, wNAME )
    return render_template('search.html', info=info)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'), 301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
