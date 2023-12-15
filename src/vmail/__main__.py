# -*- coding: utf-8 -*-

# Module 配置
# File __main__.py:
#
# It is the entry point when your project is used as an application (python -m mypackage).
# It can contain logging configuration unconditionally at the top level.

# 通过在__main__.py中定义logger，可以在模块内中直接使用logger，而不需要再次导入。
from loguru import logger

logger.disable("vmail")
print('import vmail module by __main__.py')




