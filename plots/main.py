import matplotlib.pyplot as plt
import numpy as np
print("Plotting Prompt")
ox = []
oy = []
while True:
    try:
        cmd = input("plt > ")
        cmd = cmd.split(" ")
        args = cmd[1:]
        if cmd[0] == "addData":
            if len(cmd) < 5:
                print("No data to add.")
                continue
            ox.append(args[0])
            ox.append(args[3])
            oy.append(args[2])
            oy.append(args[1])     
        if cmd[0] == "pie":
            print("Only using X.")
            x = np.array(ox)
            plt.pie(x)
            plt.show()
        if cmd[0] == "line":
            x = np.array(ox)
            y = np.array(oy)
            plt.plot(x,y)
            plt.show()     
        if cmd[0] == "points":
            if len(oy) != len(ox):
                print("Not enough items in X and Y.")
                print(f"X: {len(ox)}")
                print(f"Y: {len(oy)}")
            x = np.array(ox)
            y = np.array(oy)
            plt.plot(x,y,'o')
            plt.show()
        if cmd[0] == "exit":
            exit()
        if cmd[0] == "showData":
            print(ox)
            print(oy)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)