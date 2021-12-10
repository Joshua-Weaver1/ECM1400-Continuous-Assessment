"""This module will contain the formatting for my logger to remove the requirement
of defining it in individual modules"""

import logging
logging.basicConfig(filename='sys.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d | %(module)s | %(name)s  | %(levelname)s | %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
