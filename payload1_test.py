import time
import os
import subprocess
print("hello world")
text = "Pablo serait pas fier de ton incompétence totale :("

time.sleep(5)

with open("pablo.txt", "w") as file:
    file.write(text)

subprocess.run(["notepad.exe", "pablo.txt"])