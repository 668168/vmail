# -*- coding: utf-8 -*-

# Package 配置
# File __init__.py:
#
# It is the entry point when your project is used as a library (import mypackage).
#
# It should contain logger.disable("mypackage") unconditionally at the top level.
#
# It should not call logger.add() as it modifies handlers configuration.

# 通过在__init__.py中定义logger，可以在其他模块中直接使用logger，而不需要再次导入。
from loguru import logger

logger.disable("vmail")

# 利用__all__提供包的显式索引
# 当我们直接采用from sound.effects import *时，可能会引用一些不需要的内容，或者导致加载速度过慢。
# 这时我们可以通过在__init__.py中定义一个_all__列表，来指定用 * 时应导入的模块名称列表：
# __all__ = ["echo", "surround", "reverse"]
# 1
# 这样我们就可以维护在import * 时需要导入的模块列表，在发布不同版本的包时很有用。
__all__ = ["multi_media_mail", "plain_text_mail"]

print('import vmail package by __main__.py')
