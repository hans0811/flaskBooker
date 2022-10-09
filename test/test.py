from flask import Flask, current_app, request, Request

app = Flask(__name__)
# application context
# Request context
# Flask AppContext
# Request RequestContext

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# using with (__enter__ and __exit__)
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# Object with context instance can use with
# context manager
# The object implements __enter__ and __exit__

# Example
# 1. connect DB
# 2. execute sql
# 3. release

# try -> except -> finally:
# __enter__, __exit__( release resource)

# try:
#     f = open(r'hans/test.txt')
#     print(f.read())
# finally:
#     f.close()
#
# #
# with open(r"") as f:
#     print(f.read())
#
class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    # only return true or false
    # Default is none, and none is false
    # False -> it give expection
    # True -> close
    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        return True

    def query(self):
        print('query data')

# A need return __enter__, and __exit__
# obj_A is empty
try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass