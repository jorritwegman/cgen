from datetime import datetime

rawText = []
metadata = {
    "program": "Program: " + input("Name of program: "),
    "desc": "Description: " + input("Description of program: "),
    "author": "Author: " + input("Name of programs author: ")
}

if input("Include date in comment? (Y/n): ").lower() == "y":
    metadata["Date"] = "Date: " + datetime.today().strftime('%Y-%m-%d')

for data in metadata.values():
    if "".join(data.split(':')[1].split()) != "":
        rawText.append(data)

maxLen = max([len(v) for v in rawText])
tbRow = "# " + "*" * (maxLen + 4)

with open("comment.txt", "w") as file:
    file.write(tbRow + "\n")
    for data in rawText:
        space = str(len(tbRow) - 2)
        row = "# * " + data
        line = ("{:" + space + "}").format(row) + " *\n"
        file.write(line)
    file.write(tbRow)