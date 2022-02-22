import os

path = "../ricette-md"
os.chdir("ricette-html")
for file in os.listdir(path):
    if file.endswith(".md"):
        # print("creando per...",os.path.join(path, file))
        # installare pandoc, https://pandoc.org/installing.html
        # print("{}".format(file))
        
        # print(os.getcwd())
        file = file.replace(".md", ".html")

        # print("{}".format(file))

        if os.path.isfile(file) == True:
            print("file già presente: {}".format(file))
            
        else:
            print("file non esistente")
            os.system("pandoc ../ricette-md/{} -s -c style.css -o {}".format(file.replace(".html", ".md"), file))
        