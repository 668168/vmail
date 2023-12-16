
import time
import os

from email.mime.multipart import MIMEMultipart  # 多个MIME对象的集合,可以添加附件
from email.mime.text import MIMEText  # 文本对象
from email.mime.image import MIMEImage  # 图片对象
from email.mime.audio import MIMEAudio  # 音频对象
from email.utils import formatdate  # 设置邮件时间
from email.header import Header
import email.utils


from ._smtp_config import smtp_config


def read_file_from_current_path(filename):
    # 显示当前路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"当前路径是：{current_path}")

    # 检查文件是否存在
    file_path = os.path.join(current_path, filename)  # 也可以直接使用文件名，如果文件在当前工作目录下
    if not os.path.exists(file_path):
        print(f" ERROR: {file_path} do not exit...。")
        exit(1)

    with open(file_path, 'r', encoding='utf-8') as fb:
        # Read the entire file content
        file_string = fb.read()
        return file_string


def send_email_multimedia(_subject='no subject', _content='', _image='', _attachment=''):
    # -----------------------   step1. 配置邮件msg对象    -----------------------
    message = MIMEMultipart()  # 定义一个MIMEMultipart实例，作为邮件主体处理正文及附件
    message['Subject'] = _subject
    # message['Subject'] = 'chatGPT 每天用量统计'  # 标题
    message['From'] = 'aidog@189.cn'  # 发件人
    # message['To']      = ';'.join         (RECIPIENTS)    # 收件人'1@gmail.com;1@189.cn;1@139.com;1@qq.com'
    # message['Cc']      = ';'.join         (CC_RECIPIENTS) # 抄送人
    message['To'] = 'fanpengtao@gmail.com'  # 收件人'1@gmail.com;1@189.cn;1@139.com;1@qq.com'
    # message['Date'] = formatdate()  # 邮件时间               ，可以不用加

    # 创建一个唯一的Message-ID
    # 没这个id, 会导致gsuite接收block: Messages missing a valid Message-ID header
    msg_id = email.utils.make_msgid(domain='cfpod.com')
    msg['Message-ID'] = msg_id

    # -----------------------   step2. 配置邮件正文    ------------------------
    times = time.strftime("%Y%m%dT%H%M%S%z", time.localtime())
    # html_content = html

    css = read_file_from_current_path(os.path.join('html_template', 'foghorn.css'))
    body = read_file_from_current_path(os.path.join('html_template', 'body.html'))
    html = read_file_from_current_path(os.path.join('html_template', 'index-template.html')).format(css=css, body=body, title=_subject,
                                                                                   content=_content)
    # 定义html内容实例，推荐使用html正文内容，可以附加图片地址，调整格式等
    html_part = MIMEText(_text=html, _subtype='html', _charset='utf-8')
    message.attach(html_part)  # 邮件主体添加html正文

    # -----------------------   step3. 配置邮件正文中图片    ------------------------
    if '' != _image:
        image_name = os.path.basename(_image)
        with open(_image, 'rb') as fp:
            # 这里和附件格式有点差异
            image_part = MIMEImage(fp.read())  # 定义图片内容实例
            image_part['Content-Type'] = 'application/octet-stream'  # 设置内容类型为二进制流
            # image_part['Content-Disposition'] = 'attachment; filename="邮件图片测试.jpg"' # 设置文件名称,直接设置会乱码或不显示，所以使用下面的方法
            # 👉这句有意思,似乎先设定为附件, 但有不显示. 不加的话,图片在189.cn不显示. 在139.com显示.
            image_part.add_header('Content-Disposition', 'attachment',
                                  filename=('gbk', '', image_name))  # 解决中文附件乱码或不显示问题
            image_part.add_header('Content-ID', '<image1>')  # 头信息添加图片cid，用于html正文显示
        message.attach(image_part)  # 邮件主体添加图片

    # -----------------------   step4. 配置邮件附件    ------------------------
    if '' != _attachment:
        attachment_name = os.path.basename(_attachment)
        with open(_attachment, 'rb') as f:
            # 这里和图片格式有点差异
            file_attach = MIMEText(f.read(), 'base64', 'utf-8')  # 定义附件内容实例
            file_attach['Content-Type'] = 'application/octet-stream'  # 设置内容类型为二进制流
            # file_attach['Content-Disposition'] = 'attachment; filename="邮件附件测试.txt"'
            # 设置文件名称,直接设置会乱码或不显示，所以使用下面的方法
            file_attach.add_header('Content-Disposition', 'attachment',
                                   filename=('gbk', '', attachment_name))  # 解决中文附件乱码或不显示问题
        message.attach(file_attach)  # 邮件主体添加附件

    # -----------------------   step2. 配置一个SMTP对象   -----------------------
    smtp_config(message)


if __name__ == '__main__':
    # 直接运行包内的模块
    # 当你直接运行包内的一个模块作为脚本时，这个模块的
    # __name__
    # 属性会被设置为
    # '__main__'，而不是它在包结构中的完整路径。这样会导致Python不能识别出相对导入的上下文。
    #
    # 解决方法：不要直接运行包内部的模块。相反，你应该从包的外部运行模块，确保整个包被正确加载。例如，如果你的包名为
    # my_package，你应该这样运行
    # multi_media_mail.py：
    # python -m my_package.multi_media_mail

    from loguru import logger
    from dotenv import load_dotenv

    if not os.path.exists('../tokens/.env'):
        logger.error('tokens/.env not exists')
        exit(1)
    load_dotenv(dotenv_path='../tokens/.env')
    send_from = os.getenv("SEND_FROM")
    send_to = os.getenv('SEND_TO')
    content = f'the test test content'
    send_email_multimedia(_subject='no subject', _content='ttrst', _image='', _attachment='')

