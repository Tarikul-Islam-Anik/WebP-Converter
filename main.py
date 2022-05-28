import subprocess
import os

img_list = os.listdir("in/")

for i in img_list:
    cmd = f'"bin/cwebp.exe" "in/{i}" -o "out/{i.split(".")[0]}.webp"'
    subprocess.Popen(cmd, shell=True)
