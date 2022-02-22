#pip install markdown
import markdown
print(markdown)

with open("esempio.md", "r", encoding="utf8") as file:
    text = file.read()
html = markdown.markdown(text)

with open("esempio.html", "w", encoding="utf-8") as file:
    file.write(html)
print("done")