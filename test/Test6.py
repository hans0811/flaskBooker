import threading
import time

from werkzeug.local import LocalStack

# push, pop, top

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push, the value is ' + str(my_stack.top))

def worker():
    print('in the new thread before push, value is: ' + str(my_stack.top))
    my_stack.push(2)
    print('in the new thread after push, value is: ' + str(my_stack.top))

new_t = threading.Thread(target=worker, name='First_thread')
new_t.start()
time.sleep(1)
# Main
print('Finally, in main thread value is: ' + str(my_stack.top))