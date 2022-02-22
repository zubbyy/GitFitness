#internal libs
import os
import HomeScreen
import json
#external libs


###############################
#pagination


files = []


###############################
# main





def Conversion():
    # changing converting markdown recipes to html files 
    path = "../ricette-md"
    os.chdir("ricette-html")
    for file in os.listdir(path):
        if file.endswith(".md"):
            # print("creando per...",os.path.join(path, file))
            # installare pandoc, https://pandoc.org/installing.html
            # print("{}".format(file))
            
            # print(os.getcwd())
            file = file.replace(".md", ".html")

            files.append(file)
            # print("{}".format(file))
            with open("../data/data.json", "w") as json_string:
                json.dump(files, json_string)
            if os.path.isfile(file) == True:
                #if the html file is already present we don't download it again

                # print("file già presente: {}".format(file))
                pass
                
            else:
                #if the html file doesn't exist, we use pandoc to make it from a markdown file
                print("file non esistente")
                os.system("pandoc ../ricette-md/{} -s -c style.css -o {}".format(file.replace(".html", ".md"), file))






Conversion()
HomeScreen.HomeScreen()