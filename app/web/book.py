from flask import jsonify, Blueprint

from booker_book import BookerBook
from helper import is_isbn_or_key
from . import web

@web.route('/book/search/<q>/<page>')
def search(q, page):
    # app.add_url_rule("url")
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = BookerBook.search_by_isbn(q)
    else:
        result = BookerBook.search_by_keyword(q)
    return jsonify(result)
    #return json.dumps(result), 200, {'content-type': 'application/json'}