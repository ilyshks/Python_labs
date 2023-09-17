import os


s = input()
res = 0
try:
    for filename in os.listdir("example/"):
        if s in filename:
            res += 1
    print(res)
except FileNotFoundError:
    print("Нет такой директориии!")

