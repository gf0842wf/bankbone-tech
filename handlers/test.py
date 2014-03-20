# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
import json

class TestModelHandler(BaseHandler):
    
    def get(self):
        self.render("test_model.html")
        
    def post(self):
        print self.raw
        self.set_header("Content-Type", "application/json")
        self.write({"message":"test post ok"})
        
        
class TestModelGetHandler(BaseHandler):
    
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write({"message":"test post ok"})

class TestCollectionHandler(BaseHandler):
    
    def get(self):
        self.render("test_collection.html")
        
class TestCollectionGetHandler(BaseHandler):
    
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps([{"title":"book1_server"}, {"title":"book2_server"}, {"title":"book4"}]))
#         self.render("test_collection.html")

class TestRouterHandler(BaseHandler):
    
    def get(self):
        self.render("test_router.html")
    
__all__ = ["TestModelHandler", "TestModelGetHandler", "TestCollectionHandler", "TestCollectionGetHandler", "TestRouterHandler"]