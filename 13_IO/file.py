from datetime import datetime

file_path = "/Users/guihua.pgh/workspace/python/2024-study/13_IO/test.txt"

with open(file_path, "w") as f:
    f.write("open for write...")
    f.write(datetime.now().strftime("%Y-%m-%d"))

with open(file_path, "r") as f:
    s = f.read()
    print("open for read...")
    print(s)

with open(file_path, "rb") as f:
    s = f.read()
    print("open as binary for read...")
    print(s)