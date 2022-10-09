# Dict
# manipulate data
# werkzeug local
import threading
import time

from werkzeug.local import Local


# {thread_id_1: value1, thread_id2:value2}
# Define an object - L which is lock thread
# t1 L..a, t2 L.a
# LocalStack Local
# Local use dict
# Local encapsulate local
# Encapsulate

class A:
    b = 1


# my_obj = A()
my_obj = Local()
my_obj.b = 1


def worker():
    # new thread
    my_obj.b = 2
    print('in new thread b is: ' + str(my_obj.b))


new_t = threading.Thread(target=worker, name='Test1')
new_t.start()
time.sleep(1)
# Main thread
print('in main thread b is: ' + str(my_obj.b))
