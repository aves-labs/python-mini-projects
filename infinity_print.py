import time
def prx(Text):
    for i in Text:
        print(i, end="", flush=True)
        time.sleep(0.01)
    print() #for newline

prx("==================Please Type Your Text Below=================================")
Text = input("------->")
prx("How many Times/Interval?: ")
Interval = int(input())
prx("DO you suggest 1. Printx or 2. Print ?")
Type = int(input("------->"))
if Type == 1:
    for i in range(1, Interval+1):
        prx(Text)
else:
    for i in range(1, Interval+1):
        print(Text)
