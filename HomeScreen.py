#external libs
import dominate
from dominate.tags import *


import json, sys
# website title
Website_title = "GitFitness"




def HomeScreen():

    with open("../data/data.json", "r") as read_file:
        files = json.load(read_file)

    doc = dominate.document(title=Website_title)

    # link css/js
    with doc.head:
        link(rel="stylesheet", href="ricette-html/style.css")
        # script(type='text/javascript', src='script.js')
    #adding the files to the homepage:

    with doc:
        with div(cls="container"):
            h1("GitFitness")
            p("Il sito web semplice e leggero per chi non vuole pubblicità fastidiosa e tempi di caricamento infiniti.")
                
            h2("Ricette Disponibili:")
            
            with div(id="header").add(ul()):
                for file in files:
                    li(a(file.replace("-", " ").title(), href="ricette-html/"+file))


            h1("Progetto:")
            p("Sito web open source a cui si può contribuire utilizzando github")
            
            ul(li("Per inviare nuove ricette o consultare il progetto:",a("github", href="github.com"), __pretty=False))


    # writing one the html file, idk wtf is sys.stdout but idc:3
    # basically somehow it gets the html onto homepage.html
    
    original = sys.stdout
    with open("../homepage.html", "w") as f:
        sys.stdout = f
        print(doc)
        sys.stdout = original


if __name__ == "__main__":
    pass