# -*- coding: utf-8 -*-

"""启动web server"""

import logging

from application import application
from tornado.options import define, options

# tornado没有的命令要通过define定义(logging等命令有了)
define("port", 8880, help="define http port", type=int)

        
if __name__ == "__main__":
    options.logging = "debug"           # *1
#     options.log_file_prefix = "var/log/test_log@8880.log"
    options.parse_command_line()
    from share import ioloop
    # 启动http服务
    application.listen(options.port)
    logging.debug("http server:%s", options.port)
    # IO 循环
    ioloop.start()
    # python main.py --port=8880 --logging=warning  # 这里的会覆盖 *1行的
