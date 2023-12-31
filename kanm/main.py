
# import required module
import base64
import os
import sys

if "--help" in sys.argv or "-h" in sys.argv:
    print(f"""Usage: {sys.argv[0]} [directory] [knm file]
Zips a whole directory to a knm file.""")
    exit(0)

if len(sys.argv) < 3:
    print("2 arguments needed. found " + str(len(sys.argv) - 1) + " args.")
    exit(0)

# assign directory
directory = sys.argv[1]
 
# iterate over files in
# that directory
with open(sys.argv[2] if sys.argv[2].endswith('.knm') else sys.argv[2] + ".knm", "a") as a:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f, "r") as fi:
                
                a.write(base64.b16encode(bytes(filename + "\n[CONTENTS]" + base64.b64encode(bytes(fi.read(), 'utf-8')).decode("utf-8") + "\n[NFI]", 'utf-8')).decode())
        