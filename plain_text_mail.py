from email.mime.text import MIMEText  # 文本对象
from ._smtp_config import smtp_config


def send_email_plaintext(_subject='', _content='', _send_from='', _to=''):
    # -----------------------  step1. 获取 parameters   -----------------------
    if _send_from == '':
        _send_from = os.getenv('SEND_FROM')
    if _to == '':
        _send_to = os.getenv('SEND_TO')
    if _subject == '':
        _subject = os.getenv('SUBJECT')
    if _content == '':
        _content = os.getenv('CONTENT')
    # -----------------------   step2. 配置邮件msg对象    -----------------------
    msg = MIMEText(_content)  # 邮件内容
    # msg['Subject'] = f'chatGPT 订阅地址每周定时自动发送 @ {times}'  # 邮件主题
    msg['Subject'] = _subject  # 邮件主题
    msg['From'] = _send_from  # 发件人
    msg['To'] = _to  # 收件人

    # -----------------------   step3. 配置一个SMTP对象   -----------------------
    smtp_config(msg)


def vnotify():
    send_email_plaintext()


if __name__ == '__main__':
    from loguru import logger
    import os
    from dotenv import load_dotenv

    if not os.path.exists('../tokens/.env'):
        logger.error('tokens/.env not exists')
        exit(1)
    load_dotenv(dotenv_path='../tokens/.env')
    send_from = os.getenv("SEND_FROM")
    send_to = os.getenv('SEND_TO')
    content = f'the test test content'
    send_email_plaintext(_subject='test subject', _content=content, _send_from=send_from, _to=send_to)
