from utils.logUtil import init_logging
import sys


def test1():
    logger = init_logging()
    logger.info(sys.platform)


test1()
