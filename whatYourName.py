import time

print(("AI：你叫什么名字"))
t = input("你：")

for i in range(6):
    print(".", end="", flush=False)
    time.sleep(1)
print("\nAI：你好，%s！" % t)
