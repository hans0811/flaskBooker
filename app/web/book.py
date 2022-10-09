from flask import jsonify, request

from app.spider.booker_book import BookerBook
from app.libs.helper import is_isbn_or_key
from . import web
from app.forms.book import SearchForm
from ..view_models.book import BookViewModel


@web.route('/test')
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
    # validation layer
    if form.validate():
        q = form.q.data.strip() # delete space
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = BookerBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = BookerBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)

    #return json.dumps(result), 200, {'content-type': 'application/json'}