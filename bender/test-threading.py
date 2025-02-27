import threading
import time


def my_thread():
    count: int = 0

    while count < 10:
        print(f"[{count}] printing...")
        count += 1
        time.sleep(1)


th = threading.Thread(target=my_thread)
th.start()

text = ""
while text != "exit":
    text: str = input("> ")

    print("your text:", text)


th.join()
