# -*- coding: UTF8 -*-
import json
import logging.config
import os


def init_logging(path='../config/logger.json', level='logging.DEBUG'):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    return logger

