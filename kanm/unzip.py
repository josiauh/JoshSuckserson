import base64
import sys
zfile = sys.argv[1]
with open(zfile, "r") as knmF:
    filesToDo = base64.b16decode(knmF.read()).decode().split("[NFI]")
    filesToDo.pop()
    print(filesToDo)
    sans = [

    ]
    for fl in filesToDo:
        sans.append((fl.split("\n[CONTENTS]")[0], fl.split("\n[CONTENTS]")[1]))
    for filename, contents in sans:
        with open(filename, "w") as f:
            f.write(base64.b64decode(contents).decode("utf-8"))
    print("Unzipped")