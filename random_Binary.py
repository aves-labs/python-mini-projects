import time
import random
interval = int(input("Numbers To Print: "))
for i in range(1, interval+1):
    print(random.randint(0, 1), end="", flush="True")
    time.sleep(0.0001)
print()  # It is for Newline ;)
print("Task Completed!")
