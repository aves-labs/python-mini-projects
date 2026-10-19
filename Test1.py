import time, random
user_input = int(input("Numbers To Print: "))
user_time = int(input("Interval Time: "))
for i in range(1, user_input):
    print(random.randint(0,1), end="", flush="True")
    time.sleep(int(user_time/1000))

print() #newline
print("Completed!")
