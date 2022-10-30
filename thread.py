import threading


def print1():
    while(1):
        print("asdddddddddd")
Main_thread=threading.Thread(target=print1)
Main_thread.start()

while(1):
    print("a7a")

