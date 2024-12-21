import threading
from file1 import Class1
from file2 import Class2
from file3 import Class3
from file4 import Class4

def thread_function1():
    obj1 = Class1()
    obj1.method1()

def thread_function2():
    obj2 = Class2()
    obj2.method2()

def thread_function3():
    obj3 = Class3()
    obj3.method3()

def thread_function4():
    obj4 = Class4()
    obj4.method4()

if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=thread_function1)
    thread2 = threading.Thread(target=thread_function2)
    thread3 = threading.Thread(target=thread_function3)
    thread4 = threading.Thread(target=thread_function4)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("All threads have completed their tasks.")
