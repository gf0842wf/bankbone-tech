# -*- coding: utf-8 -*-

# 共享对象

# import weakref
from tornado.ioloop import IOLoop

ioloop = IOLoop.instance()


__all__ = ["ioloop"]