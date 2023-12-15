# -*- coding: utf-8 -*-

import os
import smtplib


def smtp_config(_msg):
    # TODO: config save to env file is best practice
    # -----------------------   step1. 配置一个SMTP对象   -----------------------
    # SMTP_SERVER, SSL_PORT, PORT = 'smtp.189.cn', 465, 25
    # ACCOUNT, PASSWORD = 'aidog@189.cn', 'Xd#7Vw@1v#2Tv@7J'
    # with open('tokens/.env', 'r', encoding='utf-8') as f:
    #     credentials = f.read().strip().split('\n')
    # credentials = [credential.split(',', 1) for credential in credentials]
    # logger.debug(f'credentials = {credentials}')

    smtp_obj = smtplib.SMTP_SSL(host=os.getenv('SMTP_SERVER'), port=os.getenv('SSL_PORT'))  # 使用Gmail作为例子
    # smtp_obj.set_debuglevel(1)
    smtp_obj.ehlo()  # 打个招呼
    # smtp_obj.ehlo_or_helo_if_needed()  # 打个招呼
    # smtp_obj.starttls()  # 开启TLS加密
    # 登录SMTP服务器
    smtp_obj.login(user=os.getenv('SEND_FROM'), password=os.getenv('PASSWORD'))
    # 发送邮件
    smtp_obj.send_message(_msg)
    # 关闭与SMTP服务器的连接
    smtp_obj.quit()

if __name__ == '__main__':
    pass
