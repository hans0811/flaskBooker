import json

from flask import jsonify, request, render_template, flash

from app.spider.booker_book import BookerBook
from app.libs.helper import is_isbn_or_key
from . import web
from app.forms.book import SearchForm
from ..view_models.book import BookViewModel, BookCollection


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }

    r1={

    }
    flash('Hello, Hans', category='error')
    flash('Hello, This is Oct.', category='warning')
    # Template
    return render_template('test.html', data=r, data1=r1)

@web.route('/test1')
def test1():
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print(n.v)
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''

@web.route('/book/search')
def search():
    # app.add_url_rule
    # # At least 1 character
    # q = request.args['q']
    # # length limit
    # page = request.args['page']

    form = SearchForm(request.args)
    books = BookCollection()

    ## validation layer
    if form.validate():
        q = form.q.data.strip() # delete space
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        booker_book = BookerBook()

        if isbn_or_key == 'isbn':
            booker_book.search_by_isbn(q)
        else:
            booker_book.search_by_keyword(q, page)
        books.fill(booker_book, q)

        #return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
        #__dict__
        #return jsonify(books)
    else:
        flash('Please input again')
        #return jsonify(form.errors)

    return render_template('search_result.html', books=books)
    #return json.dumps(result), 200, {'content-type': 'application/json'}

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    booker_book = BookerBook()
    booker_book.search_by_isbn(isbn)
    book = BookViewModel(booker_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])