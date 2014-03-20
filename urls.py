# -*- coding: utf-8 -*-

from handlers.errors import PageNotFoundHandler
from handlers.test import TestModelHandler, TestModelGetHandler, TestCollectionHandler, TestCollectionGetHandler, TestRouterHandler

urls = [
    (r"/test_model/", TestModelHandler),
    (r"/test_model/test_get", TestModelGetHandler),
    (r"/getbooks", TestCollectionHandler),
    (r"/getbooks/", TestCollectionGetHandler),
    (r"/test_router", TestRouterHandler),
    
    # 在最后加一个 PageNotFoundHandler 来处理这里没有的请求(贪婪匹配,一直匹配到最后,发现没有,就调用这个handler了)
    # PageNotFoundHandler 的 get 里 raise tornado.web.HTTPError(404)即可
    (r".*", PageNotFoundHandler),
    ]

