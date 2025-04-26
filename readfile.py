filePath = "read.txt"

with open(filePath,"r",encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    print(f.readlines())