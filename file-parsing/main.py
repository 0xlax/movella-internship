"""
Sample log file parser which will parse the log file, and writes to 3 different log files
"""


import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_info_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def setup_debug_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def setup_error_logger(name, log_file, level=logging.ERROR):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


info_logger = setup_info_logger('info_logger', 'info.log')
info_logger.info('This is just info message')

debug_logger = setup_debug_logger('debug_logger', 'debug.log')
debug_logger.debug('This is just debug message')

error_logger = setup_error_logger('error_logger', 'error.log')
error_logger.error('This is just error message')