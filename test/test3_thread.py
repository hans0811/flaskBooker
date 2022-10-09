import threading
import time

request = None

def worker():
    print('First Thread')
    t = threading.current_thread()
    time.sleep(8)
    print(t.name)

# second thread
new_t = threading.Thread(target=worker, name='The_great_thread_00')
new_t.start()

# Main thread
t = threading.current_thread()
print('')
print(t.name)


