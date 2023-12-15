# -*- coding: utf-8 -*-
# main.py just a module for import in __main__.py
# File main.py:
#

from multi_media_mail import send_email_multimedia
from plain_text_mail import send_email_plaintext

from loguru import logger
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    if not os.path.exists('../tokens/.env'):
        logger.error('tokens/.env not exists')
        exit(1)
    load_dotenv(dotenv_path='../tokens/.env')
    send_from = os.getenv("SEND_FROM")
    send_to = os.getenv('SEND_TO')
    content = f'the test test content'
    send_email_plaintext(_subject='1. test send_email_plaintext subject', _content=content, _send_from=send_from, _to=send_to)
    send_email_multimedia(_subject='2. test  send_email_multimedia subject', _content='ttrst', _image='', _attachment='')
